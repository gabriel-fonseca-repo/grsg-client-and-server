# faker version 25.4.0
from faker import Faker
import random as r
import json as j

fake = Faker()

# criando 20 usuários:
# message User {
#   int32 id = 1;
#   string name = 2;
#   int32 age = 3;
# }
usuarios = []
for i in range(20):
    usuarios.append({"id": i, "name": fake.name(), "age": r.randint(18, 99)})

# criando 100 musicas:
# message Song {
#   int32 id = 1;
#   string name = 2;
#   int32 artist = 3;
# }
musicas = []
for i in range(100):
    musicas.append({"id": i, "name": fake.catch_phrase(), "artist": fake.name()})

# criando 30 playlists:
# message PlaylistData {
#   int32 id = 1;
#   string name = 2;
#   int32 userId = 3;
# }

# message PlaylistDataWithSongs {
#   PlaylistData playlistData = 1;
#   repeated Song songs = 2;
# }
playlists_with_songs = []
for i in range(30):
    playlists_with_songs.append(
        {
            "id": i,
            "name": fake.word(),
            "userId": r.randint(0, 19),
            "songs": [r.randint(0, 99) for _ in range(r.randint(5, 15))],
        }
    )

# salvando os dados em um arquivo json
with open("data.json", "w") as f:
    j.dump(
        {"usuarios": usuarios, "musicas": musicas, "playlists": playlists_with_songs}, f
    )

print("Dados salvos com sucesso!")
