import jakarta.inject.Inject;
import jakarta.jws.WebMethod;
import jakarta.jws.WebService;

import java.util.List;

@WebService(name = "MSService", serviceName = "MSService", targetNamespace = "http://musicstreaming.com")
public class MSServiceImpl implements MSService {

  @Inject
  Database database;

  @WebMethod
  @Override
  public List<FygUser> listAllUsers() {
    return database.getUsers();
  }

  @WebMethod
  @Override
  public List<FygSong> listAllSongs() {
    return database.getSongs();
  }

  @WebMethod
  @Override
  public List<FygPlaylist> listAllPlaylistsByUser(Integer userId) {
    return database.getPlaylists().stream().filter(p -> p.getUserId().equals(userId)).toList();
  }

  @WebMethod
  @Override
  public List<FygSong> listAllSongDataOfPlaylist(Integer playlistId) {
    FygPlaylist playlist =
      database.getPlaylists().stream().filter(p -> p.getId().equals(playlistId)).findFirst().orElse(null);
    return database.getSongs().stream().filter(s -> {
      if (playlist != null) {
        return playlist.getSongs().contains(s.getId());
      } return false;
    }).toList();
  }

  @WebMethod
  @Override
  public List<FygPlaylist> listAllPlaylistsWithSong(Integer songId) {
    return database.getPlaylists().stream().filter(p -> p.getSongs().contains(songId)).toList();
  }

}
