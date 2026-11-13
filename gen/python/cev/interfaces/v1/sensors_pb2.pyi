from cev.interfaces.v1 import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Imu(_message.Message):
    __slots__ = ("stamp_ns", "linear_acceleration", "angular_velocity")
    STAMP_NS_FIELD_NUMBER: _ClassVar[int]
    LINEAR_ACCELERATION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    stamp_ns: int
    linear_acceleration: _common_pb2.Vector3
    angular_velocity: _common_pb2.Vector3
    def __init__(self, stamp_ns: _Optional[int] = ..., linear_acceleration: _Optional[_Union[_common_pb2.Vector3, _Mapping]] = ..., angular_velocity: _Optional[_Union[_common_pb2.Vector3, _Mapping]] = ...) -> None: ...

class WheelSpeed(_message.Message):
    __slots__ = ("stamp_ns", "rev_per_s")
    STAMP_NS_FIELD_NUMBER: _ClassVar[int]
    REV_PER_S_FIELD_NUMBER: _ClassVar[int]
    stamp_ns: int
    rev_per_s: float
    def __init__(self, stamp_ns: _Optional[int] = ..., rev_per_s: _Optional[float] = ...) -> None: ...
