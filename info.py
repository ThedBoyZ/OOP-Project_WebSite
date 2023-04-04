from dataclasses import dataclass
from datetime import date

@dataclass
class ContractInfo():
    title : str
    name : str
    surname : str
    country : str
    mobile_number : str
    email : str
 
@dataclass
class TravelerInfo():
    type_person : str
    title : str
    gender : str
    name : str
    surname : str
    dob : date
    nationality : str
    baggage_weight : str

@dataclass
class Country():
    name : str
    calling_code : str

class CountryCollection:
    def __init__(self):
        self.countries = []
    
    def add_country(self, name, calling_code):
        country = Country(name, calling_code)
        self.countries.append(country)

    def get_calling_code(self, name):
        for country in self.countries:
            if country.name == name:
                return country.calling_code
        return None
        

if __name__ == '__main__':
    th = Country("Thailand", "+66")
    c1 = ContractInfo("Mr.", "Tanathip", "Pona", th, "0800687960", "65010443@kmitl.ac.th")
    print(c1.country.name)          # Thailand
    print(c1.country.calling_code)  # +66

    t1 = TravelerInfo("Child", "", "Male", "Peter", "Parker", date(2007, 10, 14), "Thailand", "20")
    print(t1.dob)   # 2007-10-14

    countries = CountryCollection()
    countries.add_country("Thailand", "+66")
    countries.add_country("Japan", "+81")

    c2 = ContractInfo("Mr.", "Tanathip", "Pona", countries.countries[0], "0800687960", "65010443@kmitl.ac.th")
    print(c2.country.name)          # Thailand
    print(c2.country.calling_code)  # +66