#The line below will open a file containing information
#about every pokemon through Generation 7:

pokedex = open('../resource/lib/public/pokedex.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has 13 values, separated by commas.
#They are: 
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#Use this dataset to answer the questions below.
class pokemon():
    def __init__(self, ident, name, type1, hp, attack, defense, specialatk, specialdef, speed, gen, leg, mega, type2 = None):
        self.ident = ident
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialatk = specialatk
        self.specialdef = specialdef
        self.speed = speed
        self.gen = gen
        self.leg = self.set_bool(leg)
        self.mega = self.set_bool(mega)
        
    def stats_sum(self):
        return int(self.hp) + int(self.attack) + int(self.defense) + int(self.specialatk) + int(self.speed)
    
    def set_bool(self, type1):
        if type1 == "FALSE":
            return False
        elif type1 == "TRUE":
            return True

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

lines = pokedex.readlines()
lines = lines[1:]
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    lines[i] = lines[i].split(",")
    #print(lines[i])

pokemons = []
for i in lines:
    temp = pokemon(i[0], i[1], i[2], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[3])
    pokemons.append(temp)
    
nones = 0
for i in lines:
    if i[3] == '':
        nones +=1
print(nones)

highest_hp = pokemons[0]
for i in pokemons:
    if int(i.hp) > int(highest_hp.hp):
        highest_hp = i
print(highest_hp.name)

highest_defense = pokemons[0]
for i in pokemons:
    if not i.leg and not i.mega:
        if int(i.defense) > int(highest_defense.defense):
            highest_defense = i
print(highest_defense.name)

highest_stat = pokemons[0]
print("first one: ", highest_stat.name, highest_stat.leg, highest_stat.mega)
for i in pokemons:
    if not i.leg and not i.mega:
        stat_sum = i.stats_sum()
        current_sum = highest_stat.stats_sum()
        if stat_sum > current_sum:
            highest_stat = i
print(highest_stat.name)


my_dict = {"hi": 0}
maximum = "hi"
for i in pokemons:
    if i.leg:
        keys = list(my_dict.keys())
        if i.type1 in keys:
            my_dict[i.type1] += 1
        if i.type2 in keys:
            my_dict[i.type2] += 1
            if my_dict[i.type2] > my_dict[maximum]:
                maximum = i.type2


        if i.type1 not in keys:
            my_dict[i.type1] = 1
        if i.type2 not in keys and i.type2 != "":
            my_dict[i.type2] = 1

        if my_dict[i.type1] > my_dict[maximum]:
            maximum = i.type1
    
        
print(maximum, my_dict[maximum])


dictionary = {"hi": [0,1]}
avg_speed = "hi"
for i in pokemons:

    keys = list(dictionary.keys())
    if i.type1 in keys:
        dictionary[i.type1][1] += 1
        dictionary[i.type1][0] += int(i.speed)
    if i.type2 in keys:
        dictionary[i.type2][1] += 1
        dictionary[i.type2][0] += int(i.speed)


    if i.type1 not in keys:
        dictionary[i.type1] = [0,0]
        dictionary[i.type1][1] = 1
        dictionary[i.type1][0] = int(i.speed)
    if i.type2 not in keys and i.type2 != "":
        dictionary[i.type2] = [0,0]
        dictionary[i.type2][1] = 1
        dictionary[i.type2][0] = int(i.speed)
        
        
        
for i in (list(dictionary.keys())):
    #print(type(dictionary[i][0]))
    if (dictionary[i][0] / dictionary[i][1]) > (dictionary[avg_speed][0] / dictionary[avg_speed][1]):
        avg_speed = i
    
print(avg_speed, dictionary[avg_speed][0] / dictionary[avg_speed][1])


generations = {'1': [0, 1], '2': [0, 1], '3': [0, 1], '4': [0, 1], '5': [0, 1], '6': [0, 1], '7': [0, 1]}

for i in pokemons:
    generations[i.gen][0] += i.stats_sum()
    generations[i.gen][1] += 1
    
highest_avg_stat = "1"
for i in list(generations.keys()):
    print(i, generations[i][0] / generations[i][1])
    if generations[i][0] / generations[i][1] > generations[highest_avg_stat][0] / generations[highest_avg_stat][1]:
        highest_avg_stat = i
        
print(highest_avg_stat, 380.1684210526316 - 378.6967213114754)
        

# id, mega, mega count, non mega, non mega count
last_dict = {"1": [0,0,0,0]}
last_list = 0
    
duplicates = 0
'''
for i in range(len(pokemons)-1):
    for j in range(i+1, len(pokemons)):
        if pokemons[i].ident == pokemons[j].ident:
            duplicates += 1
            
            if pokemons[i].mega:
                the_mega = pokemons[i]
                non_mega = pokemons[j]
            else:
                the_mega = pokemons[j]
                non_mega = pokemons[i]
            last_list += (the_mega.stats_sum() - non_mega.stats_sum())
            
            
            last_dict["mega"][0] += the_mega.stats_sum()
            last_dict["mega"][1] += 1
            last_dict["non_mega"][0] += non_mega.stats_sum()
            last_dict["non_mega"][1] += 1
      
'''

for i in pokemons:
    if i.ident in list(last_dict.keys()):
        if i.mega:
            last_dict[i.ident][0] += i.stats_sum()
            last_dict[i.ident][1] += 1
        if not i.mega:
            last_dict[i.ident][2] += i.stats_sum()
            last_dict[i.ident][3] += 1
    else:
        last_dict[i.ident] = [0,0,0,0]
        if i.mega:
            last_dict[i.ident][0] = i.stats_sum()
            last_dict[i.ident][1] = 1
        if not i.mega:
            last_dict[i.ident][2] = i.stats_sum()
            last_dict[i.ident][3] = 1

real_last_dict = {}
for i in list(last_dict.keys()):
    val1=0
    if last_dict[i][1] != 0 and last_dict[i][0] != 0:
        val1 = last_dict[i][0]/last_dict[i][1]
        val2 = last_dict[i][2]/last_dict[i][3]
        temp = [val1, val2]
        real_last_dict[i] = temp
    
differences = 0
counter = 0
for i in list(real_last_dict.keys()):
    differences += (real_last_dict[i][0] - real_last_dict[i][1])
    counter +=1
    
    
print()
#print(differences, counter, differences / counter, len(real_last_dict), real_last_dict)

#print(round((last_dict["mega"][0] / last_dict["mega"][1]) - (last_dict["non_mega"][0] / last_dict["non_mega"][1])))

        
        
mega_sum = 0
mega_count = 0
non_mega_sum = 0
non_mega_count = 0
for i in pokemons:
    if i.mega:
        mega_count += 1
        mega_sum += i.stats_sum()
    elif not i.mega:
        non_mega_sum += i.stats_sum()
        non_mega_count += 1

print(mega_sum / mega_count - non_mega_sum / non_mega_count)