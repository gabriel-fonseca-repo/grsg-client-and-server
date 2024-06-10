import requests


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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code

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
        ).status_code


if __name__ == "__main__":
    import random as r
    from faker import Faker

    fake = Faker()

    def random_user_id():
        return r.randint(0, 19)

    def random_playlist_id():
        return r.randint(0, 29)

    def random_song_id():
        return r.randint(0, 99)

    client = MusicStreamingSOAPClient()

    metodos = {
        client.get_users: {},
        client.get_songs: {},
        client.get_playlists: {},
        client.create_user: {"name": fake.name(), "age": r.randint(18, 99)},
        client.create_song: {"name": fake.catch_phrase(), "artist": fake.name()},
        client.create_playlist: {
            "name": fake.word(),
            "user_id": r.randint(0, 19),
            "songs": [r.randint(0, 99) for _ in range(r.randint(5, 15))],
        },
        client.update_user: {
            "id": random_user_id(),
            "name": fake.name(),
            "age": r.randint(18, 99),
        },
        client.update_song: {
            "id": random_song_id(),
            "name": fake.catch_phrase(),
            "artist": fake.name(),
        },
        client.update_playlist: {
            "id": random_playlist_id(),
            "name": fake.word(),
            "user_id": random_user_id(),
            "songs": [r.randint(0, 99) for _ in range(r.randint(5, 15))],
        },
        client.delete_user: {"id": random_user_id()},
        client.delete_song: {"id": random_song_id()},
        client.delete_playlist: {"id": random_playlist_id()},
    }

    for metodo, params in metodos.items():
        print(metodo(**params))
