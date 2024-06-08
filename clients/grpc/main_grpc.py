import grpc
import generated.music_streaming_service_pb2 as mss_pb2
import generated.music_streaming_service_pb2_grpc as mss_pb2_grpc


class MusicStreamingClient:

    def __init__(self, host="localhost", port=9090):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = mss_pb2_grpc.MusicStreamingServiceStub(self.channel)

    def list_all_users(self):
        try:
            response = self.stub.ListAllUsers(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def list_all_songs(self):
        try:
            response = self.stub.ListAllSongs(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def list_all_playlists_by_user(self, user_id):
        try:
            response = self.stub.ListAllPlaylistsByUser(
                request=mss_pb2.ListAllPlaylistsByUserRequest(userId=user_id),
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def list_all_song_data_of_playlist(self, playlist_id):
        try:
            response = self.stub.ListAllSongDataOfPlaylist(
                request=mss_pb2.ListAllSongDataOfPlaylistRequest(
                    playlistId=playlist_id
                ),
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def list_all_playlists_with_song(self, song_id):
        try:
            response = self.stub.ListAllPlaylistsWithSong(
                request=mss_pb2.ListAllPlaylistsWithSongRequest(songId=song_id),
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

    client = MusicStreamingClient()
    print(client.list_all_users())
    print(client.list_all_songs())
    print(client.list_all_playlists_by_user(random_user_id()))
    print(client.list_all_song_data_of_playlist(random_playlist_id()))
    print(client.list_all_playlists_with_song(random_song_id()))
    client.close()
