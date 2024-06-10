import { faker } from '@faker-js/faker';
import csv from 'csv-writer';

const { createObjectCsvWriter } = csv;

const now = performance.now

const qtdUsuarios = 3000
const qtdMusicas = 10000
const qtdPlaylists = 4000

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

function randomAge() {
  return randomInt(18, 99);
}

function randomUserId() {
  return randomInt(0, qtdUsuarios - 1);
}

function randomSongId() {
  return randomInt(0, qtdMusicas - 1);
}

function randomPlaylistId() {
  return randomInt(0, qtdPlaylists - 1);
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

const actionsRandomData = {
  GetUsers: () => ({}),
  GetSongs: () => ({}),
  GetPlaylists: () => ({}),
  CreateUser: () => ({ name: faker.person.fullName(), age: randomAge() }),
  CreateSong: () => ({ name: faker.music.songName(), artist: faker.person.firstName() }),
  CreatePlaylist: () => ({ name: faker.music.genre(), userId: randomUserId(), songs: randomSongs() }),
  UpdateUser: () => ({ id: randomUserId(), name: faker.person.fullName(), age: randomAge() }),
  UpdateSong: () => ({ id: randomSongId(), name: faker.music.songName(), artist: faker.person.firstName() }),
  UpdatePlaylist: () => ({ id: randomPlaylistId(), userId: randomUserId(), name: faker.music.genre(), songs: randomSongs() }),
  DeleteUser: () => ({ id: randomUserId() }),
  DeleteSong: () => ({ id: randomSongId() }),
  DeletePlaylist: () => ({ id: randomPlaylistId() }),
}


const allActions = {
  GetUsers: {
    query: `
      query Users {
        users {
            age
            id
            name
        }
      }`.trim(),
    variables: {},
  },
  GetSongs: {
    query: `
      query Songs {
        songs {
            artist
            id
            name
        }
      }`.trim(),
    variables: {},
  },
  GetPlaylists: {
    query: `
      query Playlists {
        playlists {
            id
            name
            songs
            userId
        }
      }`.trim(),
    variables: {},
  },
  CreateUser: {
    query: `
      mutation CreateUser($name: String!, $age: Int!) {
        createUser(user: { age: $age, name: $name }) {
            age
            id
            name
        }
      }`.trim(),
    variables: { name: faker.person.fullName(), age: randomAge() },
  },
  CreateSong: {
    query: `
      mutation CreateSong($name: String!, $artist: String!) {
        createSong(song: { artist: $artist, name: $name }) {
            artist
            id
            name
        }
      }`.trim(),
    variables: { name: faker.music.songName(), artist: faker.person.firstName() },
  },
  CreatePlaylist: {
    query: `
      mutation CreatePlaylist($name: String!, $userId: Int!, $songs: [Int!]!) {
        createPlaylist(playlist: { name: $name, userId: $userId, songs: $songs}) {
            id
            name
            songs
            userId
        }
      }`.trim(),
    variables: { name: faker.music.genre(), userId: randomUserId(), songs: randomSongs() },
  },
  UpdateUser: {
    query: `
      mutation UpdateUser($id: Int!, $name: String!, $age: Int!) {
        updateUser(user: { id: $id, age: $age, name: $name }) {
            age
            id
            name
        }
      }`.trim(),
    variables: { id: randomUserId(), name: faker.person.fullName(), age: randomAge() },
  },
  UpdateSong: {
    query: `
      mutation UpdateSong($id: Int!, $name: String!, $artist: String!) {
        updateSong(song: { id: $id, artist: $artist, name: $name }) {
            artist
            id
            name
        }
      }`.trim(),
    variables: { id: randomSongId(), name: faker.music.songName(), artist: faker.person.firstName() },
  },
  UpdatePlaylist: {
    query: `
      mutation UpdatePlaylist($id: Int!, $name: String!, $userId: Int!, $songs: [Int!]!) {
        updatePlaylist(playlist: { id: $id, name: $name, userId: $userId, songs: $songs}) {
            id
            name
            songs
            userId
        }
      }`.trim(),
    variables: { id: randomPlaylistId(), userId: randomUserId(), name: faker.music.genre(), songs: randomSongs() },
  },
  DeleteUser: {
    query: `
      mutation DeleteUser($id: Int!) {
        deleteUser(id: $id) {
            age
            id
            name
        }
      }`.trim(),
    variables: { id: randomUserId() },
  },
  DeleteSong: {
    query: `
      mutation DeleteSong($id: Int!) {
        deleteSong(id: $id) {
            artist
            id
            name
        }
      }`.trim(),
    variables: { id: randomSongId() },
  },
  DeletePlaylist: {
    query: `
      mutation DeletePlaylist($id: Int!) {
        deletePlaylist(id: $id) {
            id
            name
            songs
            userId
        }
      }`.trim(),
    variables: { id: randomPlaylistId() },
  },
}

const csvWriter = createObjectCsvWriter({
  path: 'data/out/performance_data_graphql.csv',
  header: [
    { id: 'action', title: 'Action' },
    { id: 'totalRequests', title: 'Total Requests' },
    { id: 'failedRequests', title: 'Failed Requests' },
    { id: 'averageTime', title: 'Average Time (ms)' },
    { id: 'totalTime', title: 'Total Time (ms)' }
  ]
});

const performanceData = {};

function avgTime(actionName) {
  return (performanceData[actionName].totalTime / performanceData[actionName].totalRequests).toFixed(3);
}

for (const key in allActions) {
  performanceData[key] = {
    action: key,
    totalRequests: 0,
    failedRequests: 0,
    totalTime: 0,
    averageTime: 0,
  };
}

async function performAction(action, actionName) {
  action.variables = actionsRandomData[actionName]();
  const start = now();
  performanceData[actionName].totalRequests += 1;
  try {
    const response = await makeRequest(action.query, action.variables);
    const end = now();
    const time = (end - start).toFixed(3);
    performanceData[actionName].totalTime += parseFloat(time);
    performanceData[actionName].averageTime = avgTime(actionName);
    console.log(`Action: ${actionName} - Time: ${time}ms`);
    return response;
  } catch (error) {
    const end = now();
    const time = (end - start).toFixed(3);
    performanceData[actionName].failedRequests += 1;
    performanceData[actionName].totalTime += parseFloat(time);
    performanceData[actionName].averageTime = avgTime(actionName);
    console.error(`Action: ${actionName} - Error: ${error.message} - Time: ${time}ms`);
    throw error;
  }
}

async function loadTest(actions, iterations = 100) {
  for (let i = 0; i < iterations; i++) {
    for (const key in actions) {
      const action = actions[key];
      await performAction(action, key);
    }
  }
}

loadTest(allActions, 100)
  .then(() => {
    csvWriter.writeRecords(Object.values(performanceData))
      .then(() => console.log('Teste de carga concluído e dados exportados para performance_data.csv'))
      .catch((error) => console.error('Erro ao escrever dados no CSV', error));
  })
  .catch((error) => console.error('Erro durante o teste de carga', error));
