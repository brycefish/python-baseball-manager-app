import csv
LINEUPFILE = "lineup.csv"

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