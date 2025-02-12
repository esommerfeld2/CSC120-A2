class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, descrip: str, 
                 ptype: str, 
                 hdc: int, 
                 mem: int, 
                 opersystem: str, 
                 year: int, 
                 cost: int):
        self.description = descrip
        self.processor_type= ptype
        self.hard_drive_capacity= hdc 
        self.memory= mem 
        self.operating_system= opersystem
        self.year_made= year 
        self.price= cost

    # What methods will you need?
    #Updating Price
    def update_price(self, cost:int):
        self.price = cost
    #Updatind OS
    def update_OS(self, opersystem:str):
        self.operating_system = opersystem