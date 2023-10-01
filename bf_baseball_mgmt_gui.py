#!/usr/bin/env python3
# Bryce Fish
# Project 1
# Server-Side Programming
import csv
LINEUPFILE = "lineup.csv"

def display_menu():
    print()
    print("================================================================")
    print("MENU OPTIONS")
    print("1 - Display lineup" +
          "\n2 - Add player" +
          "\n3 - Remove player" +
          "\n4 - Move player" +
          "\n5 - Edit player position" +
          "\n6 - Edit player stats" +
          "\n7 - Exit program")
    print()
    print("POSTIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("================================================================")

def read_lineup_csv():
    newlineup = []
    with open(LINEUPFILE, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            newlineup.append(row)
    return newlineup

def write_lineup_csv(lineup):
    with open(LINEUPFILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lineup)

def calc_bat_avg(at_bats, num_hits):
    batting_avg =  num_hits / at_bats
    batting_avg = round(batting_avg, 3)
    return batting_avg


####    option 1: display lineup   ####
def display_lineup(lineup):
    
    lineup = read_lineup_csv()
    if len(lineup) == 0:
        print("There are no players to display")
    else:
        print(f"\tPLAYER\t\tPOS\tAB\tH\tAVG")
        print("----------------------------------------------------------------")
        print()
        lineup_count = 0
        for player in lineup:
            lineup_count += 1
            for index, item in enumerate(player):
                if index == 0:
                    if len(player[0]) <= 7:
                        print(f"{lineup_count}\t{item}", end='\t\t')
                    else:
                        print(f"{lineup_count}\t{item}", end='\t')
                else:
                    print(item, end='\t')
            print()


####    option 2: enter new player    ####
def enter_new_player(valid_positions):
    player = []
    name = input("Name: ")
    player.append(name)

    while True:
        position = input("Position: ").upper()
        if position in valid_positions:
            player.append(position)
            break
        else:
            print("Invalid Position. Please try again")
            print("POSITIONS:")
            print(valid_positions)
    while True:
        at_bats = int(input("At bats: "))
        if at_bats < 0:
            print("At bats must be a positive integer ")
        else:
            break
    while True:
        num_hits = int(input("Hits: "))
        if num_hits < 0:
            print("Hits must be greater than zero")
        elif num_hits > at_bats:
            print("Hits must be lower than at bats")
        else:
            break
    
    bat_avg = calc_bat_avg(at_bats, num_hits)
    player.append(at_bats)
    player.append(num_hits)
    player.append(bat_avg)
    print(f"{name} was added")
    return player


####   option 3: remove player   ####
def remove_player(current_lineup):
    if len(current_lineup) == 0:
        print("There are no players to display")
        return

    while len(current_lineup) > 0:
        index = int(input("Select lineup number to remove: "))
        if index < 1 or index > len(current_lineup):
            print("\nInvalid lineup number. Try again.")
        else:
            player_selected = current_lineup.pop(index - 1)
            print(f"{player_selected[0]} was removed.")
            break
    write_lineup_csv(current_lineup)
    

####    Option 4: move player   ####
def move_player(lineup):
    if len(lineup) == 0:
        print("There are no players to display")
        return
    
    # get player
    current_num = int(input("Enter players current lineup number: "))
    if current_num < 1 or current_num > len(lineup):
        print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
    else:
        player = lineup.pop(current_num - 1)
        print(f"{player[0]} was selected.")
    
    # move player
    new_num = int(input("New lineup number: "))
    if new_num < 1 or new_num > len(lineup):
        print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
    else:
        lineup.insert(new_num - 1, player)
        write_lineup_csv(lineup)
        print(f"{player[0]} was moved.")
    

####   option 5: edit player position   ####
def edit_position(lineup, positions):
    if len(lineup) == 0:
        print("There are no players to display")
        return

    # get player
    print("Editing player position-")
    while True:
        player_index = int(input("Enter lineup number: "))
        if player_index < 1 or player_index > len(lineup):
            print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
        else:
            player = lineup[player_index - 1]
            print(f"{player[0]}'s current position is {player.pop(1)}")
            break

    # add new position
    while True:
        position = input("New position: ").upper()
        if position in positions:
            player.insert(1, position)
            print(f"{player[0]}'s position was changed.")
            #write to csv
            write_lineup_csv(lineup)
            break
        else:
            print("\nInvalid position. Please try again")
            print("POSITIONS")
            print(positions)


####   option 6: edit player stats ####
def edit_player_stats(lineup):
    if len(lineup) == 0:
        print("There are no players to display")
        return
    
    #get player
    print("Editing player stats-")
    while True:
        player_index = int(input("Enter player lineup number: "))
        if len(lineup) == 0:
            print("There are no players to display")
        elif player_index < 1 or player_index > len(lineup):
            print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
        else:
            player = lineup.pop(player_index - 1)
            print(f"You selected:\t {player[0]} AB={player.pop(2)} H={player.pop(3)}")
            player.pop()
            break

    # get stats
    while True:
        at_bats = int(input("At bats: "))
        if at_bats < 0:
            print("At bats must be a positive integer ")
        else:
            player.append(at_bats)
            break
    while True:
        num_hits = int(input("Hits: "))
        if num_hits < 0:
            print("Hits must be greater than zero")
        elif num_hits > at_bats:
            print("Hits must be lower than at bats")
        else:
            player.append(num_hits)
            break

    bat_avg = calc_bat_avg(at_bats, num_hits)
    player.append(bat_avg)
    lineup.insert(player_index - 1, player)
    write_lineup_csv(lineup)
    print(f"{player[0]} was added.")


####    Main    ####
def main():
    valid_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    lineup = read_lineup_csv()

    display_menu()
    while True:
        print()
        option = input("Menu option: ")

        if option == '1':
            display_lineup(lineup)

        elif option == '2':
            player = enter_new_player(valid_positions)
            lineup.append(player)
            write_lineup_csv(lineup)

        elif option == '3':
            remove_player(lineup)

        elif option == '4':
            move_player(lineup)

        elif option == '5':
            edit_position(lineup, valid_positions)

        elif option == '6':
            edit_player_stats(lineup)

        elif option == '7':
            break

        else:
            print("Not a valid option. Please try again")

    print("\nBye!")

if __name__ == "__main__":
    main()
