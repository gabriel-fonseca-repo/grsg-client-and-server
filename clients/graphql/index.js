const host = "http://localhost:8082/graphql";

async function callEndpoint(query, variables = {}) {
  const response = await fetch(host, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({ query, variables }),
  });
  return response;
}

async function makeRequest(query, variables = {}) {
  try {
    const response = await callEndpoint(query, variables);

    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }

    const data = await response.json();
    if (data.errors) {
      throw new Error(
        `Erro no GraphQL: ${data.errors.map((e) => e.message).join(", ")}`
      );
    }

    console.log(data);

    return data;
  } catch (error) {
    console.error("Erro ao buscar os dados:", error);
  }
}

makeRequest(`
  query ListAllUsers {
    listAllUsers {
        age
        id
        name
    }
  }`
);

makeRequest(`
  query ListAllSongs {
    listAllSongs {
        artist
        id
        name
    }
  }`
);

makeRequest(`
  query ListAllPlaylistsByUser($userId: Int) {
    listAllPlaylistsByUser(userId: $userId) {
        id
        name
        songs
        userId
    }
  }`,
  { userId: 10 }
);

makeRequest(`
  query ListAllSongDataOfPlaylist($playlistId: Int) {
    listAllSongDataOfPlaylist(playlistId: $playlistId) {
        artist
        id
        name
    }
  }`,
  { playlistId: 8 }
);

makeRequest(`
  query ListAllPlaylistsWithSong($songId: Int) {
    listAllPlaylistsWithSong(songId: $songId) {
        id
        name
        songs
        userId
    }
  }`,
  { songId: 6 }
);
