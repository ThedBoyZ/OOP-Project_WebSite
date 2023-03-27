import json

class System:
    def read_data():
        with open("data.txt", "r") as f:
            data = f.read()
            dict_data = json.loads(data)

        f.close()
        print(list(dict_data.keys()))
        return dict_data

System.read_data()