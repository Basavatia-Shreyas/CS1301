#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.

def max_length(a_list):
    list_lengths = [len(i) for i in a_list]
    index = 0
    for i in range(len(list_lengths)):
        if(list_lengths[i] > list_lengths[index]):
            index = i
    return index
    
#Add your code here!
def check_plagiarism(file_one, file_two):
    first = open(file_one, "r")
    second = open(file_two, "r")
    
    first_file = first.read().split(" ")
    second_file = second.read().split(" ")
    #print(first_file, second_file)
    consec_words = []
    for i in range(len(first_file)):
        for j in range(len(second_file)):
            if(first_file[i] == second_file[j]):
                increment = 0
                temp_list = []
                while (first_file[i+increment] == second_file[j+increment]):
                    
                #print(i, j, increment, first_file[i+increment], second_file[j+increment], consec_words)
                
                    temp_list.append(first_file[i+increment])
                    increment += 1
                consec_words.append(temp_list)
    final = ""
    final_list = consec_words[max_length(consec_words)]
    if len(final_list) >= 5:
        
        for i in final_list:
            final += i + " "
        return final
    else:
        return False
                
                
    
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
#print(max_length([[1,4],[1,2,3], [1,2]]))
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))
