#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.



def all_time_record():
    record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    lines = record_file.readlines()[1:]
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].split(',')
    #print(lines)
    
    #Find first team
    earliest = lines[0]
    date = lines[0][0].split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    
    for i in lines:
        temp_date = i[0].split("-")
        temp_year = int(temp_date[0])
        temp_month = int(temp_date[1])
        temp_day = int(temp_date[2])
        if (temp_year < year):
            earliest = i
            day = temp_day
            month = temp_month
            year = temp_year
        elif (temp_year <= year and temp_month < month):
            earliest = i
            day = temp_day
            month = temp_month
            year = temp_year
        elif (temp_year <= year and temp_month <= month and temp_day < day):
            earliest = i
            day = temp_day
            month = temp_month
            year = temp_year
    print(earliest[1])
        
    wins = 0
    lose = 0
    tie = 0
    win_points = 0
    lose_points = 0
    
    year_wins = 0
    year_lose = 0
    year_tie = 0
    
    my_dict = {}
    for i in lines:
        if i[1] in my_dict.keys():
            my_dict[i[1]][0] += (int(i[3]) - int(i[4]))
            my_dict[i[1]][1] += 1
        else:
            my_dict[i[1]] = [(int(i[3]) - int(i[4])), 1]

        date = i[0].split("-")
        if int(date[0]) >= 1933 and int(date[0]) <= 1963:
            if int(i[3]) > int(i[4]):
                year_wins += 1
            elif int(i[3]) < int(i[4]):
                
                year_lose += 1
            elif int(i[3]) == int(i[4]):
                year_tie += 1
                
        if i[2] == "Home":
            win_points += int(i[3])
            lose_points += int(i[4])
            if int(i[3]) > int(i[4]):
                wins += 1
            elif int(i[3]) < int(i[4]):
                
                lose += 1
            elif int(i[3]) == int(i[4]):
                tie += 1
    print(win_points, lose_points)
    print(str(wins) + "-" + str(lose) + "-" + str(tie))
    print(str(year_wins) + "-" + str(year_lose) + "-" + str(year_tie))
    print(max(my_dict.values()))
    #print(my_dict)
    highest_average = list(my_dict.keys())[0]

    for i in my_dict.keys():
        if my_dict[i][1] >= 5:
            if((my_dict[i][0] / my_dict[i][1]) > (my_dict[highest_average][0] / my_dict[highest_average][1])):
                highest_average = i
    print(highest_average)
            
    
all_time_record()
