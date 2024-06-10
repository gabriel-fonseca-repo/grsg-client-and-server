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
  public List<FygUser> getUsers() {
    return database.getUsers();
  }

  @WebMethod
  @Override
  public List<FygSong> getSongs() {
    return database.getSongs();
  }

  @WebMethod
  @Override
  public List<FygPlaylist> getPlaylists() {
    return database.getPlaylists();
  }

  @WebMethod
  @Override
  public Integer createUser(FygUser user) {
    return database.createUser(user);
  }

  @WebMethod
  @Override
  public Integer createSong(FygSong song) {
    return database.createSong(song);
  }

  @WebMethod
  @Override
  public Integer createPlaylist(FygPlaylist playlist) {
    return database.createPlaylist(playlist);
  }

  @WebMethod
  @Override
  public Integer updateUser(FygUser user) {
    return database.updateUser(user);
  }

  @WebMethod
  @Override
  public Integer updateSong(FygSong song) {
    return database.updateSong(song);
  }

  @WebMethod
  @Override
  public Integer updatePlaylist(FygPlaylist playlist) {
    return database.updatePlaylist(playlist);
  }

  @WebMethod
  @Override
  public Integer deleteUser(Integer id) {
    return database.deleteUser(id);
  }

  @WebMethod
  @Override
  public Integer deleteSong(Integer id) {
    return database.deleteSong(id);
  }

  @WebMethod
  @Override
  public Integer deletePlaylist(Integer id) {
    return database.deletePlaylist(id);
  }

}
