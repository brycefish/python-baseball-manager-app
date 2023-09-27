#!/usr/bin/env python3
# Bryce Fish
# Project 1
# Server-Side Programming
# TO-DO: options-          #5     #6  

#####   display menu    #####
def display_menu():
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


#####    option 1:    #####
def display_lineup(lineup):
    print(f"\tPLAYER\t\tPOS\tAB\tH\tAVG")
    print("----------------------------------------------------------------")

    if len(lineup) == 0:
        print("There are no players on the lineup")
    else:
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



#####    option 2   #####
def enter_new_player():
    player = []
    possible_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    
    name = input("Name: ")
    player.append(name)

    while True:
        position = input("Position: ").upper()

        if position in possible_positions:
            player.append(position)
            break
        else:
            print("Invalid Position. Please try again")
            print("POSITIONS")
            print(possible_positions)

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


#####   option 3   #####
def remove_player(current_lineup):

    if len(current_lineup) < 1 :
        print("There are no players currently in the lineup")

    while len(current_lineup) > 0:
        index = int(input("Select lineup number to remove: "))
        if index < 1 or index > len(current_lineup):
            print("\nInvalid lineup number. Try again.")
        else:
            player_selected = current_lineup.pop(index - 1)
            print(f"\n{player_selected[0]} was removed\n")
            break

    return current_lineup


#####    Option 4: Move Player  #####
def move_player(lineup):
    current_num = int(input("Enter players current lineup number: "))
    if current_num < 1 or current_num > len(lineup):
        print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
    else:
        player = lineup.pop(current_num - 1)
        print(f"{player[0]} was selected.")
    
    new_num = int(input("New lineup number: "))
    if new_num < 1 or new_num > len(lineup):
        print(f"Invalid lineup number, please enter a number between 1 and {len(lineup)}")
    else:
        lineup.insert(new_num - 1, player)
        print(f"{player[0]} was moved/")



#####   Calculate Batting Average   ####
def calc_bat_avg(at_bats, num_hits):
    batting_avg =  num_hits / at_bats
    batting_avg = round(batting_avg, 3)
    
    return batting_avg


####    Main    ####
def main():
    lineup = []
    possible_positions = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
    #fake lineup for testing of course
    test_lineup = [["jonh", "P", 10, 2, 0.2],
                  ["billy", "SS", 11, 4, 0.364],
                  ["suzie", "3B", 9, 3, 0.333],
                  ["roger", "C", 4, 1, 0.25],
                  ["christopher", "3B", 10, 5, 0.5],
                  ["randy", "1B", 9, 3, 0.333]]

    display_menu()
    while True:
        print()
        option = input("Menu option: ")
        if option == '1':
            display_lineup(test_lineup)

        elif option == '2':
            player = enter_new_player()
            lineup.append(player)

        elif option == '3':
            remove_player(test_lineup)

        elif option == '4':
            move_player(test_lineup)

        elif option == '5':
            print("option 5")

        elif option == '6':
            print("option 6")

        elif option == '7':
            print("\nBye!")
            break

        else:
            print("Not a valid option. Please try again")


if __name__ == "__main__":
    main()
