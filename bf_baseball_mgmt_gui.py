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

def calc_bat_avg(at_bats, num_hits):
    batting_avg = at_bats / num_hits
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

        # added code for logical errors, no error handling
        if option == '1':
            print("-- Calculate batting average --")

            at_bats = int(input("Official number of at bats: "))
            if at_bats < 0:
                print("Number of at bats must be greater than 0.")
                continue

            num_hits = int(input("Number of hits: "))
            if num_hits < 0:
                print("Number of hits must be greater than 0.")
                continue
            elif num_hits > at_bats:
                print("Number of hits must be less that number of at bats")
                continue
            
            batting_average = calc_bat_avg(at_bats, num_hits)
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