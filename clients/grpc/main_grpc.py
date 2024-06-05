import grpc
import generated.music_streaming_service_pb2 as mss_pb2
import generated.music_streaming_service_pb2_grpc as mss_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:9090") as channel:
        stub = mss_pb2_grpc.MusicStreamingServiceStub(channel)
        response = stub.ListAllUsers(request=mss_pb2.EmptyRequest())
        print("Resposta do servidor:", response)


if __name__ == "__main__":
    run()
