package com.fyg.grpc;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Component;

import java.io.InputStream;
import java.util.List;

@Component
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

class FygUser {
  private Integer id;
  private String name;
  private Integer age;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Integer getAge() {
    return age;
  }

  public void setAge(Integer age) {
    this.age = age;
  }
}

class FygSong {
  private Integer id;
  private String name;
  private String artist;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getArtist() {
    return artist;
  }

  public void setArtist(String artist) {
    this.artist = artist;
  }
}

class FygPlaylist {
  private Integer id;
  private String name;
  private Integer userId;
  private List<Integer> songs;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Integer getUserId() {
    return userId;
  }

  public void setUserId(Integer userId) {
    this.userId = userId;
  }

  public List<Integer> getSongs() {
    return songs;
  }

  public void setSongs(List<Integer> songs) {
    this.songs = songs;
  }
}

class FygDataFile {
  private List<FygUser> usuarios;
  private List<FygSong> musicas;
  private List<FygPlaylist> playlists;

  public List<FygUser> getUsuarios() {
    return usuarios;
  }

  public void setUsuarios(List<FygUser> usuarios) {
    this.usuarios = usuarios;
  }

  public List<FygSong> getMusicas() {
    return musicas;
  }

  public void setMusicas(List<FygSong> musicas) {
    this.musicas = musicas;
  }

  public List<FygPlaylist> getPlaylists() {
    return playlists;
  }

  public void setPlaylists(List<FygPlaylist> playlists) {
    this.playlists = playlists;
  }
}