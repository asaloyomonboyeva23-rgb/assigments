from abc import ABC , abstractmethod 

class Member(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def monthly_fee(self):
        ...
    
class Basic(Member):
    def monthly_fee(self):
        return 200_000
    
class Premium(Member):
    def monthly_fee(self):
        return 500_000
    
class Vip(Member):
    def monthly_fee(self):
        return 1_000_000
    
class Storage(ABC):
    @abstractmethod
    def save(self, members):
        ...
            
class FileStorage(Storage):
    def save(self, members):
        for m in members:
            print(f"[FILE] {m.name},{m.monthly_fee()}")
        
        
class Notifier(ABC):
    @abstractmethod
    def notify(self , members) :
        ...
        
class EmailNotifier(Notifier):
    def notify(self, members):
       for m in members:
            print(f"[EMAIL → {m.name}] Your fee: {m.monthly_fee()} $")
 
        
        
class GymManager:
    def __init__(self):
        self.members = []   # list of (name, plan)

    def add(self, name):
        self.members.append((name))
        
    def run(self,storage:Storage, notifier:Notifier):
            storage.save(self.members)
            notifier.notify(self.members)
        
gym = GymManager()
gym.add(Basic("Frodo"))
gym.add(Premium("Aragorn"))
gym.add(Vip("Legolas"))

gym.run(FileStorage(), EmailNotifier())

 