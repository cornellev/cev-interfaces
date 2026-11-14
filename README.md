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

`proto/cev/interfaces/v1/sensors.proto`:
| topic | data name | type | type vague description |
|---|---|---|---|
| cev/sensors/imu | imu data | `Imu` | timestamp + floats for each of the accelerometer data (f/b, l/r, u/d) and gyroscope (roll pitch yaw) - 6dof |
| cev/sensors/wheels/left_rpm | left wheel rpm | `WheelSpeed` | timestamp + rotations/s, float |
| cev/sensors/wheels/right_rpm | right wheel rpm | `WheelSpeed` | timestamp + rotations/s, float |

`proto/cev/interfaces/v1/planning.proto`:
| topic | data name | type | type vague description |
|---|---|---|---|
| cev/planning/goal | goal | `Goal` | timestamp + target pose + how close counts as arrived (m, and optionally heading) |
| cev/vehicle/state | vehicle state | `VehicleState` | timestamp + rear axle pose + speed (m/s) + front wheel steering angle (rad) |
| cev/planning/global_path | global path | `Path` | timestamp + points (pose, speed, steering, time) from the car to the goal on the known map + reaches goal + cost |
| cev/planning/local_path | local path | `Path` | same as global path: the path the driver is following now, updated when it replans |
| cev/planning/status | planner status | `PlannerStatus` | timestamp + mode (follow / replan / stop / done) + message |

TODO add common.proto

## Usage

Messages are defined as `.proto` files in `proto/cev/interfaces/[version]/`. 

Every PR to this repo
triggers CI to run `generate.sh`, which in turn runs `protoc` to compile
modified `.proto` files into Rust and Python code in `gen/`. This directory
contains the corresponding structs (or equivalent, depending on language) which
you can import into your projects.

We recommend adding this entire repo into your code as a Git submodule.
Although this will likely carry some unnecessary code, it's the easiest way to
track updates.

## Contributing

We follow [Protocol Buffers Style Guide](https://protobuf.dev/programming-guides/style/)
and [Google Cloud API directory structure](https://cloud.google.com/apis/design/directory_structure)
best practices regarding naming protobuf files and versioning them. This means
the version number e.g. v1 identifies breaking changes, so we can add new
versions as v2, v3, etc. to allow users to update without breaking their old
code (and to use the new versions at their own pace).

You can find a directory of types in the above Messages section of this README.
If you would
like to add new struct(s), you can feel free to place them wherever makes
the most sense for you as a user. This could mean adding them to existing
`.proto` files or making a new `.proto` file.