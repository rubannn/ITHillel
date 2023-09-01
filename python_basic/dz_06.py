chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}

filtred_players = dict()
for name, raiting in chess_players.items():
    shortname = name.split()
    if raiting > 2000:
        filtred_players[raiting] = f'{shortname[0][:-1]} {shortname[1][0]}.'

print(filtred_players)
