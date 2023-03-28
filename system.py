import json

class System:
    def read_data():
        with open("data.txt", "r") as f:
            data = f.read()
            json_data = json.loads(data)

        f.close()
        return json_data
    
    def write_data(username, password):
        exsist_data = System.read_data()
        #new_data = str(f"{username}:{password}")
        exsist_data[f"{username}"] = str(password)
        
        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()
        
    