# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example3.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example3.proto',
  package='example3',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x65xample3.proto\x12\x08\x65xample3\"\x9c\x04\n\x0bTypeMessage\x12\x14\n\x0c\x64ouble_field\x18\x01 \x01(\x01\x12\x13\n\x0b\x66loat_field\x18\x02 \x01(\x02\x12\x13\n\x0bint32_field\x18\x03 \x01(\x05\x12\x13\n\x0bint64_field\x18\x04 \x01(\x03\x12\x14\n\x0cuint32_field\x18\x05 \x01(\r\x12\x14\n\x0cuint64_field\x18\x06 \x01(\x04\x12\x14\n\x0csint32_field\x18\x07 \x01(\x11\x12\x14\n\x0csint64_field\x18\x08 \x01(\x12\x12\x15\n\rfixed32_field\x18\t \x01(\x07\x12\x15\n\rfixed64_field\x18\n \x01(\x06\x12\x16\n\x0esfixed32_field\x18\x0b \x01(\x0f\x12\x16\n\x0esfixed64_field\x18\x0c \x01(\x10\x12\x12\n\nbool_field\x18\r \x01(\x08\x12\x14\n\x0cstring_field\x18\x0e \x01(\t\x12\x13\n\x0b\x62ytes_field\x18\x0f \x01(\x0c\x12.\n\nenum_field\x18\x10 \x01(\x0e\x32\x1a.example3.TypeMessage.Enum\x12\x36\n\tmsg_field\x18\x11 \x01(\x0b\x32#.example3.TypeMessage.NestedMessage\x1a%\n\rNestedMessage\x12\x14\n\x0c\x64ouble_field\x18\x01 \x01(\x01\"4\n\x04\x45num\x12\x10\n\x0c\x45NUM_INVALID\x10\x00\x12\x0c\n\x08\x45NUM_ONE\x10\x01\x12\x0c\n\x08\x45NUM_TWO\x10\x02\"\x87\x03\n\x0eLabeledMessage\x12\x17\n\x0foptional_scalar\x18\x04 \x01(\x01\x12\x34\n\roptional_enum\x18\x05 \x01(\x0e\x32\x1d.example3.LabeledMessage.Enum\x12<\n\x0coptional_msg\x18\x06 \x01(\x0b\x32&.example3.LabeledMessage.NestedMessage\x12\x17\n\x0frepeated_scalar\x18\x07 \x03(\x01\x12\x34\n\rrepeated_enum\x18\x08 \x03(\x0e\x32\x1d.example3.LabeledMessage.Enum\x12<\n\x0crepeated_msg\x18\t \x03(\x0b\x32&.example3.LabeledMessage.NestedMessage\x1a%\n\rNestedMessage\x12\x14\n\x0c\x64ouble_field\x18\x01 \x01(\x01\"4\n\x04\x45num\x12\x10\n\x0c\x45NUM_INVALID\x10\x00\x12\x0c\n\x08\x45NUM_ONE\x10\x01\x12\x0c\n\x08\x45NUM_TWO\x10\x02\x62\x06proto3')
)



_TYPEMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='example3.TypeMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUM_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM_ONE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM_TWO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=517,
  serialized_end=569,
)
_sym_db.RegisterEnumDescriptor(_TYPEMESSAGE_ENUM)

_LABELEDMESSAGE_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='example3.LabeledMessage.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUM_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM_ONE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENUM_TWO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=517,
  serialized_end=569,
)
_sym_db.RegisterEnumDescriptor(_LABELEDMESSAGE_ENUM)


_TYPEMESSAGE_NESTEDMESSAGE = _descriptor.Descriptor(
  name='NestedMessage',
  full_name='example3.TypeMessage.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_field', full_name='example3.TypeMessage.NestedMessage.double_field', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=515,
)

_TYPEMESSAGE = _descriptor.Descriptor(
  name='TypeMessage',
  full_name='example3.TypeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_field', full_name='example3.TypeMessage.double_field', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_field', full_name='example3.TypeMessage.float_field', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int32_field', full_name='example3.TypeMessage.int32_field', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_field', full_name='example3.TypeMessage.int64_field', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint32_field', full_name='example3.TypeMessage.uint32_field', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uint64_field', full_name='example3.TypeMessage.uint64_field', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint32_field', full_name='example3.TypeMessage.sint32_field', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sint64_field', full_name='example3.TypeMessage.sint64_field', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed32_field', full_name='example3.TypeMessage.fixed32_field', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed64_field', full_name='example3.TypeMessage.fixed64_field', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sfixed32_field', full_name='example3.TypeMessage.sfixed32_field', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sfixed64_field', full_name='example3.TypeMessage.sfixed64_field', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_field', full_name='example3.TypeMessage.bool_field', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_field', full_name='example3.TypeMessage.string_field', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_field', full_name='example3.TypeMessage.bytes_field', index=14,
      number=15, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum_field', full_name='example3.TypeMessage.enum_field', index=15,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_field', full_name='example3.TypeMessage.msg_field', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TYPEMESSAGE_NESTEDMESSAGE, ],
  enum_types=[
    _TYPEMESSAGE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=569,
)


_LABELEDMESSAGE_NESTEDMESSAGE = _descriptor.Descriptor(
  name='NestedMessage',
  full_name='example3.LabeledMessage.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_field', full_name='example3.LabeledMessage.NestedMessage.double_field', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=515,
)

_LABELEDMESSAGE = _descriptor.Descriptor(
  name='LabeledMessage',
  full_name='example3.LabeledMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optional_scalar', full_name='example3.LabeledMessage.optional_scalar', index=0,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional_enum', full_name='example3.LabeledMessage.optional_enum', index=1,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional_msg', full_name='example3.LabeledMessage.optional_msg', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_scalar', full_name='example3.LabeledMessage.repeated_scalar', index=3,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_enum', full_name='example3.LabeledMessage.repeated_enum', index=4,
      number=8, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_msg', full_name='example3.LabeledMessage.repeated_msg', index=5,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LABELEDMESSAGE_NESTEDMESSAGE, ],
  enum_types=[
    _LABELEDMESSAGE_ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=963,
)

_TYPEMESSAGE_NESTEDMESSAGE.containing_type = _TYPEMESSAGE
_TYPEMESSAGE.fields_by_name['enum_field'].enum_type = _TYPEMESSAGE_ENUM
_TYPEMESSAGE.fields_by_name['msg_field'].message_type = _TYPEMESSAGE_NESTEDMESSAGE
_TYPEMESSAGE_ENUM.containing_type = _TYPEMESSAGE
_LABELEDMESSAGE_NESTEDMESSAGE.containing_type = _LABELEDMESSAGE
_LABELEDMESSAGE.fields_by_name['optional_enum'].enum_type = _LABELEDMESSAGE_ENUM
_LABELEDMESSAGE.fields_by_name['optional_msg'].message_type = _LABELEDMESSAGE_NESTEDMESSAGE
_LABELEDMESSAGE.fields_by_name['repeated_enum'].enum_type = _LABELEDMESSAGE_ENUM
_LABELEDMESSAGE.fields_by_name['repeated_msg'].message_type = _LABELEDMESSAGE_NESTEDMESSAGE
_LABELEDMESSAGE_ENUM.containing_type = _LABELEDMESSAGE
DESCRIPTOR.message_types_by_name['TypeMessage'] = _TYPEMESSAGE
DESCRIPTOR.message_types_by_name['LabeledMessage'] = _LABELEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TypeMessage = _reflection.GeneratedProtocolMessageType('TypeMessage', (_message.Message,), dict(

  NestedMessage = _reflection.GeneratedProtocolMessageType('NestedMessage', (_message.Message,), dict(
    DESCRIPTOR = _TYPEMESSAGE_NESTEDMESSAGE,
    __module__ = 'example3_pb2'
    # @@protoc_insertion_point(class_scope:example3.TypeMessage.NestedMessage)
    ))
  ,
  DESCRIPTOR = _TYPEMESSAGE,
  __module__ = 'example3_pb2'
  # @@protoc_insertion_point(class_scope:example3.TypeMessage)
  ))
_sym_db.RegisterMessage(TypeMessage)
_sym_db.RegisterMessage(TypeMessage.NestedMessage)

LabeledMessage = _reflection.GeneratedProtocolMessageType('LabeledMessage', (_message.Message,), dict(

  NestedMessage = _reflection.GeneratedProtocolMessageType('NestedMessage', (_message.Message,), dict(
    DESCRIPTOR = _LABELEDMESSAGE_NESTEDMESSAGE,
    __module__ = 'example3_pb2'
    # @@protoc_insertion_point(class_scope:example3.LabeledMessage.NestedMessage)
    ))
  ,
  DESCRIPTOR = _LABELEDMESSAGE,
  __module__ = 'example3_pb2'
  # @@protoc_insertion_point(class_scope:example3.LabeledMessage)
  ))
_sym_db.RegisterMessage(LabeledMessage)
_sym_db.RegisterMessage(LabeledMessage.NestedMessage)


# @@protoc_insertion_point(module_scope)