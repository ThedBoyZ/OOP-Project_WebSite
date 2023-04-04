import json

class Country:
    def __init__(self):
        with open("countries.json") as f:
            self.data = json.load(f)
        self.__country_dict = {d["name"] : {"code": d["code"]} for d in self.data["countries"]}

    @property
    def country_dict(self):
        return self.__country_dict
    
    def get_code(self, name):
        if name in self.__country_dict:
            return self.__country_dict[name]["code"]
        else:
            return None

    def add_country(self, name, code):
        if name in self.__country_dict:
            raise ValueError("Country already exists")
        else:
            self.__country_dict[name] = {"code": code}
            self.data["countries"].append({"code": code ,"name": name})

            with open("countries.json", "w") as f:
                json.dump(self.data, f)

    def remove_country(self, name):
        if name not in self.__country_dict:
            raise ValueError("Country does not exist")
        else:
            del self.__country_dict[name]
            for country in self.data["countries"]:
                if country["name"] == name:
                    self.data["countries"].remove(country)

            with open("countries.json", "w") as f:
                json.dump(self.data, f)
    
    def __str__(self):
        output = ""
        for name, code in self.__country_dict.items():
            output += f"{name} ({code['code']})\n"
        return output


if __name__ == "__main__":
    country = Country()
    # country.add_country("Zzzz", "+67")
    # country.remove_country("Zzzz")
    print(country)
    print(country.country_dict)
