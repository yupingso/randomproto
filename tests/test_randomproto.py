import pytest

import randomproto
from tests.proto3.example1_pb2 import TypeMessage


@pytest.mark.parametrize('proto_class', [TypeMessage], ids=['example1_pb2'])
def test_randproto(proto_class):
    msg = randomproto.randproto(proto_class)
    assert len(str(msg)) > 0
    assert msg.float_field != 0.0
    assert len(msg.string_field) > 0
    assert len(msg.int32_repeated) > 0
    assert len(msg.msg_repeated) > 0
    assert len(msg.map_field) > 0

