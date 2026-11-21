from cev.interfaces.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RangeNode(_message.Message):
    __slots__ = ("x", "y", "z", "intensity", "range", "azimuth_centideg", "point_idx", "valid", "alpha", "beta")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_CENTIDEG_FIELD_NUMBER: _ClassVar[int]
    POINT_IDX_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    BETA_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    intensity: float
    range: float
    azimuth_centideg: int
    point_idx: int
    valid: bool
    alpha: int
    beta: int
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., intensity: _Optional[float] = ..., range: _Optional[float] = ..., azimuth_centideg: _Optional[int] = ..., point_idx: _Optional[int] = ..., valid: _Optional[bool] = ..., alpha: _Optional[int] = ..., beta: _Optional[int] = ...) -> None: ...

class RangeGraph(_message.Message):
    __slots__ = ("header", "num_rings", "num_cols", "azimuth_resolution_centideg", "nodes")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    NUM_RINGS_FIELD_NUMBER: _ClassVar[int]
    NUM_COLS_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_RESOLUTION_CENTIDEG_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    num_rings: int
    num_cols: int
    azimuth_resolution_centideg: int
    nodes: _containers.RepeatedCompositeFieldContainer[RangeNode]
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., num_rings: _Optional[int] = ..., num_cols: _Optional[int] = ..., azimuth_resolution_centideg: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[RangeNode, _Mapping]]] = ...) -> None: ...

class PointCloud(_message.Message):
    __slots__ = ("header", "width", "point_step", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    POINT_STEP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    width: int
    point_step: int
    data: bytes
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., width: _Optional[int] = ..., point_step: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class OccupancyGrid(_message.Message):
    __slots__ = ("header", "size_x", "size_y", "resolution_m", "origin_x", "origin_y", "data")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SIZE_X_FIELD_NUMBER: _ClassVar[int]
    SIZE_Y_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_M_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_X_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_Y_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    size_x: int
    size_y: int
    resolution_m: float
    origin_x: float
    origin_y: float
    data: bytes
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., size_x: _Optional[int] = ..., size_y: _Optional[int] = ..., resolution_m: _Optional[float] = ..., origin_x: _Optional[float] = ..., origin_y: _Optional[float] = ..., data: _Optional[bytes] = ...) -> None: ...

class Diff(_message.Message):
    __slots__ = ("mx", "my", "old", "new")
    MX_FIELD_NUMBER: _ClassVar[int]
    MY_FIELD_NUMBER: _ClassVar[int]
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    mx: int
    my: int
    old: int
    new: int
    def __init__(self, mx: _Optional[int] = ..., my: _Optional[int] = ..., old: _Optional[int] = ..., new: _Optional[int] = ...) -> None: ...

class OccupancyGridDiff(_message.Message):
    __slots__ = ("header", "diffs")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DIFFS_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    diffs: _containers.RepeatedCompositeFieldContainer[Diff]
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., diffs: _Optional[_Iterable[_Union[Diff, _Mapping]]] = ...) -> None: ...

class Transform(_message.Message):
    __slots__ = ("header", "translation", "rotation")
    HEADER_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    header: _common_pb2.Header
    translation: _common_pb2.Vector3
    rotation: _common_pb2.Quaternion
    def __init__(self, header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., translation: _Optional[_Union[_common_pb2.Vector3, _Mapping]] = ..., rotation: _Optional[_Union[_common_pb2.Quaternion, _Mapping]] = ...) -> None: ...
