#Copy your Burrito class from the last exercise. Below,
#We've given you three additional classes named "Meat",  
#"Rice" and "Beans." We've gone ahead and built getters
#and setters in these classes to check if the incoming
#values are valid, so you'll be able to remove those
#from your original code.
#
#First, edit the constructor of your Burrito class.
#Instead of calling setters to set the values of the
#attributes self.meat, self.rice, and self.beans, it
#should instead create new instances of Meat, Rice, and
#Beans. The arguments to these new instances should be
#the same as the arguments you were sending to the
#setters previously (e.g. self.rice = Rice("brown")
#instead of set_rice("brown")).
#
#Second, modify your getters and setters from your
#original code so that they still return the same value
#as before. get_rice(), for example, should still
#return "brown" for brown rice, False for no rice, etc.
#instead of returning the instance of Rice.
#
#Third, make sure that your get_cost function still
#works when you're done changing your code.
#
#Hint: When you're done, creating a new instance of
#Burrito with Burrito("pork", True, "brown", "pinto")
#should still work to create a new Burrito. The only
#thing changing is the internal reasoning of the
#Burrito class.
#
#Hint 2: Notice that the classes Meat, Beans, and Rice
#already contain the code to validate whether input is
#valid. So, your setters in the Burrito class no
#longer need to worry about that -- they can just pass
#their input to the set_value() methods for those
#classes.
#
#Hint 3: This exercise requires very little actual
#coding: you'll only write nine lines of new code, and
#those nine lines all replace existing lines of code
#in the constructor, getters, and setters of Burrito.
#
#You should not need to modify the code below.

class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            

            
#Add and modify your code here!
class Burrito:
    
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
        
    def get_meat(self):
        return self.meat.get_value()
    
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice.get_value()
    
    def get_beans(self):
        return self.beans.get_value()
    
    def get_extra_meat(self):
        return self.extra_meat
    
    def get_guacamole(self):
        return self.guacamole
    
    def get_cheese(self):
        return self.cheese
    
    def get_pico(self):
        return self.pico
    
    def get_corn(self):
        return self.corn
    
    def set_meat(self, new_meat):
        valid_meats = ["chicken", "pork", "steak", "tofu"]

        if not new_meat in valid_meats:
            self.meat.set_value(False)
        else:
            self.meat.set_value(new_meat)
    
    def set_to_go(self, new_to_go):
        if type(new_to_go) != bool:
            self.to_go = False
        else:
            self.to_go = new_to_go
   
    def set_rice(self, new_rice):
        valid_rice = ["brown", "white", False]

        if new_rice not in valid_rice:
            self.rice.set_value(False)
        else:
            self.rice.set_value(new_rice)
            
    def set_beans(self, new_beans):
        valid_beans = ["black", "pinto", False]
        if new_beans not in valid_beans:
            self.beans.set_value(False)
        else:
            self.beans.set_value(new_beans)
    
    def set_extra_meat(self, new_to_go):
        if type(new_to_go) != bool:
            self.extra_meat = False
        else:
            self.extra_meat = new_to_go
    
    def set_guacamole(self, new_to_go):
        if type(new_to_go) != bool:
            self.guacamole = False
        else:
            self.guacamole = new_to_go
            
    def set_cheese(self, new_to_go):
        if type(new_to_go) != bool:
            self.cheese = False
        else:
            self.cheese = new_to_go
            
    def set_pico(self, new_to_go):
        if type(new_to_go) != bool:
            self.pico = False
        else:
            self.pico = new_to_go
            
    def set_corn(self, new_to_go):
        if type(new_to_go) != bool:
            self.corn = False
        else:
            self.corn = new_to_go
    def get_cost(self):
        base = 5.0
        if self.meat.get_value() in ["chicken", "pork", "tofu"]:
            base += 1.0
        elif self.meat.get_value() == "steak":
            base += 1.5
        if self.extra_meat == True and self.meat.get_value() != False:
            base += 1.0
        if self.guacamole:
            base += 0.75
        return base


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs. Remember though, the results
#of this code should be the same as the previous problem:
#what should be different is how it works behind the scenes.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

