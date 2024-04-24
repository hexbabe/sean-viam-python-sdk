"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
from .... import common
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MoveStraightRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DISTANCE_MM_FIELD_NUMBER: builtins.int
    MM_PER_SEC_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a base'
    distance_mm: builtins.int
    'Desired travel distance in millimeters'
    mm_per_sec: builtins.float
    'Desired travel velocity in millimeters/second'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., distance_mm: builtins.int=..., mm_per_sec: builtins.float=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['distance_mm', b'distance_mm', 'extra', b'extra', 'mm_per_sec', b'mm_per_sec', 'name', b'name']) -> None:
        ...
global___MoveStraightRequest = MoveStraightRequest

@typing.final
class MoveStraightResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___MoveStraightResponse = MoveStraightResponse

@typing.final
class SpinRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ANGLE_DEG_FIELD_NUMBER: builtins.int
    DEGS_PER_SEC_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a base'
    angle_deg: builtins.float
    'Desired angle'
    degs_per_sec: builtins.float
    'Desired angular velocity'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., angle_deg: builtins.float=..., degs_per_sec: builtins.float=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['angle_deg', b'angle_deg', 'degs_per_sec', b'degs_per_sec', 'extra', b'extra', 'name', b'name']) -> None:
        ...
global___SpinRequest = SpinRequest

@typing.final
class SpinResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SpinResponse = SpinResponse

@typing.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a base'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___StopRequest = StopRequest

@typing.final
class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopResponse = StopResponse

@typing.final
class SetPowerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LINEAR_FIELD_NUMBER: builtins.int
    ANGULAR_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a base'

    @property
    def linear(self) -> common.v1.common_pb2.Vector3:
        """Desired linear power percentage as -1 -> 1"""

    @property
    def angular(self) -> common.v1.common_pb2.Vector3:
        """Desired angular power percentage % as -1 -> 1"""

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., linear: common.v1.common_pb2.Vector3 | None=..., angular: common.v1.common_pb2.Vector3 | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['angular', b'angular', 'extra', b'extra', 'linear', b'linear']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['angular', b'angular', 'extra', b'extra', 'linear', b'linear', 'name', b'name']) -> None:
        ...
global___SetPowerRequest = SetPowerRequest

@typing.final
class SetPowerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetPowerResponse = SetPowerResponse

@typing.final
class SetVelocityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LINEAR_FIELD_NUMBER: builtins.int
    ANGULAR_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of a base'

    @property
    def linear(self) -> common.v1.common_pb2.Vector3:
        """Desired linear velocity in mm per second"""

    @property
    def angular(self) -> common.v1.common_pb2.Vector3:
        """Desired angular velocity in degrees per second"""

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., linear: common.v1.common_pb2.Vector3 | None=..., angular: common.v1.common_pb2.Vector3 | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['angular', b'angular', 'extra', b'extra', 'linear', b'linear']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['angular', b'angular', 'extra', b'extra', 'linear', b'linear', 'name', b'name']) -> None:
        ...
global___SetVelocityRequest = SetVelocityRequest

@typing.final
class SetVelocityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetVelocityResponse = SetVelocityResponse

@typing.final
class IsMovingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name']) -> None:
        ...
global___IsMovingRequest = IsMovingRequest

@typing.final
class IsMovingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_MOVING_FIELD_NUMBER: builtins.int
    is_moving: builtins.bool

    def __init__(self, *, is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['is_moving', b'is_moving']) -> None:
        ...
global___IsMovingResponse = IsMovingResponse

@typing.final
class GetPropertiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of the base'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPropertiesRequest = GetPropertiesRequest

@typing.final
class GetPropertiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WIDTH_METERS_FIELD_NUMBER: builtins.int
    TURNING_RADIUS_METERS_FIELD_NUMBER: builtins.int
    WHEEL_CIRCUMFERENCE_METERS_FIELD_NUMBER: builtins.int
    width_meters: builtins.float
    turning_radius_meters: builtins.float
    wheel_circumference_meters: builtins.float

    def __init__(self, *, width_meters: builtins.float=..., turning_radius_meters: builtins.float=..., wheel_circumference_meters: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['turning_radius_meters', b'turning_radius_meters', 'wheel_circumference_meters', b'wheel_circumference_meters', 'width_meters', b'width_meters']) -> None:
        ...
global___GetPropertiesResponse = GetPropertiesResponse