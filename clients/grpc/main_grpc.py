import grpc
import generated.music_streaming_service_pb2 as mss_pb2
import generated.music_streaming_service_pb2_grpc as mss_pb2_grpc

from typing import Dict, Union


class MusicStreamingGRPCClient:

    def __init__(self, host="localhost", port=9090):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = mss_pb2_grpc.MusicStreamingServiceStub(self.channel)

    def get_users(self):
        try:
            response = self.stub.GetUsers(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def get_songs(self):
        try:
            response = self.stub.GetSongs(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def get_playlists(self):
        try:
            response = self.stub.GetPlaylists(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_user(self, user: Dict[str, Union[str, int]]):
        try:
            response = self.stub.CreateUser(request=mss_pb2.CreateUserRequest(**user))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_song(self, song: Dict[str, str]):
        try:
            response = self.stub.CreateSong(request=mss_pb2.CreateSongRequest(**song))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_playlist(self, playlist: Dict[str, Union[str, int, list]]):
        try:
            response = self.stub.CreatePlaylist(
                request=mss_pb2.CreatePlaylistRequest(**playlist)
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_user(self, user: Dict[str, Union[str, int]]):
        try:
            response = self.stub.UpdateUser(request=mss_pb2.UpdateUserRequest(**user))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_song(self, song: Dict[str, str]):
        try:
            response = self.stub.UpdateSong(request=mss_pb2.UpdateSongRequest(**song))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_playlist(self, playlist: Dict[str, Union[str, int, list]]):
        try:
            response = self.stub.UpdatePlaylist(
                request=mss_pb2.UpdatePlaylistRequest(**playlist)
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_user(self, user_id: int):
        try:
            response = self.stub.DeleteUser(request=mss_pb2.IdRequest(id=user_id))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_song(self, song_id: int):
        try:
            response = self.stub.DeleteSong(request=mss_pb2.IdRequest(id=song_id))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_playlist(self, playlist_id: int):
        try:
            response = self.stub.DeletePlaylist(
                request=mss_pb2.IdRequest(id=playlist_id)
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def __del__(self):
        if self.channel:
            self.channel.close()

    def close(self):
        if self.channel:
            self.channel.close()
            self.channel = None


if __name__ == "__main__":
    import random as r

    def random_user_id():
        return r.randint(0, 19)

    def random_playlist_id():
        return r.randint(0, 29)

    def random_song_id():
        return r.randint(0, 99)

    client = MusicStreamingGRPCClient()
    print(client.get_users())
    client.close()
