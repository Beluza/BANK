import random 

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare == True:
            self.value = self.orginal_value * 1.25
        else:
            self.value = self.orginal_value

        if self.is_clean == True:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
      
        

class one_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness":1.52,
            "mass":3.56
            }
        super().__init__(**data)



class two_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness":1.85,
            "mass":7.12
            }
        super().__init__(**data)



class five_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness":1.77,
            "mass":3.25
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour


class ten_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness":1.85,
            "mass":6.50
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour


class twenty_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness":1.7,
            "mass":5.00
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour


class fifty_pence(Coin):
    def __init__(self):
        data = {
            "orginal_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness":1.78,
            "mass":8.00
            }
        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour



class one_pound(Coin):
    def __init__(self):
        data = {
            "orginal_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass":9.5
            }
        super().__init__(**data)

    
class two_pound(Coin):
    def __init__(self):
        data = {
            "orginal_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness":2.50,
            "mass":12.00
            }
        super().__init__(**data)


