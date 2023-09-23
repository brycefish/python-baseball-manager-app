#!/usr/bin/env python3
# Bryce Fish
# Project 1
# Server-Side Programming

def menu_title():
    print()

def menu_line():
    print("================================================================")

def menu_options():
   print("MENU OPTIONS")
   print("1 – Calculate batting average")
   print("2 - Exit program")

def calc_bat_avg(num_bats_input, num_hits_input):
    batting_avg = num_hits_input / num_bats_input
    batting_avg = round(batting_avg, 3)
    return batting_avg

#### Main ####
def main():
    menu_line()
    menu_title()
    menu_options()
    menu_line()

    exitChar = True
    while exitChar == True:
        print()
        option = input("Menu option: ")

        if option == '1':
            print("-- Calculate batting average --")
            num_bats_input = int(input("Official number of at bats: "))
            num_hits_input = int(input("Number of hits: "))
            
            batting_average = calc_bat_avg(num_bats_input, num_hits_input)
            print(f"Batting average: {batting_average}")

        elif option == '2':
            print("Bye!")
            exitChar = False

        else:
            print("Not a valid option. Please try again")
            print()
            menu_options()

if __name__ == "__main__":
    main()