package com.fyg.data;

import java.util.List;

public class FygDataFile {
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
