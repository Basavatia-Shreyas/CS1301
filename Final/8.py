#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

names_file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

lines = names_file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n","").split(",")

print(len(lines))
#print(lines)

total = 0
for i in lines:
    total += int(i[1])
print(total)

boy_z_names = 0
for i in lines:
    if(i[0][0] == "Z" and i[2] == "Boy"):
        boy_z_names += 1

print(boy_z_names)

girls_names = []
for i in lines:
    if(i[2] == "Girl" and i[0][0] == "Q"):
        girls_names.append([i[0], i[1]])
print(girls_names)

num_vowels = 0
vowels = "aeiou"
for i in lines:
    if(i[0][0].lower() in vowels and i[0][-1] in vowels):
        num_vowels += int(i[1])
print(num_vowels)

letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
for i in lines:
    letters[i[0][0].lower()] += int(i[1])
print(letters)
print(max(letters.values()))

my_dict = {}
for i in lines:
    if i[0] in list(my_dict.keys()):
        my_dict[i[0]] += int(i[1])
    else:
        my_dict[i[0]] = int(i[1])
maximum = max(my_dict.values())
for i in list(my_dict.keys()):
    if my_dict[i] == maximum:
        print(i)
print(max(my_dict.values()))


min_difference = [10000000000, lines[0]]
for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        if lines[i][0] == lines[j][0]:
            temp_diff = abs(int(lines[i][1])-int(lines[j][1]))
            if(temp_diff < min_difference[0]):
                min_difference[0] = temp_diff
                min_difference[1] = lines[i]
                
print(min_difference)