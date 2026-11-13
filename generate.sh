#!/usr/bin/env bash
# Regenerates gen/ from the versioned definitions under proto/cev/interfaces.
# CI runs this script and
# fails the PR if gen/ changes, so commit its output with every .proto change.
#
# Needs: curl, unzip, and protoc-gen-prost on PATH:
#   cargo install --locked protoc-gen-prost --version 0.5.0
# Downloads protoc into .tools/ on first run.
set -euo pipefail
cd "$(dirname "$0")"

# Generated code differs between generator versions. CI pins the same ones.
# The Python runtime must match PROTOC_VERSION: protobuf 7.35.1.
PROTOC_VERSION=35.1
PROTOC_GEN_PROST_VERSION=0.5.0

case "$(uname -s)-$(uname -m)" in
    Linux-x86_64) platform=linux-x86_64 ;;
    Linux-aarch64) platform=linux-aarch_64 ;;
    Darwin-arm64) platform=osx-aarch_64 ;;
    Darwin-x86_64) platform=osx-x86_64 ;;
    *) echo "no protoc release for $(uname -s)-$(uname -m)" >&2; exit 1 ;;
esac

protoc_dir=".tools/protoc-$PROTOC_VERSION"
if [[ ! -x "$protoc_dir/bin/protoc" ]]; then
    mkdir -p "$protoc_dir"
    url="https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOC_VERSION/protoc-$PROTOC_VERSION-$platform.zip"
    curl -fsSL "$url" -o "$protoc_dir/protoc.zip"
    unzip -q "$protoc_dir/protoc.zip" -d "$protoc_dir"
    rm "$protoc_dir/protoc.zip"
fi

if [[ "$(protoc-gen-prost --version 2>/dev/null)" != "$PROTOC_GEN_PROST_VERSION" ]]; then
    echo "need protoc-gen-prost $PROTOC_GEN_PROST_VERSION on PATH" >&2
    exit 1
fi

rm -rf gen/python gen/rust/src
mkdir -p gen/python gen/rust/src

"$protoc_dir/bin/protoc" \
    --proto_path=proto \
    --plugin=protoc-gen-prost="$(command -v protoc-gen-prost)" \
    --prost_out=gen/rust/src \
    --prost_opt=bytes=. \
    --python_out=gen/python \
    --pyi_out=gen/python \
    cev/interfaces/v1/common.proto

# protoc-gen-prost nests output by package. One package, so the generated
# module is the whole crate.
mv gen/rust/src/cev/interfaces/v1/cev.interfaces.v1.rs gen/rust/src/lib.rs
rm -r gen/rust/src/cev
