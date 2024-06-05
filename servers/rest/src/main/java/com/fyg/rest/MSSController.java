package com.fyg.rest;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class MSSController {

  private final Database database;

  public MSSController(Database database) {
    this.database = database;
  }

  @GetMapping("/users")
  public ResponseEntity<List<FygUser>> listAllUsers() {
    return ResponseEntity.ok(database.getUsers());
  }

  @GetMapping("/songs")
  public ResponseEntity<List<FygSong>> listAllSongs() {
    return ResponseEntity.ok(database.getSongs());
  }

  @GetMapping("/playlists-by-user/{userId}")
  public ResponseEntity<List<FygPlaylist>> listAllPlaylistsByUser(@PathVariable Integer userId) {
    return ResponseEntity.ok(database.getPlaylists().stream().filter(p -> p.getUserId().equals(userId)).toList());
  }

  @GetMapping("/songs-by-playlist/{playlistId}")
  public ResponseEntity<List<FygSong>> listAllSongDataOfPlaylist(@PathVariable Integer playlistId) {
    FygPlaylist playlist =
      database.getPlaylists().stream().filter(p -> p.getId().equals(playlistId)).findFirst().orElse(null);

    List<FygSong> songs = database.getSongs().stream().filter(s -> {
      if (playlist != null) {
        return playlist.getSongs().contains(s.getId());
      } return false;
    }).toList();

    return ResponseEntity.ok(songs);
  }

  @GetMapping("/playlists-with-song/{songId}")
  public ResponseEntity<List<FygPlaylist>> listAllPlaylistsWithSong(@PathVariable Integer songId) {

    List<FygPlaylist> playlists =
      database.getPlaylists().stream().filter(p -> p.getSongs().contains(songId)).toList();

    return ResponseEntity.ok(playlists);
  }

}
