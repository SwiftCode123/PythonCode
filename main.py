players = []

num = int(input("Enter a whole number of players: "))

for i in range(0, num):
    player_name = input("Enter player name: ")
    players.append(player_name)

player_number = None
player_numbers = []
for i in players:
    player_number = int(input(i + ", pick a number: "))
    player_numbers.append(player_number)

max_number = max(player_numbers)
print("The max number picked was: " + str(max_number))
