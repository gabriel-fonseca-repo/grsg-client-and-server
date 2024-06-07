const host = "http://localhost:8080";

async function callEndpoint(endpoint) {
  const response = await fetch(host + endpoint, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  return response;
}

async function makeRequest(endpoint) {
  try {
    const response = await callEndpoint(endpoint);

    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);

    return data;
  } catch (error) {
    console.error("Erro ao buscar os dados:", error);
  }
}

const userId = 10;
const playlistId = 8;
const songId = 6;

makeRequest("/users");
makeRequest("/songs");
makeRequest(`/playlists-by-user/${userId}`);
makeRequest(`/songs-by-playlist/${playlistId}`);
makeRequest(`/playlists-by-song/${songId}`);