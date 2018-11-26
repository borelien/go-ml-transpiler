

# targets

protobuf_go:
	protoc -I proto service.proto --go_out=plugins=grpc:proto

protobuf_python:
	python -m grpc_tools.protoc -I proto --python_out=client/python --grpc_python_out=client/python service.proto

transpile:
	docker build -t transpiler/model -f Dockerfiles/model/Dockerfile.model .

api:
	docker build -t transpiler/server -f Dockerfiles/server/Dockerfile.server .

run:
	docker run -p 8080:8080 transpiler/server

_benchmarkmodel:
	docker build -t transpiler/benchmark/model -f Dockerfiles/server/Dockerfile.benchmark .

_benchmarkapi:
	docker-compose -f docker-compose.yml up --build -d
	docker-compose run client go test -bench=.
	docker-compose down


### make + start server

serving: transpile api run


### benchmark

benchmark_model: transpile api _benchmarkmodel
	docker run transpiler/benchmark/model

benchmark_api: transpile _benchmarkapi
