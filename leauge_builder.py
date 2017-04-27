import csv

def get_players(sfilename):
    has_exp = []
    no_exp = []
    single_test = []
    with open(sfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        columns = list(reader)
        for column in columns:
            if column['Soccer Experience'] == "YES":
                has_exp.append(column)
            else:
                no_exp.append(column)
    return has_exp, no_exp

experts, beginners = get_players("soccer_players.csv")

def build_team(a_players, b_players):
    team1 = a_players[0:3] + b_players[0:3]
    team2 = a_players[3:6] + b_players[3:6]
    team3 = a_players[6:] + b_players[6:]
    return team1, team2, team3

dragons, sharks, raptors = build_team(experts, beginners)

def write_team(t1, t2, t3):
    with open('teams.txt', 'a') as file:
        file.write("Dragons\n")
        for i in range(0,6):
            file.write(t1[i]['Name'])
            file.write(' , ')
            file.write(t1[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t1[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n\n\n')
        file.write("Sharks\n")
        for i in range(0, 6):
            file.write(t2[i]['Name'])
            file.write(' , ')
            file.write(t2[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t2[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')
        file.write("Raptors\n")
        for i in range(0, 6):
            file.write(t3[i]['Name'])
            file.write(' , ')
            file.write(t3[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t3[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')

def welcome_letters(t1, t2, t3):
    a = dragons[1]["Name"][:].split()
    with open(a[0] + "_" + a[1])


#if __name__ == '__main__':
    #write_team(dragons, sharks, raptors)