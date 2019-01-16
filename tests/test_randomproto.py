"""Test randomproto."""
import pytest

import randomproto
import example2_pb2
import example3_pb2


@pytest.mark.parametrize('proto',
                         [example2_pb2.TypeMessage,
                          example3_pb2.TypeMessage,
                          example2_pb2.LabeledMessage,
                          example3_pb2.LabeledMessage,
                          example2_pb2.DefaultMessage],
                         ids=['type-proto2', 'type-proto3',
                              'labeled-proto2', 'labeled-proto3',
                              'default-proto2'])
def test_randproto(proto):
    """Test ``randproto``."""
    randomproto.randproto(proto)
