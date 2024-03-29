from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TypeMessage(_message.Message):
    __slots__ = ("double_field", "float_field", "int32_field", "int64_field", "uint32_field", "uint64_field", "sint32_field", "sint64_field", "fixed32_field", "fixed64_field", "sfixed32_field", "sfixed64_field", "bool_field", "string_field", "bytes_field", "enum_field", "msg_field", "optional_field", "oneof_field", "int32_repeated", "msg_repeated", "map_field")
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_INVALID: _ClassVar[TypeMessage.Enum]
        ENUM_ONE: _ClassVar[TypeMessage.Enum]
        ENUM_TWO: _ClassVar[TypeMessage.Enum]
    ENUM_INVALID: TypeMessage.Enum
    ENUM_ONE: TypeMessage.Enum
    ENUM_TWO: TypeMessage.Enum
    class NestedMessage(_message.Message):
        __slots__ = ("double_field", "string_field")
        DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
        double_field: float
        string_field: str
        def __init__(self, double_field: _Optional[float] = ..., string_field: _Optional[str] = ...) -> None: ...
    class MapFieldEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TypeMessage.NestedMessage
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TypeMessage.NestedMessage, _Mapping]] = ...) -> None: ...
    DOUBLE_FIELD_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_FIELD_NUMBER: _ClassVar[int]
    SFIXED32_FIELD_FIELD_NUMBER: _ClassVar[int]
    SFIXED64_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT32_REPEATED_FIELD_NUMBER: _ClassVar[int]
    MSG_REPEATED_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_FIELD_NUMBER: _ClassVar[int]
    double_field: float
    float_field: float
    int32_field: int
    int64_field: int
    uint32_field: int
    uint64_field: int
    sint32_field: int
    sint64_field: int
    fixed32_field: int
    fixed64_field: int
    sfixed32_field: int
    sfixed64_field: int
    bool_field: bool
    string_field: str
    bytes_field: bytes
    enum_field: TypeMessage.Enum
    msg_field: TypeMessage.NestedMessage
    optional_field: int
    oneof_field: int
    int32_repeated: _containers.RepeatedScalarFieldContainer[int]
    msg_repeated: _containers.RepeatedCompositeFieldContainer[TypeMessage.NestedMessage]
    map_field: _containers.MessageMap[int, TypeMessage.NestedMessage]
    def __init__(self, double_field: _Optional[float] = ..., float_field: _Optional[float] = ..., int32_field: _Optional[int] = ..., int64_field: _Optional[int] = ..., uint32_field: _Optional[int] = ..., uint64_field: _Optional[int] = ..., sint32_field: _Optional[int] = ..., sint64_field: _Optional[int] = ..., fixed32_field: _Optional[int] = ..., fixed64_field: _Optional[int] = ..., sfixed32_field: _Optional[int] = ..., sfixed64_field: _Optional[int] = ..., bool_field: bool = ..., string_field: _Optional[str] = ..., bytes_field: _Optional[bytes] = ..., enum_field: _Optional[_Union[TypeMessage.Enum, str]] = ..., msg_field: _Optional[_Union[TypeMessage.NestedMessage, _Mapping]] = ..., optional_field: _Optional[int] = ..., oneof_field: _Optional[int] = ..., int32_repeated: _Optional[_Iterable[int]] = ..., msg_repeated: _Optional[_Iterable[_Union[TypeMessage.NestedMessage, _Mapping]]] = ..., map_field: _Optional[_Mapping[int, TypeMessage.NestedMessage]] = ...) -> None: ...
