"""13. Secure Login System (Decorators)
A web application wants to ensure that users are authenticated before accessing
sensitive functions. Create a decorator that checks whether the user is logged in before
allowing access to a function."""

def login(func):
    def check():
        if logged_in:
            func()
        else:
            print("Please login first")
    return check

logged_in = True

@login
def home():
    print("Hii Welcome")

home()
