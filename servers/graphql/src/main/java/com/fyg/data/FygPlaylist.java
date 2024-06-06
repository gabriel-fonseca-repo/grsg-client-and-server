package com.fyg.data;

import java.util.List;

public class FygPlaylist {
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
