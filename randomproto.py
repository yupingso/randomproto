"""Random protobuf message generator."""
import random
import string
import functools

from google.protobuf.descriptor import FieldDescriptor


def _rand_float():
    return random.random() * 2 - 1


def _rand_int_factory(a=0, b=(1 << 128)):
    def get_random_int():
        """Get random int."""
        return random.randint(a, b - 1)
    return get_random_int


def _rand_signed_int_factory(bits=32):
    max_abs = 1 << (bits // 2)
    return _rand_int_factory(a=-max_abs, b=max_abs)


def _rand_unsigned_int_factory(bits=32):
    return _rand_int_factory(a=0, b=(1 << bits))


def _rand_bool():
    return random.randint(0, 1) == 1


def _rand_str():
    n = random.randint(0, 2)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(n))


def _rand_bytes():
    s = _rand_str()
    return s.encode('utf-8')


_FIELD_RANDOM_GENERATOR = {
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


def _fill_random(msg, desc):
    """Fill all fields of ``msg`` with random values."""
    for field in desc.fields:
        is_message = field.type == FieldDescriptor.TYPE_MESSAGE
        is_repeated = field.label == FieldDescriptor.LABEL_REPEATED
        if is_message:
            msg_field = getattr(msg, field.name)
            if is_repeated:
                num = random.randint(0, 2)
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
                num = random.randint(0, 2)
                msg_field = getattr(msg, field.name)
                for _ in range(num):
                    msg_field.append(generator())
            else:
                setattr(msg, field.name, generator())


def randproto(proto):
    """Generate random protobuf message object.

    Args:
        proto: The protobuf message class.

    Returns:
        google.protobuf.message: Generated massage object.

    """
    msg = proto()
    _fill_random(msg, proto.DESCRIPTOR)
    return msg
