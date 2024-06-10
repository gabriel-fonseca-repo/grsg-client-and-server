import jakarta.jws.WebMethod;
import jakarta.jws.WebService;

import java.util.List;

@WebService(name = "MSService", serviceName = "MSService", targetNamespace = "http://musicstreaming.com")
public interface MSService {

  @WebMethod
  List<FygUser> getUsers();

  @WebMethod
  List<FygSong> getSongs();

  @WebMethod
  List<FygPlaylist> getPlaylists();

  @WebMethod
  Integer createUser(FygUser user);

  @WebMethod
  Integer createSong(FygSong song);

  @WebMethod
  Integer createPlaylist(FygPlaylist playlist);

  @WebMethod
  Integer updateUser(FygUser user);

  @WebMethod
  Integer updateSong(FygSong song);

  @WebMethod
  Integer updatePlaylist(FygPlaylist playlist);

  @WebMethod
  Integer deleteUser(Integer id);

  @WebMethod
  Integer deleteSong(Integer id);

  @WebMethod
  Integer deletePlaylist(Integer id);

}
