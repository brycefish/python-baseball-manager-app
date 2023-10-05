import csv
LINEUPFILE = "lineup.csv"

def read_lineup_csv():
    newlineup = []
    try:
        with open(LINEUPFILE, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                newlineup.append(row)
        return newlineup
    except FileNotFoundError:
        print("\nTeam data file could not be found\n" + "A new file will be created\n")
        write_lineup_csv(newlineup)
        return newlineup


def write_lineup_csv(lineup):
    with open(LINEUPFILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lineup)