IMAGE_NAME = python

CURRENT_DIR = $(shell pwd)

all: build run

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -v $(CURRENT_DIR):/usr/src/app  -it $(IMAGE_NAME) 

clean:
	docker image rm $(IMAGE_NAME)

.PHONY: build run
