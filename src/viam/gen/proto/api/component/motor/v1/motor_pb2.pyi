"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class SetPowerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    POWER_PCT_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'
    power_pct: builtins.float
    "Percentage of motor's power, between -1 and 1"

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., power_pct: builtins.float=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'power_pct', b'power_pct']) -> None:
        ...
global___SetPowerRequest = SetPowerRequest

class SetPowerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetPowerResponse = SetPowerResponse

class GoForRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    RPM_FIELD_NUMBER: builtins.int
    REVOLUTIONS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'
    rpm: builtins.float
    'Speed of motor travel in rotations per minute'
    revolutions: builtins.float
    "Number of revolutions relative to motor's start position"

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., rpm: builtins.float=..., revolutions: builtins.float=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'revolutions', b'revolutions', 'rpm', b'rpm']) -> None:
        ...
global___GoForRequest = GoForRequest

class GoForResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___GoForResponse = GoForResponse

class GoToRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    RPM_FIELD_NUMBER: builtins.int
    POSITION_REVOLUTIONS_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'
    rpm: builtins.float
    'Speed of motor travel in rotations per minute'
    position_revolutions: builtins.float
    "Number of revolutions relative to motor's home home/zero"

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., rpm: builtins.float=..., position_revolutions: builtins.float=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'position_revolutions', b'position_revolutions', 'rpm', b'rpm']) -> None:
        ...
global___GoToRequest = GoToRequest

class GoToResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___GoToResponse = GoToResponse

class ResetZeroPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'
    offset: builtins.float
    'Motor position'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., offset: builtins.float=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name', 'offset', b'offset']) -> None:
        ...
global___ResetZeroPositionRequest = ResetZeroPositionRequest

class ResetZeroPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ResetZeroPositionResponse = ResetZeroPositionResponse

class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPositionRequest = GetPositionRequest

class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSITION_FIELD_NUMBER: builtins.int
    position: builtins.float
    'Current position of the motor relative to its home'

    def __init__(self, *, position: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['position', b'position']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___StopRequest = StopRequest

class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopResponse = StopResponse

class IsPoweredRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___IsPoweredRequest = IsPoweredRequest

class IsPoweredResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_ON_FIELD_NUMBER: builtins.int
    is_on: builtins.bool
    'Returns true if the motor is on'

    def __init__(self, *, is_on: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['is_on', b'is_on']) -> None:
        ...
global___IsPoweredResponse = IsPoweredResponse

class GetFeaturesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a motor'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""
        pass

    def __init__(self, *, name: typing.Text=..., extra: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetFeaturesRequest = GetFeaturesRequest

class GetFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    POSITION_REPORTING_FIELD_NUMBER: builtins.int
    position_reporting: builtins.bool
    'Returns true if the motor supports reporting its position'

    def __init__(self, *, position_reporting: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['position_reporting', b'position_reporting']) -> None:
        ...
global___GetFeaturesResponse = GetFeaturesResponse

class Status(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IS_POWERED_FIELD_NUMBER: builtins.int
    POSITION_REPORTING_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    IS_MOVING_FIELD_NUMBER: builtins.int
    is_powered: builtins.bool
    'Returns true if the motor is powered'
    position_reporting: builtins.bool
    'Returns true if the motor has position support'
    position: builtins.float
    'Returns current position of the motor relative to its home'
    is_moving: builtins.bool
    'Returns true if the motor is moving'

    def __init__(self, *, is_powered: builtins.bool=..., position_reporting: builtins.bool=..., position: builtins.float=..., is_moving: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['is_moving', b'is_moving', 'is_powered', b'is_powered', 'position', b'position', 'position_reporting', b'position_reporting']) -> None:
        ...
global___Status = Status