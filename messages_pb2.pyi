from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED: _ClassVar[StatusEnum]
    RECEIVED: _ClassVar[StatusEnum]
    RECORDED: _ClassVar[StatusEnum]
    ERROR_WHILE_RECORDING: _ClassVar[StatusEnum]
UNDEFINED: StatusEnum
RECEIVED: StatusEnum
RECORDED: StatusEnum
ERROR_WHILE_RECORDING: StatusEnum

class RequestData(_message.Message):
    __slots__ = ("page_name", "client_address", "request_body")
    PAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    page_name: str
    client_address: str
    request_body: str
    def __init__(self, page_name: _Optional[str] = ..., client_address: _Optional[str] = ..., request_body: _Optional[str] = ...) -> None: ...

class ResponseBody(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: StatusEnum
    def __init__(self, status: _Optional[_Union[StatusEnum, str]] = ...) -> None: ...
