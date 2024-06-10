package com.fyg.rest;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

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

  @GetMapping("/playlists")
  public ResponseEntity<List<FygPlaylist>> listAllPlaylists() {
    return ResponseEntity.ok(database.getPlaylists());
  }

  @PostMapping("/users")
  public ResponseEntity<Integer> createUser(@RequestBody(required = false) FygUser user) {
    Integer userCreated = database.createUser(user);
    if (userCreated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(userCreated);
  }

  @PostMapping("/songs")
  public ResponseEntity<Integer> createSong(@RequestBody(required = false) FygSong song) {
    Integer songCreated = database.createSong(song);
    if (songCreated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(songCreated);
  }

  @PostMapping("/playlists")
  public ResponseEntity<Integer> createPlaylist(@RequestBody(required = false) FygPlaylist playlist) {
    Integer playlistCreated = database.createPlaylist(playlist);
    if (playlistCreated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(playlistCreated);
  }

  @PatchMapping("/users")
  public ResponseEntity<Integer> updateUser(@RequestBody(required = false) FygUser user) {
    Integer userUpdated = database.updateUser(user);
    if (userUpdated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(userUpdated);
  }

  @PatchMapping("/songs")
  public ResponseEntity<Integer> updateSong(@RequestBody(required = false) FygSong song) {
    Integer songUpdated = database.updateSong(song);
    if (songUpdated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(songUpdated);
  }

  @PatchMapping("/playlists")
  public ResponseEntity<Integer> updatePlaylist(@RequestBody(required = false) FygPlaylist playlist) {
    Integer playlistUpdated = database.updatePlaylist(playlist);
    if (playlistUpdated == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(playlistUpdated);
  }

  @DeleteMapping("/users")
  public ResponseEntity<Integer> deleteUser(@RequestBody(required = false) Map<String, Integer> body) {
    Integer id = body.get("id");
    Integer deletedUser = database.deleteUser(id);
    if (deletedUser == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(deletedUser);
  }

  @DeleteMapping("/songs")
  public ResponseEntity<Integer> deleteSong(@RequestBody(required = false) Map<String, Integer> body) {
    Integer id = body.get("id");
    Integer deletedSong = database.deleteSong(id);
    if (deletedSong == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(deletedSong);
  }

  @DeleteMapping("/playlists")
  public ResponseEntity<Integer> deletePlaylist(@RequestBody(required = false) Map<String, Integer> body) {
    Integer id = body.get("id");
    Integer deletedPlaylist = database.deletePlaylist(id);
    if (deletedPlaylist == -1) {
      return ResponseEntity.badRequest().build();
    }
    return ResponseEntity.ok(deletedPlaylist);
  }

}
