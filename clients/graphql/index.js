import { faker } from '@faker-js/faker';

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function randomSongs() {
  let songs = [];
  for (let i = 0; i < randomInt(5, 20); i++) {
    songs.push(randomInt(1, 100));
  }
  return songs;
}

async function callEndpoint(query, variables = {}) {
  const response = await fetch("http://127.0.0.1:8082/graphql", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "*/*",
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

    console.log(`Status: ${response.status}`);

    return data;
  } catch (error) {
    console.error(`Erro ao buscar os dados:`, error);
  }
}

// Consultas
await makeRequest(`
  query Users {
    users {
        age
        id
        name
    }
  }`.trim()
);

await makeRequest(`
  query Songs {
    songs {
        artist
        id
        name
    }
  }`.trim()
);

await makeRequest(`
  query Playlists {
    playlists {
        id
        name
        songs
        userId
    }
  }`.trim()
);

// Cadastros
await makeRequest(`
  mutation CreateUser($name: String!, $age: Int!) {
    createUser(user: { age: $age, name: $name }) {
        age
        id
        name
    }
  }`,
  { name: faker.person.fullName(), age: randomInt(18, 99) }
);

await makeRequest(`
  mutation CreateSong($name: String!, $artist: String!) {
    createSong(song: { artist: $artist, name: $name }) {
        artist
        id
        name
    }
  }`.trim(),
  { name: faker.music.songName(), artist: faker.person.firstName() }
);

await makeRequest(`
  mutation CreatePlaylist($name: String!, $userId: Int!, $songs: [Int!]!) {
    createPlaylist(playlist: { name: $name, userId: $userId, songs: $songs}) {
        id
        name
        songs
        userId
    }
  }`.trim(),
  { name: faker.music.genre(), userId: randomInt(0, 19), songs: randomSongs() }
);

// Atualizações
await makeRequest(`
  mutation UpdateUser($id: Int!, $name: String!, $age: Int!) {
    updateUser(user: { id: $id, age: $age, name: $name }) {
        age
        id
        name
    }
  }`.trim(),
  { id: randomInt(0, 19), name: faker.person.fullName(), age: randomInt(18, 99) }
);

await makeRequest(`
  mutation UpdateSong($id: Int!, $name: String!, $artist: String!) {
    updateSong(song: { id: $id, artist: $artist, name: $name }) {
        artist
        id
        name
    }
  }`.trim(),
  { id: randomInt(0, 99), name: faker.music.songName(), artist: faker.person.firstName() }
);

await makeRequest(`
  mutation UpdatePlaylist($id: Int!, $name: String!, $userId: Int!, $songs: [Int!]!) {
    updatePlaylist(playlist: { id: $id, name: $name, userId: $userId, songs: $songs}) {
        id
        name
        songs
        userId
    }
  }`.trim(),
  { id: randomInt(0, 29), userId: randomInt(0, 19), name: faker.music.genre(), songs: randomSongs() }
);

// Deletar
await makeRequest(`
  mutation DeleteUser($id: Int!) {
    deleteUser(id: $id) {
        age
        id
        name
    }
  }`.trim(),
  { id: randomInt(0, 19) }
);

await makeRequest(`
  mutation DeleteSong($id: Int!) {
    deleteSong(id: $id) {
        artist
        id
        name
    }
  }`.trim(),
  { id: randomInt(0, 99) }
);

await makeRequest(`
  mutation DeletePlaylist($id: Int!) {
    deletePlaylist(id: $id) {
        id
        name
        songs
        userId
    }
  }`.trim(),
  { id: randomInt(0, 29) }
);