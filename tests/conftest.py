import os

# Required to test both old (proto2 and proto3 < 4.0) and new (proto3 >= 4.0) compiled protobufs.
# Without that protobuf argues about Descriptors direct declarations.
# https://developers.google.com/protocol-buffers/docs/news/2022-05-06#python-updates
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
