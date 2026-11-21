from cev.interfaces.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DriverMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DRIVER_MODE_UNSPECIFIED: _ClassVar[DriverMode]
    DRIVER_MODE_FOLLOW: _ClassVar[DriverMode]
    DRIVER_MODE_REPLAN: _ClassVar[DriverMode]
    DRIVER_MODE_STOP: _ClassVar[DriverMode]
    DRIVER_MODE_DONE: _ClassVar[DriverMode]
DRIVER_MODE_UNSPECIFIED: DriverMode
DRIVER_MODE_FOLLOW: DriverMode
DRIVER_MODE_REPLAN: DriverMode
DRIVER_MODE_STOP: DriverMode
DRIVER_MODE_DONE: DriverMode

class Goal(_message.Message):
    __slots__ = ("header", "pose", "tolerance_m", "use_heading", "heading_tolerance_rad")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_M_FIELD_NUMBER: _ClassVar[int]
    USE_HEADING_FIELD_NUMBER: _ClassVar[int]
    HEADING_TOLERANCE_RAD_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    pose: _common_pb2.Pose2
    tolerance_m: float
    use_heading: bool
    heading_tolerance_rad: float
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., pose: _Optional[_Union[_common_pb2.Pose2, _Mapping]] = ..., tolerance_m: _Optional[float] = ..., use_heading: _Optional[bool] = ..., heading_tolerance_rad: _Optional[float] = ...) -> None: ...

class VehicleState(_message.Message):
    __slots__ = ("header", "pose", "speed_mps", "steering_rad")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POSE_FIELD_NUMBER: _ClassVar[int]
    SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    STEERING_RAD_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    pose: _common_pb2.Pose2
    speed_mps: float
    steering_rad: float
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., pose: _Optional[_Union[_common_pb2.Pose2, _Mapping]] = ..., speed_mps: _Optional[float] = ..., steering_rad: _Optional[float] = ...) -> None: ...

class PathPoint(_message.Message):
    __slots__ = ("pose", "speed_mps", "steering_rad", "time_s")
    POSE_FIELD_NUMBER: _ClassVar[int]
    SPEED_MPS_FIELD_NUMBER: _ClassVar[int]
    STEERING_RAD_FIELD_NUMBER: _ClassVar[int]
    TIME_S_FIELD_NUMBER: _ClassVar[int]
    pose: _common_pb2.Pose2
    speed_mps: float
    steering_rad: float
    time_s: float
    def __init__(self, pose: _Optional[_Union[_common_pb2.Pose2, _Mapping]] = ..., speed_mps: _Optional[float] = ..., steering_rad: _Optional[float] = ..., time_s: _Optional[float] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ("header", "points", "reaches_goal", "cost")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    REACHES_GOAL_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    points: _containers.RepeatedCompositeFieldContainer[PathPoint]
    reaches_goal: bool
    cost: float
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., points: _Optional[_Iterable[_Union[PathPoint, _Mapping]]] = ..., reaches_goal: _Optional[bool] = ..., cost: _Optional[float] = ...) -> None: ...

class PlannerStatus(_message.Message):
    __slots__ = ("header", "mode", "message")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    mode: DriverMode
    message: str
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., mode: _Optional[_Union[DriverMode, str]] = ..., message: _Optional[str] = ...) -> None: ...
