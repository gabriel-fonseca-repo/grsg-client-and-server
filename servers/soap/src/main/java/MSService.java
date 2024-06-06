import jakarta.jws.WebMethod;
import jakarta.jws.WebService;

import java.util.List;

@WebService(name = "MSService", serviceName = "MSService", targetNamespace = "http://musicstreaming.com")
public interface MSService {

  @WebMethod
  List<FygUser> listAllUsers();

  @WebMethod
  List<FygSong> listAllSongs();

  @WebMethod
  List<FygPlaylist> listAllPlaylistsByUser(Integer userId);

  @WebMethod
  List<FygSong> listAllSongDataOfPlaylist(Integer playlistId);

  @WebMethod
  List<FygPlaylist> listAllPlaylistsWithSong(Integer songId);

}
