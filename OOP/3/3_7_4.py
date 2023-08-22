lst_in = ['Балакирев; 34; 2048', 'Mediel; 27; 0', 'Влад; 18; 9012', 'Nina P; 33; 0']


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


players = []


for zn_odj in lst_in:
    l = zn_odj.split(";")
    players.append(Player(l[0], l[1], int(l[-1])))

players_filtered = list(filter(bool, players))
print(players_filtered)