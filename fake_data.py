# faker version 25.4.0
from faker import Faker
import random as r
import json as j

fake = Faker()
qtd_usuarios = 3000
qtd_musicas = 10000
qtd_playlists = 4000

usuarios = []
for i in range(qtd_usuarios):
    usuarios.append({"id": i, "name": fake.name(), "age": r.randint(18, 99)})

musicas = []
for i in range(qtd_musicas):
    musicas.append({"id": i, "name": fake.catch_phrase(), "artist": fake.name()})

playlists_with_songs = []
for i in range(qtd_playlists):
    playlists_with_songs.append(
        {
            "id": i,
            "name": fake.word(),
            "userId": r.randint(0, qtd_usuarios - 1),
            "songs": [r.randint(0, qtd_musicas - 1) for _ in range(r.randint(5, 15))],
        }
    )

# salvando os dados em um arquivo json
with open("data/data.json", "w") as f:
    j.dump(
        {"usuarios": usuarios, "musicas": musicas, "playlists": playlists_with_songs}, f
    )

print("Dados salvos com sucesso!")
