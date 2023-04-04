from system import System

class Admin:
    def delete_account(email):
        System.delete_data(email)
        print(f"{email} was deleted")
