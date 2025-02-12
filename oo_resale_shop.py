from computer import Computer
class ResaleShop:

    # What attributes will it need?
    inventory : list = []
    computer : dict
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, comp : dict, invent: list = []):
        self. computer = comp
        self.inventory = invent
        
    # What methods will you need?
    def buy_comp(self, comp : dict):
        #Call inventory.append() to add computer to inventory
        self.inventory.append(comp)

    #Checks inventory
    def inventory_check(self):
        if self.inventory: #if there is an inventory
            for comp in self.inventory:
                print(f"{comp.description}") #List the description of Computer
        else:
            print("Nothing in inventory")

    #Updates inventory when computer is sold
    def sell_comp(self, comp : dict):
        for i, item in enumerate(self.inventory): #For each iteam in self.inventory
            if item == comp: #See if that item is the computer we want
                sold_comp = self.inventory.pop(i)  # Remove and get the computer from inventory
                print(f"Item {sold_comp.description} sold!")
                return
        print("Computer not found in inventory.")

def main():
    #Setting up my Computer
    myComp: Computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    #Setting up my Shop
    myShop: ResaleShop = ResaleShop(myComp)

    #Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    print("****")

    #Buy the Computer
    print("Buying", myComp.description)
    print("Adding to inventory...")
    myShop.buy_comp(myComp)
    print("Done.\n")

    #Check the inventory
    print("Checking inventory...")
    myShop.inventory_check()
    print("Done.\n")

    #Refurbish my Computer
    #Updating Price
    print("Changing Price")
    print("Updating inventory...")
    myComp.update_price(3000)
    print("New price is", myComp.price)
    print("Done.\n")

    #Udapting OS
    print("Refurbishing Item:", myComp.description, ", updating OS")
    print("Updating inventory...")
    myComp.update_OS("New")
    print("New OS is", myComp.operating_system)
    print("Done.\n")

    #Check the inventory
    print("Checking inventory...")
    myShop.inventory_check()
    print("Done.\n")
    
    # Now let's sell it!
    print("Selling Item:", myComp.description)
    myShop.sell_comp(myComp)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    myShop.inventory_check()
    print("Done.\n")

if __name__ == "__main__": main()
