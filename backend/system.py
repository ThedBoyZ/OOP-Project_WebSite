import json

class System:
    @staticmethod
    def read_data():
        with open("data.txt", "r") as f:
            data = f.read()
            json_data = json.loads(data)
        return json_data
    
    @staticmethod
    def write_data(email, user_data):
        exist_data = System.read_data()
        new_data_header = {}
        new_data_header[email] = user_data
        exist_data.update(new_data_header)

        with open("data.txt", "w") as f:
            json.dump(exist_data, f)

    @staticmethod
    def delete_data(email):
        exsist_data = System.read_data()
        exsist_data.pop(email)

        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()

    @staticmethod
    def write_purchased(email, price):
        exsist_data = System.read_data()[email]
        exsist_data["purchased"] = price

        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()

    @staticmethod
    def reset_purchased(email):
        exsist_data = System.read_data()[email]
        exsist_data["purchased"] = 0
        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()

    @staticmethod
    def get_purchased(email):
        exsist_data = System.read_data()[email]
        print(exsist_data["purchased"])
        return exsist_data["purchased"]