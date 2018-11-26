import grpc

from service_pb2 import ModelInput
from service_pb2_grpc import ModelStub


class GrpcClient(object):
    def __init__(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = ModelStub(self.channel)

    def get_response(self, features):
        input = ModelInput(features=features)
        return self.stub.Forward(request=input)

def main():
    features = [17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]
    client = GrpcClient(url="localhost:8080")
    response = client.get_response(features=features)
    print("label={0}, probability={1:0.2f}%".format(response.label, 100*response.probability))


if __name__ == "__main__":
    main()
