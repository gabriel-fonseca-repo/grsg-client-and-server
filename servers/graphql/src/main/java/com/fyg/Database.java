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

  public Integer createUser(FygUser user) {
    if (user == null) {
      return -1;
    }
    if (user.getId() != null) {
      return -1;
    }
    user.setId(getUsers().size());
    getUsers().add(user);
    return user.getId();
  }

  public Integer createSong(FygSong song) {
    if (song == null) {
      return -1;
    }
    if (song.getId() != null) {
      return -1;
    }
    song.setId(getSongs().size());
    getSongs().add(song);
    return song.getId();
  }

  public Integer createPlaylist(FygPlaylist playlist) {
    if (playlist == null) {
      return -1;
    }
    if (playlist.getId() != null) {
      return -1;
    }
    playlist.setId(getPlaylists().size());
    getPlaylists().add(playlist);
    return playlist.getId();
  }

  public Integer updateUser(FygUser user) {
    if (user == null) {
      return -1;
    }
    if (user.getId() == null) {
      return -1;
    }
    if (user.getId() >= getUsers().size()) {
      return -1;
    }
    getUsers().set(user.getId(), user);
    return user.getId();
  }

  public Integer updateSong(FygSong song) {
    if (song == null) {
      return -1;
    }
    if (song.getId() == null) {
      return -1;
    }
    if (song.getId() >= getSongs().size()) {
      return -1;
    }
    getSongs().set(song.getId(), song);
    return song.getId();
  }

  public Integer updatePlaylist(FygPlaylist playlist) {
    if (playlist == null) {
      return -1;
    }
    if (playlist.getId() == null) {
      return -1;
    }
    if (playlist.getId() >= getPlaylists().size()) {
      return -1;
    }
    getPlaylists().set(playlist.getId(), playlist);
    return playlist.getId();
  }

  public Integer deleteUser(Integer id) {
    if (id == null) {
      return -1;
    }
    if (id >= getUsers().size()) {
      return -1;
    }
    getUsers().remove(id.intValue());
    return id;
  }

  public Integer deleteSong(Integer id) {
    if (id == null) {
      return -1;
    }
    if (id >= getSongs().size()) {
      return -1;
    }
    getSongs().remove(id.intValue());
    return id;
  }

  public Integer deletePlaylist(Integer id) {
    if (id == null) {
      return -1;
    }
    if (id >= getPlaylists().size()) {
      return -1;
    }
    getPlaylists().remove(id.intValue());
    return id;
  }

  public FygUser deleteUserGql(Integer id) {
    if (id == null) {
      return null;
    }
    if (id >= getUsers().size()) {
      return null;
    }
    FygUser user = getUsers().get(id);
    getUsers().remove(id.intValue());
    return user;
  }

  public FygSong deleteSongGql(Integer id) {
    if (id == null) {
      return null;
    }
    if (id >= getSongs().size()) {
      return null;
    }
    FygSong song = getSongs().get(id);
    getSongs().remove(id.intValue());
    return song;
  }

  public FygPlaylist deletePlaylistGql(Integer id) {
    if (id == null) {
      return null;
    }
    if (id >= getPlaylists().size()) {
      return null;
    }
    FygPlaylist playlist = getPlaylists().get(id);
    getPlaylists().remove(id.intValue());
    return playlist;
  }

}