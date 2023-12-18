#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force_from_file(forces):
    
    file = open(forces, "r")
    lines = file.readlines()
    #print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        for j in range(len(lines[i])):
            lines[i][j] = lines[i][j].strip()
    #print(lines)
    #We know from the directions that our goal is to find the
    #total horizontal and total vertical forces. So, let's
    #create variables to hold those values so we can add to
    #them as we go along:
    total_horizontal = 0
    total_vertical = 0
    
    #Now, let's iterate through each force in the forces:
    for i in lines:
        
        #To make our code easier to read, let's pull the
        #magnitude and angle out from the tuple:
        magnitude = int(i[0])
        #print(magnitude)
        angle = int(i[1])
        #print(angle)
        
        #The directions told us we need to convert our
        #angles to radians to use Python's trignometric
        #functions:
        angle = radians(angle)
        
        #Now, the horizontal component is the magnitude
        #times the cosine of the angle:
        horizontal = magnitude * cos(angle)
        
        #And the vertical component is the magnitude times
        #the sine of the angle:
        vertical = magnitude * sin(angle)
        
        #Now that we've calculated the horizontal and
        #vertical components, let's add those to our
        #running tallies:
        total_horizontal += horizontal
        total_vertical += vertical
    
    #The net magnitude is the hypotenuse of the triangle
    #with these two components as their legs. So, we can
    #calculate the net magnitude using the Pythagorean
    #theorem:
    net_magnitude = sqrt(total_horizontal**2 + total_vertical**2)
    
    #Then as instructed, we round it to one decimal point:
    net_magnitude = round(net_magnitude, 1)
    
    #Next, we need to calculate the angle. As directed, we
    #do this with the atan2 function from Python's math
    #library, which takes the vertical and horizontal
    #components as arguments:
    net_angle = atan2(total_vertical, total_horizontal)
    
    #Then, we convert this back to degrees:
    net_angle = degrees(net_angle)
    
    #And round it to one decimal point as instructed:
    net_angle = round(net_angle, 1)
    
    #Last, we return the tuple of the madnitude and angle:
    file.close()
    return (net_magnitude, net_angle)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))




