import json

class System:
    def read_data():
        with open("data.txt", "r") as f:
            data = f.read()
            dict_data = json.loads(data)

        f.close()

        return dict_data