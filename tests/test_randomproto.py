"""Test randomproto."""

import pytest

import randomproto
import tests.proto2.example2_pb2 as pb2_example2
import tests.proto3.example1_pb2 as pb3_example1
import tests.proto3.example2_pb2 as pb3_example2


@pytest.mark.parametrize('proto_class', [pb3_example1.TypeMessage], ids=['pb3_type_message'])
def test_randproto(proto_class):
    msg = randomproto.randproto(proto_class)
    assert len(str(msg)) > 0
    assert msg.float_field != 0.0
    assert len(msg.string_field) > 0
    assert len(msg.int32_repeated) > 0
    assert len(msg.msg_repeated) > 0
    assert len(msg.map_field) > 0


@pytest.mark.parametrize('proto_class', [pb2_example2.TypeMessage,
                                         pb2_example2.LabeledMessage,
                                         pb2_example2.DefaultMessage,
                                         pb3_example2.TypeMessage,
                                         pb3_example2.LabeledMessage],
                         ids=['pb2_type_message', 'pb2_labeled_message', 'pb2_default_message',
                              'pb3_type_message', 'pb3_labeled_message'])
def test_randproto_simple(proto_class):
    msg = randomproto.randproto(proto_class)
