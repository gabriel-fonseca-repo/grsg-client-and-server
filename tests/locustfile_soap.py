from locust import HttpUser, between, task
from random_data import random_user_id, random_playlist_id, random_song_id


class SoapUser(HttpUser):
    host = "http://localhost:8081"
    wait_time = between(5, 10)

    main_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/xml",
        "Host": "localhost:8081",
        "User-Agent": "python-requests/2.26.0",
    }

    @task
    def list_all_users(self):
        self.client.post(
            f"/soap/music",
            headers=self.main_headers,
            data="""
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllUsers/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    @task
    def list_all_songs(self):
        self.client.post(
            f"/soap/music",
            headers=self.main_headers,
            data="""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllSongs/>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    @task
    def list_all_playlists_by_user(self):
        self.client.post(
            f"/soap/music",
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllPlaylistsByUser>
                          <arg0>{random_user_id()}</arg0>
                      </msc:listAllPlaylistsByUser>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    @task
    def list_all_song_data_of_playlist(self):
        self.client.post(
            f"/soap/music",
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllSongDataOfPlaylist>
                          <arg0>{random_playlist_id()}</arg0>
                      </msc:listAllSongDataOfPlaylist>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )

    @task
    def list_all_playlists_with_song(self):
        self.client.post(
            f"/soap/music",
            headers=self.main_headers,
            data=f"""
              <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:msc="http://musicstreaming.com">
                  <soapenv:Body>
                      <msc:listAllPlaylistsWithSong>
                          <arg0>{random_song_id()}</arg0>
                      </msc:listAllPlaylistsWithSong>
                  </soapenv:Body>
              </soapenv:Envelope>
            """.strip(),
        )
