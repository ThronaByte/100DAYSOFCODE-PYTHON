class User:
    def __init__(self, name):
        self.name = name
        self.is_log_in = False

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_log_in==f"{True}":
            function(args[0])
    return wrapper

@is_authenticated
def blog(user):
    print(f"This is {user.name}'s blog")

new_user = User("Daniel")
var = new_user.is_log_in == True
blog(new_user)