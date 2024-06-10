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

    def list_all_users(self):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data="""
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllUsers/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        ).text

    def list_all_songs(self):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data="""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllSongs/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        ).text

    def list_all_playlists_by_user(self, user_id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllPlaylistsByUser>
                          <arg0>{user_id}</arg0>
                      </msc:listAllPlaylistsByUser>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        ).text

    def list_all_song_data_of_playlist(self, playlist_id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllSongDataOfPlaylist>
                          <arg0>{playlist_id}</arg0>
                      </msc:listAllSongDataOfPlaylist>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        ).text

    def list_all_playlists_with_song(self, song_id: int):
        return requests.request(
            "POST",
            self.url,
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllPlaylistsWithSong>
                          <arg0>{song_id}</arg0>
                      </msc:listAllPlaylistsWithSong>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        ).text


if __name__ == "__main__":
    import random as r

    def random_user_id():
        return r.randint(0, 19)

    def random_playlist_id():
        return r.randint(0, 29)

    def random_song_id():
        return r.randint(0, 99)

    client = MusicStreamingSOAPClient()
    print(client.list_all_users())
    print(client.list_all_songs())
    print(client.list_all_playlists_by_user(random_user_id()))
    print(client.list_all_song_data_of_playlist(random_playlist_id()))
    print(client.list_all_playlists_with_song(random_song_id()))
