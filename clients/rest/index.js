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

  const response = await fetch(`http://127.0.0.1:8080${endpoint}`, requestOptions);
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
    endpoint: '/users',
    method: 'GET',
    body: {},
  },
  GetSongs: {
    endpoint: '/songs',
    method: 'GET',
    body: {},
  },
  GetPlaylists: {
    endpoint: '/playlists',
    method: 'GET',
    body: {},
  },
  CreateUser: {
    endpoint: '/users',
    method: 'POST',
    body: {},
  },
  CreateSong: {
    endpoint: '/songs',
    method: 'POST',
    body: {},
  },
  CreatePlaylist: {
    endpoint: '/playlists',
    method: 'POST',
    body: {},
  },
  UpdateUser: {
    endpoint: '/users',
    method: 'PATCH',
    body: {},
  },
  UpdateSong: {
    endpoint: '/songs',
    method: 'PATCH',
    body: {},
  },
  UpdatePlaylist: {
    endpoint: '/playlists',
    method: 'PATCH',
    body: {},
  },
  DeleteUser: {
    endpoint: '/users',
    method: 'DELETE',
    body: {},
  },
  DeleteSong: {
    endpoint: '/songs',
    method: 'DELETE',
    body: {},
  },
  DeletePlaylist: {
    endpoint: '/playlists',
    method: 'DELETE',
    body: {},
  },
}

const csvWriter = createObjectCsvWriter({
  path: 'data/out/performance_data_rest.csv',
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
  action.body = actionsRandomData[actionName]();
  const start = now();
  performanceData[actionName].totalRequests += 1;
  try {
    const response = await makeRequest(action.endpoint, action.method, action.body);
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
