from contextlib import contextmanager
from dataclasses import dataclass,field
class PetError(Exception):
    pass
@dataclass 
class Pet:
    name:str
    species:str
    age:int
    _status :str = field(init=False ,default="NEW")
    
    def __post_init__(self):
        if self.age <=0:
            raise PetError(f'invalid age for {self.name }')   
        
    @property
    def is_senior(self):
        if self.age <= 8:
            return False
        return True
    def __str__(self):
        return f'{self.name} ({self.species}, {self.age}yrs) [{self._status}]'
    def __lt__(self, other ):
        return self.age < other.age
            
class AdoptionChecker: 
    
    def __init__(self,pets, allowed):
        self.pets = pets
        self.allowed = allowed
        self.current_index =0
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current_index >= len(self.pets):
            raise StopIteration
        
        pet =self.pets[self.current_index]
        if  pet.species in self.allowed :
                pet._status = "ADOPTABLE"
        else:
            pet._status = "ON HOLD"
            
        self.current_index+=1
        return pet    
def adoption_report(checker):
    adoptable=0
    on_hold= 0
    for pet in checker:
        if pet._status == "ADOPTABLE":
            adoptable+=1
            yield pet
        elif pet._status == "ON HOLD":
            on_hold+=1
            yield pet
    yield f"Report: {adoptable} adoptable, {on_hold} on hold"
@contextmanager 
def shelter_session(name):
       print(f' >>> Intake: {name}') 
       pets_list =[]
       try:
           yield pets_list
       except PetError as e:
           print(f'!!! Error: {e}.')
       finally:
           print(f'<<< Done: {name} ({len(pets_list)} pets)')   
       
       
with shelter_session("Monday Batch") as pets:
    pets.append(Pet("Bella", "Dog", 3))
    pets.append(Pet("Milo", "Cat", 7))
    pets.append(Pet("Koko", "Parrot", 2))

    for line in adoption_report(AdoptionChecker(pets, ("Dog", "Cat"))):
        print(line)

    print(pets[0] < pets[1])

print()

with shelter_session("Tuesday Batch") as pets:
    pets.append(Pet("Rex", "Dog", -1))
  
        
            
            
       
        
        