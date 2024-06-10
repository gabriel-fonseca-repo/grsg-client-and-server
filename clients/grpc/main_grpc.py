import grpc
import generated.music_streaming_service_pb2 as mss_pb2
import generated.music_streaming_service_pb2_grpc as mss_pb2_grpc
import random as r
from faker import Faker
import time
import csv

qtd_usuarios = 3000
qtd_musicas = 10000
qtd_playlists = 4000


def randomInt(min, max):
    return r.randint(min, max)


def random_songs():
    songs = []
    for i in range(0, randomInt(5, 15)):
        songs.append(randomInt(1, 100))
    return songs


def random_age():
    return randomInt(18, 99)


def random_user_id():
    return randomInt(0, qtd_usuarios - 1)


def random_song_id():
    return randomInt(0, qtd_musicas - 1)


def random_playlist_id():
    return randomInt(0, qtd_playlists - 1)


class MusicStreamingGRPCClient:

    def __init__(self, host="localhost", port=9090):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = mss_pb2_grpc.MusicStreamingServiceStub(self.channel)

    def get_users(self, params=None):
        try:
            response = self.stub.GetUsers(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def get_songs(self, params=None):
        try:
            response = self.stub.GetSongs(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def get_playlists(self, params=None):
        try:
            response = self.stub.GetPlaylists(request=mss_pb2.EmptyRequest())
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_user(self, user):
        try:
            response = self.stub.CreateUser(request=mss_pb2.CreateUserRequest(**user))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_song(self, song):
        try:
            response = self.stub.CreateSong(request=mss_pb2.CreateSongRequest(**song))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def create_playlist(self, playlist):
        try:
            response = self.stub.CreatePlaylist(
                request=mss_pb2.CreatePlaylistRequest(**playlist)
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_user(self, user):
        try:
            response = self.stub.UpdateUser(request=mss_pb2.UpdateUserRequest(**user))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_song(self, song):
        try:
            response = self.stub.UpdateSong(request=mss_pb2.UpdateSongRequest(**song))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def update_playlist(self, playlist):
        try:
            response = self.stub.UpdatePlaylist(
                request=mss_pb2.UpdatePlaylistRequest(**playlist)
            )
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_user(self, id):
        try:
            response = self.stub.DeleteUser(request=mss_pb2.IdRequest(**id))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_song(self, id):
        try:
            response = self.stub.DeleteSong(request=mss_pb2.IdRequest(**id))
            return response
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()}, {e.details()}")
            return None

    def delete_playlist(self, id):
        try:
            response = self.stub.DeletePlaylist(request=mss_pb2.IdRequest(**id))
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


fake = Faker()

client = MusicStreamingGRPCClient()


metodos = {
    "GetUsers": {
        "method": client.get_users,
        "params": lambda: {},
    },
    "GetSongs": {
        "method": client.get_songs,
        "params": lambda: {},
    },
    "GetPlaylists": {
        "method": client.get_playlists,
        "params": lambda: {},
    },
    "CreateUser": {
        "method": client.create_user,
        "params": lambda: {"name": fake.name(), "age": random_age()},
    },
    "CreateSong": {
        "method": client.create_song,
        "params": lambda: {"name": fake.catch_phrase(), "artist": fake.name()},
    },
    "CreatePlaylist": {
        "method": client.create_playlist,
        "params": lambda: {
            "name": fake.word(),
            "userId": random_user_id(),
            "songs": random_songs(),
        },
    },
    "UpdateUser": {
        "method": client.update_user,
        "params": lambda: {
            "id": random_user_id(),
            "name": fake.name(),
            "age": random_age(),
        },
    },
    "UpdateSong": {
        "method": client.update_song,
        "params": lambda: {
            "id": random_song_id(),
            "name": fake.catch_phrase(),
            "artist": fake.name(),
        },
    },
    "UpdatePlaylist": {
        "method": client.update_playlist,
        "params": lambda: {
            "id": random_playlist_id(),
            "name": fake.word(),
            "userId": random_user_id(),
            "songs": random_songs(),
        },
    },
    "DeleteUser": {
        "method": client.delete_user,
        "params": lambda: {"id": random_user_id()},
    },
    "DeleteSong": {
        "method": client.delete_song,
        "params": lambda: {"id": random_song_id()},
    },
    "DeletePlaylist": {
        "method": client.delete_playlist,
        "params": lambda: {"id": random_playlist_id()},
    },
}


def perform_action(method, params):
    start_time = time.time()
    try:
        _ = method(params)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        return elapsed_time, False
    except Exception as _:
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        return elapsed_time, True


def load_test(metodos, iterations=10):
    performance_data = {
        key: {
            "Action": key,
            "Total Requests": 0,
            "Failed Requests": 0,
            "Average Time (ms)": 0,
            "Total Time (ms)": 0,
        }
        for key in metodos
    }

    for _ in range(iterations):
        for action, metadata in metodos.items():
            elapsed_time, failed = perform_action(
                metadata["method"], metadata["params"]()
            )
            performance_data[action]["Total Requests"] += 1
            performance_data[action]["Total Time (ms)"] += elapsed_time
            if failed:
                performance_data[action]["Failed Requests"] += 1

    for data in performance_data.values():
        if data["Total Requests"] > 0:
            data["Average Time (ms)"] = data["Total Time (ms)"] / data["Total Requests"]

    return performance_data


def save_to_csv(performance_data, filename="data/out/performance_data_grpc.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Action",
                "Total Requests",
                "Failed Requests",
                "Average Time (ms)",
                "Total Time (ms)",
            ],
        )
        writer.writeheader()
        for data in performance_data.values():
            writer.writerow(data)


filename = "data/out/performance_data_grpc.csv"

performance_data = load_test(metodos, iterations=100)
save_to_csv(performance_data, filename)
print(f"Teste de carga concluído e dados exportados para {filename}")
