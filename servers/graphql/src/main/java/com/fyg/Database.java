package com.fyg;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fyg.data.FygDataFile;
import com.fyg.data.FygPlaylist;
import com.fyg.data.FygSong;
import com.fyg.data.FygUser;
import jakarta.enterprise.context.ApplicationScoped;

import java.io.InputStream;
import java.util.List;

@ApplicationScoped
public class Database {

  private final List<FygUser> fygUsers;

  private final List<FygSong> fygSongs;

  private final List<FygPlaylist> fygPlaylists;

  public Database() {
    ObjectMapper objectMapper = new ObjectMapper();

    try {
      InputStream dataStream = getClass().getResourceAsStream("/data.json");
      FygDataFile fygData = objectMapper.readValue(dataStream, FygDataFile.class);

      this.fygUsers = fygData.getUsuarios();
      this.fygSongs = fygData.getMusicas();
      this.fygPlaylists = fygData.getPlaylists();

      if (dataStream != null) {
        dataStream.close();
      }
    } catch (Exception e) {
      throw new RuntimeException("Falha ao carregar dados do banco de dados. (Arquivo data.json). Erro: " + e.getMessage());
    }
  }

  public List<FygUser> getUsers() {
    return fygUsers;
  }

  public List<FygSong> getSongs() {
    return fygSongs;
  }

  public List<FygPlaylist> getPlaylists() {
    return fygPlaylists;
  }

}

