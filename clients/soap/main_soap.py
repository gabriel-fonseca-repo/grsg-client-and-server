import requests
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


class MusicStreamingSOAPClient:
    url = "http://localhost:8081/soap/music"

    main_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/xml",
        "Host": "localhost:8081",
        "User-Agent": "python-requests/2.26.0",
    }

    def join_tag_values(self, tag: str, values: list[str]):
        return "".join([f"<{tag}>{value}</{tag}>" for value in values])

    def get_users(self):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data="""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:getUsers/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def get_songs(self):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data="""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:getSongs/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def get_playlists(self):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data="""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:getPlaylists/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def create_user(self, name: str, age: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:createUser>
                          <arg0>
                              <name>{name}</name>
                              <age>{age}</age>
                          </arg0>
                      </msc:createUser>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def create_song(self, name: str, artist: str):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:createSong>
                          <arg0>
                              <name>{name}</name>
                              <artist>{artist}</artist>
                          </arg0>
                      </msc:createSong>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def create_playlist(self, name: str, user_id: int, songs: list[int]):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:createPlaylist>
                          <arg0>
                              <name>{name}</name>
                              <userId>{user_id}</userId>
                              {self.join_tag_values("songs", songs)}
                          </arg0>
                      </msc:createPlaylist>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def update_user(self, id: int, name: str, age: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:updateUser>
                          <arg0>
                              <id>{id}</id>
                              <name>{name}</name>
                              <age>{age}</age>
                          </arg0>
                      </msc:updateUser>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def update_song(self, id: int, name: str, artist: str):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:updateSong>
                          <arg0>
                              <id>{id}</id>
                              <name>{name}</name>
                              <artist>{artist}</artist>
                          </arg0>
                      </msc:updateSong>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def update_playlist(self, id: int, name: str, user_id: int, songs: list[int]):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:updatePlaylist>
                          <arg0>
                              <id>{id}</id>
                              <name>{name}</name>
                              <userId>{user_id}</userId>
                              {self.join_tag_values("songs", songs)}
                          </arg0>
                      </msc:updatePlaylist>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def delete_user(self, id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:deleteUser>
                          <arg0>{id}</arg0>
                      </msc:deleteUser>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def delete_song(self, id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:deleteSong>
                          <arg0>{id}</arg0>
                      </msc:deleteSong>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    def delete_playlist(self, id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:deletePlaylist>
                          <arg0>{id}</arg0>
                      </msc:deletePlaylist>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )


fake = Faker()

client = MusicStreamingSOAPClient()


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
            "user_id": random_user_id(),
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
            "user_id": random_user_id(),
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
        _ = method(**params)
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
