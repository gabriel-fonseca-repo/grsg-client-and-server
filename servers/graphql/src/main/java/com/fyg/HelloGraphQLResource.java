package com.fyg;

import com.fyg.data.FygPlaylist;
import com.fyg.data.FygSong;
import com.fyg.data.FygUser;
import jakarta.inject.Inject;
import org.eclipse.microprofile.graphql.Description;
import org.eclipse.microprofile.graphql.GraphQLApi;
import org.eclipse.microprofile.graphql.Name;
import org.eclipse.microprofile.graphql.Query;

import java.util.List;

@GraphQLApi
public class HelloGraphQLResource {

  @Inject
  Database database;

  @Query
  @Description("Lista todos os usuários cadastrados no sistema.")
  public List<FygUser> listAllUsers() {
    return database.getUsers();
  }

  @Query
  @Description("Lista todas as músicas cadastradas no sistema.")
  public List<FygSong> listAllSongs() {
    return database.getSongs();
  }

  @Query
  @Description("Lista todas as playlists cadastradas no sistema.")
  public List<FygPlaylist> listAllPlaylistsByUser(@Name("userId") Integer userId) {
    return database.getPlaylists().stream().filter(p -> p.getUserId().equals(userId)).toList();
  }

  @Query
  @Description("Lista todas as músicas de uma playlist.")
  public List<FygSong> listAllSongDataOfPlaylist(@Name("playlistId") Integer playlistId) {
    FygPlaylist playlist =
      database.getPlaylists().stream().filter(p -> p.getId().equals(playlistId)).findFirst().orElse(null);
    return database.getSongs().stream().filter(s -> {
      if (playlist != null) {
        return playlist.getSongs().contains(s.getId());
      } return false;
    }).toList();
  }

  @Query
  @Description("Lista todas as playlists que contém uma música.")
  public List<FygPlaylist> listAllPlaylistsWithSong(@Name("songId") Integer songId) {
    return database.getPlaylists().stream().filter(p -> p.getSongs().contains(songId)).toList();
  }

}