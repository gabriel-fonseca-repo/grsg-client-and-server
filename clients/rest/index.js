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

async function callEndpoint(endpoint, method, body) {
  const requestOptions = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (method !== "GET") {
    requestOptions.body = JSON.stringify(body);
  }

  const response = await fetch(`http://localhost:8080${endpoint}`, requestOptions);
  return response;
}

async function makeRequest(endpoint, method = "GET", body = {}) {
  try {
    const response = await callEndpoint(endpoint, method, body);

    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.status}`);
    }

    const data = await response.json();

    console.log(`Status (${method} ${endpoint}): ${response.status}`);

    return data;
  } catch (error) {
    console.error(`Erro ao buscar os dados (${method} ${endpoint}):`, error);
  }
}



// Consultas
await makeRequest("/users");
await makeRequest("/songs");
await makeRequest("/playlists");

// Cadastros
await makeRequest("/users", "POST", { name: faker.person.fullName(), age: randomInt(18, 99) });
await makeRequest("/songs", "POST", { name: faker.music.songName(), artist: faker.person.firstName() });
await makeRequest("/playlists", "POST", { name: faker.music.genre(), userId: randomInt(0, 19), songs: randomSongs() });

// Atualizações
await makeRequest("/users", "PATCH", { id: randomInt(0, 19), name: faker.person.fullName(), age: randomInt(18, 99) });
await makeRequest("/songs", "PATCH", { id: randomInt(0, 99), name: faker.music.songName(), artist: faker.person.firstName() });
await makeRequest("/playlists", "PATCH", { id: randomInt(0, 29), name: faker.music.genre(), userId: randomInt(0, 19), songs: randomSongs() });

// Deletar
await makeRequest(`/users/${randomInt(0, 19)}`, "DELETE");
await makeRequest(`/songs/${randomInt(0, 99)}`, "DELETE");
await makeRequest(`/playlists/${randomInt(0, 29)}`, "DELETE");
