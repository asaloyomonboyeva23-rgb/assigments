class BusPass:
    transit_name = "Tashkent Metro"
    min_fare = 3
    total_passes = 0
    def __init__(self, holder, balance=0, rides=None):
        self.holder = holder 
        self.balance = balance
        if rides == None:
            rides = []      
        self.rides = rides
        BusPass.total_passes +=1
    def load_pass(self,amount):
        if amount > 0:
            self.balance += amount 
            self.rides.append(f"+{amount}")
            print(f"Loaded {amount}. Balance: {self.balance}")
    def take_ride (self,fare):
        if self.balance - fare >= BusPass.min_fare:
           self.balance -= fare
           self.rides.append(f"-{fare}")
           print(f"Charged {fare}. Balance: {self.balance}")
        else:
           print("Insufficient balance for ride")
    def display_pass(self):
        print(f"Holder: {self.holder}, Balance: {self.balance}, Transit: {BusPass.transit_name}")
    def show_rides(self):
        for ride in self.rides:
            print(ride)
pass1 = BusPass(holder="Jamshid", balance=10)
pass1.display_pass()
pass1.load_pass(20)
pass1.take_ride(5)
pass1.take_ride(8)
pass1.show_rides()
print(f"Total passes: {BusPass.total_passes}")



           
        
            
        
        
            
        
        

        
