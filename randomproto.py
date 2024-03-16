import random
import string
import functools
from typing import Callable, Dict, Any, Type

from google.protobuf.descriptor import Descriptor, FieldDescriptor
from google.protobuf.message import Message


def _rand_float() -> float:
    return random.random() * 2 - 1


def _rand_int_factory(a: int, b: int) -> Callable[[], int]:
    def get_random_int() -> int:
        return random.randint(a, b - 1)
    return get_random_int


def _rand_signed_int_factory(bits=32) -> Callable[[], int]:
    max_abs = 1 << (bits // 2)
    return _rand_int_factory(a=-max_abs, b=max_abs)


def _rand_unsigned_int_factory(bits=32) -> Callable[[], int]:
    return _rand_int_factory(a=0, b=(1 << bits))


def _rand_bool() -> bool:
    return random.randint(0, 1) == 1


def _rand_str() -> str:
    n = random.randint(1, 20)
    return ''.join(random.choice(string.printable) for _ in range(n))


def _rand_bytes() -> bytes:
    s = _rand_str()
    return s.encode('utf-8')


_FIELD_RANDOM_GENERATOR: Dict[int, Callable[[], Any]] = {
    FieldDescriptor.TYPE_DOUBLE: _rand_float,
    FieldDescriptor.TYPE_FLOAT: _rand_float,
    FieldDescriptor.TYPE_INT32: _rand_signed_int_factory(32),
    FieldDescriptor.TYPE_INT64: _rand_signed_int_factory(64),
    FieldDescriptor.TYPE_UINT32: _rand_unsigned_int_factory(32),
    FieldDescriptor.TYPE_UINT64: _rand_unsigned_int_factory(64),
    FieldDescriptor.TYPE_SINT32: _rand_signed_int_factory(32),
    FieldDescriptor.TYPE_SINT64: _rand_signed_int_factory(64),
    FieldDescriptor.TYPE_FIXED32: _rand_unsigned_int_factory(32),
    FieldDescriptor.TYPE_FIXED64: _rand_unsigned_int_factory(64),
    FieldDescriptor.TYPE_SFIXED32: _rand_signed_int_factory(32),
    FieldDescriptor.TYPE_SFIXED64: _rand_signed_int_factory(64),
    FieldDescriptor.TYPE_BOOL: _rand_bool,
    FieldDescriptor.TYPE_STRING: _rand_str,
    FieldDescriptor.TYPE_BYTES: _rand_bytes,
}


def _fill_random(msg: Message, desc: Descriptor):
    for field in desc.fields:
        is_message = field.type == FieldDescriptor.TYPE_MESSAGE
        is_repeated = field.label == FieldDescriptor.LABEL_REPEATED

        if is_message:
            msg_field = getattr(msg, field.name)
            if is_repeated:
                num = random.randint(1, 5)
                options = field.message_type.GetOptions()
                if options.map_entry:
                    # map entry
                    key_type_descriptor = field.message_type.fields[0]
                    value_type_descriptor = field.message_type.fields[1]
                    assert key_type_descriptor.name == 'key' and value_type_descriptor.name == 'value'
                    key_type_id = key_type_descriptor.type
                    value_type_id = value_type_descriptor.type

                    random_key_gen = _FIELD_RANDOM_GENERATOR[key_type_id]
                    random_value_gen = _FIELD_RANDOM_GENERATOR.get(value_type_id, None)

                    for _ in range(num):
                        random_key = random_key_gen()
                        if random_value_gen:
                            msg_field[random_key] = random_value_gen()
                        else:
                            el = msg_field[random_key]
                            _fill_random(el, value_type_descriptor.message_type)
                else:
                    for _ in range(num):
                        element = msg_field.add()
                        _fill_random(element, field.message_type)
            else:
                _fill_random(msg_field, field.message_type)
        else:
            if field.type == FieldDescriptor.TYPE_ENUM:
                enum_values = [x.number for x in field.enum_type.values]
                generator = functools.partial(random.choice, enum_values)
            else:
                generator = _FIELD_RANDOM_GENERATOR.get(field.type)
            if is_repeated:
                num = random.randint(1, 5)
                msg_field = getattr(msg, field.name)
                for _ in range(num):
                    msg_field.append(generator())
            else:
                setattr(msg, field.name, generator())


def randproto(proto_class: Type[Message]) -> Message:
    """Generate random protobuf message object.

    Args:
        proto_class: The protobuf message class.

    Returns:
        google.protobuf.message: Generated massage object.

    """
    msg = proto_class()
    _fill_random(msg, proto_class.DESCRIPTOR)
    return msg
