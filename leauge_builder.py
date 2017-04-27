import csv


"""get_players takes in a single argument which needs to be a csv file. It parses through the file columns and 
adds each item, in this case players, to the players list as a Ordered Dictionary and returns the players value
"""
def get_players(sfilename):
    players = []
    with open(sfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        columns = list(reader)
        for column in columns:
            players.append(column)
    return players

"""sort_players takes the Ordered Dictionay value from get_players as an argument. It will loop through each player
and check to see if the field 'Soccer Experience' has the value of YES or NO. If it is YES it will add that player to
the has_exp list, if NO it will add that player to the no_exp list and return both lists as a tuple. 
"""
def sort_players(players):
    has_exp = []
    no_exp = []
    for player in players:
        if player['Soccer Experience'] == "YES":
            has_exp.append(player)
        else:
            no_exp.append(player)
    return has_exp, no_exp

"""
build_team takes two values, a_players and b_players. It creates varibles which is the first three
items in a_players and concatenates the first three items in b_players to create a new list. It will return
each variable as a tuple.
"""
def build_team(a_players, b_players):
    team1 = a_players[0:3] + b_players[0:3]
    team2 = a_players[3:6] + b_players[3:6]
    team3 = a_players[6:] + b_players[6:]
    return team1, team2, team3

"""
write_team takes three arguments which in this case will be eact team created by build_team. It then 
creates a file called teams.txt and writes out to the file the team name as well as the roster for each team
"""
def team_rosters(t1, t2, t3):
    with open('teams.txt', 'w') as file:
        file.write("Dragons\n")
        for i in range(0,len(t1)):
            file.write(t1[i]['Name'])
            file.write(' , ')
            file.write(t1[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t1[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n\n\n')
        file.write("Sharks\n")
        for i in range(0, len(t2)):
            file.write(t2[i]['Name'])
            file.write(' , ')
            file.write(t2[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t2[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')
        file.write("Raptors\n")
        for i in range(0, len(t3)):
            file.write(t3[i]['Name'])
            file.write(' , ')
            file.write(t3[i]['Soccer Experience'])
            file.write(' , ')
            file.write(t3[i]['Guardian Name(s)'])
            file.write('\n')
        file.write('\n \n \n')
"""
welcome_letters take three arguments which will be each team. It recombines each team into a single list 
which is the league_roster. It then loops through each player in the roster assigning variables to the players
first and last name to be used to create new txt files for each player. 
"""
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
    #assigns varible player to the value of get_players with the 'soccer_players.csv' file
    players = get_players("soccer_players.csv")
    #unpacks returned value of sorted_players called with players argument in to experts and beginners varibles
    experts, beginners = sort_players(players)
    #unpacks returned value of build_team called with experts and beginners as aruments to varibles of team names
    dragons, sharks, raptors = build_team(experts, beginners)
    #creates the teams.txt file with each team roster written to the file
    team_rosters(dragons, sharks, raptors)
    #creates the welcome letter txt file for each player in their respected teams
    welcome_letters(dragons, sharks, raptors)