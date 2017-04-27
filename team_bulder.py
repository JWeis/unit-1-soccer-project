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

#print(experts[0:3])

def build_team(a_players, b_players):
    team1 = a_players[0:3] + b_players[0:3]
    team2 = a_players[3:6] + b_players[3:6]
    team3 = a_players[6:] + b_players[6:]
    return team1, team2, team3

dragons, sharks, raptors = build_team(experts, beginners)

#print(dragons[1]['Name'],dragons[1]['Height (inches)'])
#print(dragons[1]['Height (inches)'])
#print(dragons[1]['Soccer Experience'])
#print(dragons[1]['Guardian Name(s)'])

def write_team(t1, t2, t3):
    with open('teams.txt', 'a') as file:
        file.write("Dragons!!\n")
        file.write("_______________________\n")
        for i in range(0,6):
            file.write(t1[i]['Name'])
            file.write(' , ')
            file.write(t1[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t1[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n\n\n')
        file.write("Sharks!!\n")
        file.write("_______________________\n")
        for i in range(0, 6):
            file.write(t2[i]['Name'])
            file.write(' , ')
            file.write(t2[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t2[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')
        file.write("Raptors!!\n")
        file.write("_______________________\n")
        for i in range(0, 6):
            file.write(t3[i]['Name'])
            file.write(' , ')
            file.write(t3[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t3[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')

if __name__ == '__main__':
    write_team(dragons, sharks, raptors)
