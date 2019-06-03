PROTOC_IMAGE = znly/protoc:0.4.0
UID := $(shell id -u)
GID := $(shell id -g)

.PHONY: all
all: proto2 proto3

.PHONY: proto2
proto2:
	docker pull $(PROTOC_IMAGE)
	docker run --rm -t \
		--user $(UID):$(GID) \
		-v $(shell pwd):/proto \
		-w /proto \
		$(PROTOC_IMAGE) \
		--python_out=. -I. example2.proto

.PHONY: proto3
proto3:
	docker pull $(PROTOC_IMAGE)
	docker run --rm -t \
		--user $(UID):$(GID) \
		-v $(shell pwd):/proto \
		-w /proto \
		$(PROTOC_IMAGE) \
		--python_out=. -I. example3.proto

.PHONY: clean
clean:
	rm *_pb2.py
