# cev-interfaces

This repo is used to store struct formats used to transmit data on CEV
vehicles. It intends to standardize commonly-used data types, providing
modular serialization code to reduce drift across codebases and improve the
developer experience on CEV.

Structs are stored as [Protobuf](https://protobuf.dev/) definitions
(`.proto`). Protobuf is a mechanism developed by Google that enables
standardized, lightweight serialization that works across platforms.

## Why Protobuf?

In Fall 2026, CEV began switching from ROS 2 to a custom middleware based
on the Zenoh publisher-subscriber protocol. At the same time, we began writing
all new autonomy algorithms in Rust (and migrating some existing ones).

These changes introduced a need for custom pub-sub message definitions. Our
main requirements are:

- Standardization. Without a standard, people tend to write custom
serialization that ends up as technical debt.
- Language cross-compatibility. This ideally includes code generation i.e.
automatically turning a language-agnostic type into a struct defined in a
specific language.

Protobuf supports both of these, and is the industry standard for effeciently
converting arbitrary types into raw bytes.

## Messages

`proto/cev_interfaces.proto`:
| topic | data name | type | type vague description |
|---|---|---|---|
| cev/sensors/imu | imu data | `Imu` | timestamp + floats for each of the accelerometer data (f/b, l/r, u/d) and gyroscope (roll pitch yaw) - 6dof |
| cev/sensors/wheels/left_rpm | left wheel rpm | `WheelSpeed` | timestamp + rotations/s, float |
| cev/sensors/wheels/right_rpm | right wheel rpm | `WheelSpeed` | timestamp + rotations/s, float |

## Usage

Messages are defined as `.proto` files in `proto/`. Every PR to this repo
triggers CI to run `generate.sh`, which in turn runs `protoc` to compile
modified `.proto` files into Rust and Python code in `gen/`. This directory
contains the corresponding structs (or equivalent, depending on language) which
you can import into your projects.

We recommend adding this entire repo into your code as a Git submodule.
Although this will likely carry some unnecessary code, it's the easiest way to
track updates.

TODO: Figure out what C++ version we want to support and how to get protoc to work with it