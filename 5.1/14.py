#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


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
    def get_cost(self):
        base = 5.0
        if self.meat in ["chicken", "pork", "tofu"]:
            base += 1.0
        elif self.meat == "steak":
            base += 1.0
        if self.extra_meat == True and self.meat != False:
            base += 1.0
        if self.guacamole:
            base += 0.75
        return base


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

