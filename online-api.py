# online API demo

import time, random
import grpc
import protos.hello_pb2
from protos.hello_pb2_grpc import HelloStub

def run():
    with grpc.insecure_channel('[2001:da8:ff:212::12:8]:50051') as channel:
        stub = HelloStub(channel)
        request = protos.hello_pb2.Request(data="Server")
        response = stub.hi(request)
        print("Greeter client received: ", response.message)

        ipList = []
        for ip in ipList:
            request = protos.hello_pb2.queryIP(ip)
            response = stub.query(request)
            for ipGeo in response.geoInfo:
                print(ipGeo)


if __name__ == '__main__':
    run()
