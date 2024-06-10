package com.fyg;

import com.fyg.data.FygPlaylist;
import com.fyg.data.FygSong;
import com.fyg.data.FygUser;
import jakarta.inject.Inject;
import org.eclipse.microprofile.graphql.*;

import java.util.List;

@GraphQLApi
public class MusicGraphQLResource {

  @Inject
  Database database;

  @Query
  @Description("Lista todos os usuários cadastrados no sistema.")
  public List<FygUser> getUsers() {
    return database.getUsers();
  }

  @Query
  @Description("Lista todas as músicas cadastradas no sistema.")
  public List<FygSong> getSongs() {
    return database.getSongs();
  }

  @Query
  @Description("Lista todas as playlists cadastradas no sistema.")
  public List<FygPlaylist> getPlaylists() {
    return database.getPlaylists();
  }

  @Mutation
  @Description("Cria um novo usuário no sistema.")
  public FygUser createUser(@Name("user") FygUser user) {
    Integer userCreated = database.createUser(user);
    if (userCreated == -1) {
      return null;
    }
    return user;
  }

  @Mutation
  @Description("Cria uma nova música no sistema.")
  public FygSong createSong(@Name("song") FygSong song) {
    Integer songCreated = database.createSong(song);
    if (songCreated == -1) {
      return null;
    }
    return song;
  }

  @Mutation
  @Description("Cria uma nova playlist no sistema.")
  public FygPlaylist createPlaylist(@Name("playlist") FygPlaylist playlist) {
    Integer playlistCreated = database.createPlaylist(playlist);
    if (playlistCreated == -1) {
      return null;
    }
    return playlist;
  }

  @Mutation
  @Description("Atualiza um usuário existente no sistema.")
  public FygUser updateUser(@Name("user") FygUser user) {
    Integer userUpdated = database.updateUser(user);
    if (userUpdated == -1) {
      return null;
    }
    return user;
  }

  @Mutation
  @Description("Atualiza uma música existente no sistema.")
  public FygSong updateSong(@Name("song") FygSong song) {
    Integer songUpdated = database.updateSong(song);
    if (songUpdated == -1) {
      return null;
    }
    return song;
  }

  @Mutation
  @Description("Atualiza uma playlist existente no sistema.")
  public FygPlaylist updatePlaylist(@Name("playlist") FygPlaylist playlist) {
    Integer playlistUpdated = database.updatePlaylist(playlist);
    if (playlistUpdated == -1) {
      return null;
    }
    return playlist;
  }

  @Mutation
  @Description("Deleta um usuário existente no sistema.")
  public FygUser deleteUser(@Name("id") Integer id) {
    return database.deleteUserGql(id);
  }

  @Mutation
  @Description("Deleta uma música existente no sistema.")
  public FygSong deleteSong(@Name("id") Integer id) {
    return database.deleteSongGql(id);
  }

  @Mutation
  @Description("Deleta uma playlist existente no sistema.")
  public FygPlaylist deletePlaylist(@Name("id") Integer id) {
    return database.deletePlaylistGql(id);
  }

}