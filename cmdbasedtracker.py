from operator import itemgetter

# Created By Brenden Hernanderz
# this is a simple terminal based initative tracker
# might make it a touch fancier later
repeat = True

while repeat:
    print("Party Size?")

    try:
        party_size = int(input())
    except ValueError:
        print("Invalid party size. Enter an integer dummy.")

    combat_party = []

    for x in range(party_size):
        print("Party Member Name: ")
        member_name = input()
        print("Member's Roll: ")
        roll = int(input())
        combat_party.append((roll, member_name))

    print("Monster's Party Size: ")

    try:
        mon_party_size = int(input())
    except ValueError:
        print("Invalid party size. Enter an integer dummy.")

    for x in range(mon_party_size):
        print("Monster Name: ")
        mon_name = input()
        print("Monster's Roll: ")
        mon_roll = int(input())
        combat_party.append((mon_roll, mon_name))

    combat_party.sort(key=itemgetter(0), reverse=True) # Sorts by roll

    for thing in combat_party:
        print(thing[0], thing[1])

    print("Go again? (Y/N): ")
    if input() == "N" or input() == "n":
        repeat = False
    else:
        repeat = True