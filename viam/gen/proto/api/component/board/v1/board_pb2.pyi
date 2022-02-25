"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class StatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___StatusRequest = StatusRequest

class StatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STATUS_FIELD_NUMBER: builtins.int

    @property
    def status(self) -> proto.api.common.v1.common_pb2.BoardStatus:
        ...

    def __init__(self, *, status: typing.Optional[proto.api.common.v1.common_pb2.BoardStatus]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['status', b'status']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['status', b'status']) -> None:
        ...
global___StatusResponse = StatusResponse

class SetGPIORequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    pin: typing.Text = ...
    high: builtins.bool = ...

    def __init__(self, *, name: typing.Text=..., pin: typing.Text=..., high: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['high', b'high', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetGPIORequest = SetGPIORequest

class SetGPIOResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___SetGPIOResponse = SetGPIOResponse

class GetGPIORequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    pin: typing.Text = ...

    def __init__(self, *, name: typing.Text=..., pin: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'pin', b'pin']) -> None:
        ...
global___GetGPIORequest = GetGPIORequest

class GetGPIOResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HIGH_FIELD_NUMBER: builtins.int
    high: builtins.bool = ...

    def __init__(self, *, high: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['high', b'high']) -> None:
        ...
global___GetGPIOResponse = GetGPIOResponse

class SetPWMRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    DUTY_CYCLE_PCT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    pin: typing.Text = ...
    duty_cycle_pct: builtins.float = ...
    '0-1'

    def __init__(self, *, name: typing.Text=..., pin: typing.Text=..., duty_cycle_pct: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['duty_cycle_pct', b'duty_cycle_pct', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetPWMRequest = SetPWMRequest

class SetPWMResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___SetPWMResponse = SetPWMResponse

class SetPWMFrequencyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___SetPWMFrequencyResponse = SetPWMFrequencyResponse

class SetPWMFrequencyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    PIN_FIELD_NUMBER: builtins.int
    FREQUENCY_HZ_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    pin: typing.Text = ...
    frequency_hz: builtins.int = ...

    def __init__(self, *, name: typing.Text=..., pin: typing.Text=..., frequency_hz: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['frequency_hz', b'frequency_hz', 'name', b'name', 'pin', b'pin']) -> None:
        ...
global___SetPWMFrequencyRequest = SetPWMFrequencyRequest

class ReadAnalogReaderRequest(google.protobuf.message.Message):
    """Analog Reader

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOARD_NAME_FIELD_NUMBER: builtins.int
    ANALOG_READER_NAME_FIELD_NUMBER: builtins.int
    board_name: typing.Text = ...
    analog_reader_name: typing.Text = ...

    def __init__(self, *, board_name: typing.Text=..., analog_reader_name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['analog_reader_name', b'analog_reader_name', 'board_name', b'board_name']) -> None:
        ...
global___ReadAnalogReaderRequest = ReadAnalogReaderRequest

class ReadAnalogReaderResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int = ...

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___ReadAnalogReaderResponse = ReadAnalogReaderResponse

class GetDigitalInterruptValueRequest(google.protobuf.message.Message):
    """Digital Interrupt

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOARD_NAME_FIELD_NUMBER: builtins.int
    DIGITAL_INTERRUPT_NAME_FIELD_NUMBER: builtins.int
    board_name: typing.Text = ...
    digital_interrupt_name: typing.Text = ...

    def __init__(self, *, board_name: typing.Text=..., digital_interrupt_name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['board_name', b'board_name', 'digital_interrupt_name', b'digital_interrupt_name']) -> None:
        ...
global___GetDigitalInterruptValueRequest = GetDigitalInterruptValueRequest

class GetDigitalInterruptValueResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VALUE_FIELD_NUMBER: builtins.int
    value: builtins.int = ...

    def __init__(self, *, value: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['value', b'value']) -> None:
        ...
global___GetDigitalInterruptValueResponse = GetDigitalInterruptValueResponse