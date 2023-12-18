#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#Each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!


class Burrito:
    
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)
    def get_meat(self):
        return self.meat
    
    def get_to_go(self):
        return self.to_go
    
    def get_rice(self):
        return self.rice
    
    def get_beans(self):
        return self.beans
    
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
            self.meat = False
        else:
            self.meat = new_meat
    
    def set_to_go(self, new_to_go):
        if type(new_to_go) != bool:
            self.to_go = False
        else:
            self.to_go = new_to_go
   
    def set_rice(self, new_rice):
        valid_rice = ["brown", "white", False]

        if new_rice not in valid_rice:
            self.rice = False
        else:
            self.rice = new_rice
            
    def set_beans(self, new_beans):
        valid_beans = ["black", "pinto", False]
        if new_beans not in valid_beans:
            self.beans = False
        else:
            self.beans = new_beans
    
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
    


#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.

new_burrito = Burrito("spaghetti", True, True, False)
