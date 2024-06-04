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
  public void listAllUsers(EmptyRequest req, StreamObserver<ListAllUsersReply> responseObserver) {

    List<User> users =
      database.getUsers().stream().map(u -> User.newBuilder().setId(u.getId()).setName(u.getName()).setAge(u.getAge()).build()).toList();

    responseObserver.onNext(ListAllUsersReply.newBuilder().addAllUsuarios(users).build());
    responseObserver.onCompleted();
  }

  @Override
  public void listAllSongs(EmptyRequest req, StreamObserver<ListAllSongsReply> responseObserver) {

    List<Song> songs =
      database.getSongs().stream().map(s -> Song.newBuilder().setId(s.getId()).setName(s.getName()).setArtist(s.getArtist()).build()).toList();

    responseObserver.onNext(ListAllSongsReply.newBuilder().addAllSongs(songs).build()); responseObserver.onCompleted();
  }

  @Override
  public void listAllPlaylistsByUser(ListAllPlaylistsByUserRequest req,
                                     StreamObserver<ListAllPlaylistsByUserReply> responseObserver) {

    List<Playlist> playlists =
      database.getPlaylists().stream().filter(p -> p.getUserId().equals(req.getUserId())).map(p -> Playlist.newBuilder().setId(Math.toIntExact(p.getId())).setName(p.getName()).setUserId(p.getUserId()).build()).toList();

    responseObserver.onNext(ListAllPlaylistsByUserReply.newBuilder().addAllPlaylists(playlists).build());
    responseObserver.onCompleted();
  }

  @Override
  public void listAllSongDataOfPlaylist(ListAllSongDataOfPlaylistRequest req,
                                        StreamObserver<ListAllSongDataOfPlaylistReply> responseObserver) {

    Playlist playlist =
      database.getPlaylists().stream().filter(p -> p.getId().equals(req.getPlaylistId())).findFirst().map(p -> Playlist.newBuilder().setId(Math.toIntExact(p.getId())).setName(p.getName()).setUserId(p.getUserId()).addAllSongs(p.getSongs()).build()).orElse(null);

    List<Song> songs = database.getSongs().stream().filter(s -> {
      if (playlist != null) {
        return playlist.getSongsList().contains(Math.toIntExact(s.getId()));
      }
      return false;
    }).map(s -> Song.newBuilder().setId(s.getId()).setName(s.getName()).setArtist(s.getArtist()).build()).toList();

    responseObserver.onNext(ListAllSongDataOfPlaylistReply.newBuilder().addAllSongsFromPlaylist(songs).build());
    responseObserver.onCompleted();
  }

  @Override
  public void listAllPlaylistsWithSong(ListAllPlaylistsWithSongRequest req,
                                       StreamObserver<ListAllPlaylistsWithSongReply> responseObserver) {

    List<Playlist> playlists =
      database.getPlaylists().stream().filter(p -> p.getSongs().contains(req.getSongId())).map(p -> Playlist.newBuilder().setId(Math.toIntExact(p.getId())).setName(p.getName()).setUserId(p.getUserId()).addAllSongs(p.getSongs()).build()).toList();

    responseObserver.onNext(ListAllPlaylistsWithSongReply.newBuilder().addAllPlaylistData(playlists).build());
    responseObserver.onCompleted();
  }

}