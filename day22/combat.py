import re

player_one_deck, player_two_deck = [], []
with open("decks.txt") as file:
    players = re.findall("(?<=Player \d:\n)(?:\d+\n?)+", file.read())
    for i, p in enumerate([player_one_deck, player_two_deck]):
        p.extend([int(n) for n in players[i].split("\n") if n != ''])



def play_combat(player_one, player_two):
    while len(player_one) != 0 and len(player_two) != 0:
        p1, p2 = player_one.pop(0), player_two.pop(0)
        if p1 > p2:
            player_one.extend([p1, p2])
        else:
            player_two.extend([p2, p1])
    winner = player_one if len(player_one) > 0 else player_two
    return sum([(i+1)*card for i, card in enumerate(winner[::-1])])


def play_recursive_combat(player_one, player_two, initial=True):
    played_decks = []
    while len(player_one) != 0 and len(player_two) != 0:
        if (player_one, player_two) in played_decks:
            return True
        played_decks.append((player_one.copy(), player_two.copy()))
        p1, p2 = player_one.pop(0), player_two.pop(0)
        round_winner = []
        if len(player_one) >= p1 and len(player_two) >= p2:
            round_winner = play_recursive_combat(player_one.copy()[:p1], player_two.copy()[:p2], False)
        else:
            round_winner = p1 > p2
        player_one.extend([p1, p2]) if round_winner else player_two.extend([p2, p1])
    winner = player_one if len(player_one) > 0 else player_two
    return sum([(i+1)*card for i, card in enumerate(winner[::-1])]) if initial else winner == player_one
    


print(play_combat(player_one_deck.copy(), player_two_deck.copy()))
print(play_recursive_combat(player_one_deck, player_two_deck))
