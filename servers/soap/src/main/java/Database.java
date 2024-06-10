import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlRootElement;

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

}

@XmlRootElement
class FygUser {
  private Integer id;
  private String name;
  private Integer age;

  @XmlElement
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  @XmlElement
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  @XmlElement
  public Integer getAge() {
    return age;
  }

  public void setAge(Integer age) {
    this.age = age;
  }
}

@XmlRootElement
class FygSong {
  private Integer id;
  private String name;
  private String artist;

  @XmlElement
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  @XmlElement
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  @XmlElement
  public String getArtist() {
    return artist;
  }

  public void setArtist(String artist) {
    this.artist = artist;
  }
}

@XmlRootElement
class FygPlaylist {
  private Integer id;
  private String name;
  private Integer userId;
  private List<Integer> songs;

  @XmlElement
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  @XmlElement
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  @XmlElement
  public Integer getUserId() {
    return userId;
  }

  public void setUserId(Integer userId) {
    this.userId = userId;
  }

  @XmlElement
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