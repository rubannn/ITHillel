chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}

filtred_players = dict()
for name, raiting in chess_players.items():
    if raiting > 2000:
        a, b = name.split()
        filtred_players[raiting] = f'{a[:-1]} {b[0]}.'

print(filtred_players)
