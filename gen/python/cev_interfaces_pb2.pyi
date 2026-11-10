from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vector3(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Imu(_message.Message):
    __slots__ = ("stamp_ns", "linear_acceleration", "angular_velocity")
    STAMP_NS_FIELD_NUMBER: _ClassVar[int]
    LINEAR_ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    stamp_ns: int
    linear_acceleration: Vector3
    angular_velocity: Vector3
    def __init__(self, stamp_ns: _Optional[int] = ..., linear_acceleration: _Optional[_Union[Vector3, _Mapping]] = ..., angular_velocity: _Optional[_Union[Vector3, _Mapping]] = ...) -> None: ...

class WheelSpeed(_message.Message):
    __slots__ = ("stamp_ns", "rev_per_s")
    STAMP_NS_FIELD_NUMBER: _ClassVar[int]
    REV_PER_S_FIELD_NUMBER: _ClassVar[int]
    stamp_ns: int
    rev_per_s: float
    def __init__(self, stamp_ns: _Optional[int] = ..., rev_per_s: _Optional[float] = ...) -> None: ...
