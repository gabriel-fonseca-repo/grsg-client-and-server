import random as r


def random_user_id():
    return r.randint(0, 19)


def random_playlist_id():
    return r.randint(0, 29)


def random_song_id():
    return r.randint(0, 99)
