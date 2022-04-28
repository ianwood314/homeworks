NAME ?= ianwood314
VER="1.1"

all: build run pull

build:
	docker build -t ${NAME}/meteorite-landings-data:${VER} .

run:
	docker run --name "meteorite-landings-data" -d -p 5038:5000 ${NAME}/meteorite-landings-data:${VER}

redis:
	docker run -d -p 6438:6379 -v $(pwd)/data:/data:rw --name=ianwood-redis redis:6 --save 1 1

pull:
	docker pull ${NAME}/meteorite-landings-data:${VER}

push:
	docker push ${NAME}/meteorite-landings-data:${VER}

clean:
	docker ps -a | grep ianwood
