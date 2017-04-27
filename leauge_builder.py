import csv

def get_players(sfilename):
    players = []
    with open(sfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        columns = list(reader)
        for column in columns:
            players.append(column)
    return players

def sort_players(players):
    has_exp = []
    no_exp = []
    for player in players:
        if player['Soccer Experience'] == "YES":
            has_exp.append(player)
        else:
            no_exp.append(player)
    return has_exp, no_exp


def build_team(a_players, b_players):
    team1 = a_players[0:3] + b_players[0:3]
    team2 = a_players[3:6] + b_players[3:6]
    team3 = a_players[6:] + b_players[6:]
    return team1, team2, team3


def write_team(t1, t2, t3):
    with open('teams.txt', 'w') as file:
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
    leauge_roster = t1 + t2 + t3
    for i in range(0,len(leauge_roster)):
        first_name=leauge_roster[i]["Name"].split()[0]
        last_name = leauge_roster[i]["Name"].split()[1]
        filename = first_name+'_'+last_name+'.txt'
        with open(filename, 'w') as file:
            file.write("Dear ")
            file.write(leauge_roster[i]['Guardian Name(s)'])
            file.write(",")
            file.write("\n\n")
            file.write("Your child: ")
            file.write(leauge_roster[i]["Name"])
            file.write(" is on the ")
            if leauge_roster[i] in t1:
                file.write("Dragons.\n")
                file.write("Our first practice is Thursday, May 4nd at 3pm.\n")
            elif leauge_roster[i] in t2:
                file.write("Sharks.\n")
                file.write("Our first practice is Wednesday, May 3rd at 3pm.\n")
            else:
                file.write("Raptors.\n")
                file.write("Our first practice is Tuesday, May 2nd at 3pm.\n")
            file.write("If you have any questions please contact your coach.\n")
            file.write("\n\n")
            file.write("Good luck and Have Fun!")






if __name__ == '__main__':
    players = get_players("soccer_players.csv")
    experts, beginners = sort_players(players)
    dragons, sharks, raptors = build_team(experts, beginners)
    write_team(dragons, sharks, raptors)
    welcome_letters(dragons, sharks, raptors)