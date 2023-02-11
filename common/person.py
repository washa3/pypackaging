import random 

class Person: 
    
    def __init__(self): 
        print("I'm an Person")
    
    def height(self):
        return random.randint(1,100000)

def random_id():
    return random.randint(1,10)