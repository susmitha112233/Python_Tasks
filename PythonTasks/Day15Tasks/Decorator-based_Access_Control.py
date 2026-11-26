"""8. Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary"""



roles = {"Ravi": "admin", "Sita": "user"}

def check_role(func):
    def wrapper(name):
        if roles.get(name) == "admin":
            return func(name)
        else:
            print("Access denied")
    return wrapper

@check_role
def view_data(name):
    print(name, "can view data")

@check_role
def delete_data(name):
    print(name, "can delete data")

view_data("Ravi")
delete_data("Sita")
