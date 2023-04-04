import json

class System:
    def read_data():
        with open("data.txt", "r") as f:
            data = f.read()
            json_data = json.loads(data)

        f.close()
        return json_data
    
    def write_data(input_data):
        exsist_data = System.read_data()
        data_format = ["name","surname", "email", "password", "country"]
        new_data = {}
        new_data_header = {}
        i=0
        for data in input_data:
            new_data[f"{data_format[i]}"] = data
            i=i+1
        
        new_data_header[new_data["email"]]=new_data
        exsist_data.update(new_data_header)

        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()

    def search_data_by_email(email):
        exist_data = System.read_data()
        search_result = exist_data[email]
        return search_result

    def delete_data(email):
        exsist_data = System.read_data()
        exsist_data.pop(email)

        with open("data.txt", "w") as f:
            json.dump(exsist_data, f)
        f.close()

print(System.read_data())

System.delete_data("AB@")

print(System.read_data())

