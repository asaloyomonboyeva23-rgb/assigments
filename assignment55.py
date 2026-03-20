from abc import ABC,abstractmethod
class Validator(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def validate(self, value):
        pass
    
    def check(self, value):
        result = self.validate(value)
        status = 'PASS' if result else 'FAIL'
        print(f"[{status}] {self.name}: {value}")
        return result
    
class LengthValidator(Validator):
    def __init__(self,min_len ,max_len):
        name=  f"Length({min_len}-{max_len})"
        super().__init__(name)
        self.min_len = min_len
        self.max_len = max_len
        
    def validate(self, value):
        result =self.min_len <= len(value) <= self.max_len
        return result
    
class ContainsDigitValidator(Validator):
    def __init__(self):
        super().__init__("ContainsDigit")
        
    def validate(self, value):
        for character in value:
            result = character.isdigit()
        return result

class NoSpacesValidator(Validator):
    def __init__(self):
        super().__init__("NoSpaces")
    def validate(self,value):
        result = " " not in value 
        return result
       
class StartsWithUpperValidator:
    def __init__(self):
       self.name =("StartsWithUpper")
    def validate(self, value):
        result= len(value) > 0 and value[0].isupper()
        return result
    
    def check(self, value):
        result = self.validate(value)
        status = 'PASS' if result else 'FAIL'
        print(f"[{status}] {self.name}: {value}")
        return result 
    
    
class ValidationReport:
    def __init__(self):
       self.entries =[]
    def add(self, validator_name, value, passed):
        result =((validator_name, value, passed))
        self.entries.append(result)
        return result 
    
    def summary(self):
        total = len(self.entries)
        total_passed =0
        for valitor_name , value, passed  in self.entries:
            total_passed += passed 
        total_failed = total - total_passed
        print(f'"Total: {total}, Passed: {total_passed}, Failed: {total_failed}')
        
class  FormField:
    def __init__(self,field_name):
        self.field_name =field_name
        self.validators = [] 
        self.report = ValidationReport()
        
    def add_validator(self, validator):
        self.validators.append(validator)
    def validate(self, value):
        print(f'Validating {self.field_name}: "{value}"')
        all_passed = True
        for validator in self.validators:
            result = validator.check(value)
            self.report.add(validator.name , value , result )
        if not result:
            all_passed= False 
        return all_passed
    def show_report(self):
        print(f'--- Report for {self.field_name} ---')
        result = self.report.summary()
        return result
        
username_field = FormField('username')
username_field.add_validator(LengthValidator(3, 15))
username_field.add_validator(NoSpacesValidator())
username_field.add_validator(ContainsDigitValidator())
username_field.add_validator(StartsWithUpperValidator())

valid1 = username_field.validate('Admin1')
print(f'Valid: {valid1}')
print()

valid2 = username_field.validate('no')
print(f'Valid: {valid2}')
print()

valid3 = username_field.validate('has space')
print(f'Valid: {valid3}')
print()

username_field.show_report()

try:
    v = Validator('test')
except TypeError:
    print('Cannot instantiate abstract class')

        
                  
          
     
