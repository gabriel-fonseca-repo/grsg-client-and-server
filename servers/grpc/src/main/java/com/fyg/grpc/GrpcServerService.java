package com.fyg.grpc;

import com.fyg.grpc.proto.*;
import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

import java.util.List;

@GrpcService
class GrpcServerService extends MusicStreamingServiceGrpc.MusicStreamingServiceImplBase {

  private final Database database;

  public GrpcServerService(Database database) {
    this.database = database;
  }

  @Override
  public void getUsers(EmptyRequest request, StreamObserver<GetUsersReply> responseObserver) {
    List<User> response = database.getUsers().stream().map(user -> User.newBuilder()
        .setId(user.getId())
        .setName(user.getName())
        .setId(user.getId())
        .build()).toList();
    responseObserver.onNext(GetUsersReply.newBuilder().addAllUsers(response).build());
    responseObserver.onCompleted();
  }

  @Override
  public void getSongs(EmptyRequest request, StreamObserver<GetSongsReply> responseObserver) {
    List<Song> response = database.getSongs().stream().map(song -> Song.newBuilder()
        .setId(song.getId())
        .setName(song.getName())
        .setArtist(song.getArtist())
        .build()).toList();
    responseObserver.onNext(GetSongsReply.newBuilder().addAllSongs(response).build());
    responseObserver.onCompleted();
  }

  @Override
  public void getPlaylists(EmptyRequest request, StreamObserver<GetPlaylistsReply> responseObserver) {
    List<Playlist> response = database.getPlaylists().stream().map(playlist -> Playlist.newBuilder()
        .setId(playlist.getId())
        .setName(playlist.getName())
        .addAllSongs(playlist.getSongs())
        .build()).toList();
    responseObserver.onNext(GetPlaylistsReply.newBuilder().addAllPlaylists(response).build());
    responseObserver.onCompleted();
  }

  @Override
  public void createUser(CreateUserRequest request, StreamObserver<User> responseObserver) {
    FygUser user = new FygUser(null, request.getName(), request.getAge());
    Integer userCreated = database.createUser(user);
    if (userCreated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(User.newBuilder()
          .setId(userCreated)
          .setName(user.getName())
          .setAge(user.getAge())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void createSong(CreateSongRequest request, StreamObserver<Song> responseObserver) {
    FygSong song = new FygSong(null, request.getName(), request.getArtist());
    Integer songCreated = database.createSong(song);
    if (songCreated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Song.newBuilder()
          .setId(songCreated)
          .setName(song.getName())
          .setArtist(song.getArtist())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void createPlaylist(CreatePlaylistRequest request, StreamObserver<Playlist> responseObserver) {
    FygPlaylist playlist = new FygPlaylist(null, request.getName(), request.getUserId(), request.getSongsList());
    Integer playlistCreated = database.createPlaylist(playlist);
    if (playlistCreated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Playlist.newBuilder()
          .setId(playlistCreated)
          .setName(playlist.getName())
          .addAllSongs(playlist.getSongs())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void updateUser(UpdateUserRequest request, StreamObserver<User> responseObserver) {
    FygUser user = new FygUser(request.getId(), request.getName(), request.getAge());
    Integer userUpdated = database.updateUser(user);
    if (userUpdated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(User.newBuilder()
          .setId(userUpdated)
          .setName(user.getName())
          .setAge(user.getAge())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void updateSong(UpdateSongRequest request, StreamObserver<Song> responseObserver) {
    FygSong song = new FygSong(request.getId(), request.getName(), request.getArtist());
    Integer songUpdated = database.updateSong(song);
    if (songUpdated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Song.newBuilder()
          .setId(songUpdated)
          .setName(song.getName())
          .setArtist(song.getArtist())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void updatePlaylist(UpdatePlaylistRequest request, StreamObserver<Playlist> responseObserver) {
    FygPlaylist playlist = new FygPlaylist(request.getId(), request.getName(), request.getUserId(), request.getSongsList());
    Integer playlistUpdated = database.updatePlaylist(playlist);
    if (playlistUpdated == -1) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Playlist.newBuilder()
          .setId(playlistUpdated)
          .setName(playlist.getName())
          .addAllSongs(playlist.getSongs())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void deleteUser(IdRequest request, StreamObserver<User> responseObserver) {
    FygUser userDeleted = database.deleteUserGql(request.getId());
    if (userDeleted == null) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(User.newBuilder()
          .setId(userDeleted.getId())
          .setName(userDeleted.getName())
          .setAge(userDeleted.getAge())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void deleteSong(IdRequest request, StreamObserver<Song> responseObserver) {
    FygSong songDeleted = database.deleteSongGql(request.getId());
    if (songDeleted == null) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Song.newBuilder()
          .setId(songDeleted.getId())
          .setName(songDeleted.getName())
          .setArtist(songDeleted.getArtist())
          .build());
    }
    responseObserver.onCompleted();
  }

  @Override
  public void deletePlaylist(IdRequest request, StreamObserver<Playlist> responseObserver) {
    FygPlaylist playlistDeleted = database.deletePlaylistGql(request.getId());
    if (playlistDeleted == null) {
      responseObserver.onNext(null);
    } else {
      responseObserver.onNext(Playlist.newBuilder()
          .setId(playlistDeleted.getId())
          .setName(playlistDeleted.getName())
          .addAllSongs(playlistDeleted.getSongs())
          .build());
    }
    responseObserver.onCompleted();
  }

}