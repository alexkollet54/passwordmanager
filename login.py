import pickle






# storing all your user data
user_list = []


# class to create and store users
class User:
    def __init__(self, username, password, website):
        self.username = username
        self.password = password
        self.website = website
        

    # function to save user
    def save_user(self):
        user_list.append({
            "username": self.username,
            "password": self.password,
            "website": self.website,
        })

# function to create a new user
def create_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    website = input("Enter website: ")

    new_user = User(username, password, website)
    new_user.save_user()
    
    print(f"user data {username} for {website} saved!") 
    return new_user


# storing all your account data within a list in a pickle file
def save_file_user(user):
    try:
        with open("data.pickle", "wb") as file:
            pickle.dump(user_list, file,protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        print("Error during pickling object (Possibly unsupported):", e)

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
            


home = input('Type "add account" if you wish to save your account information: ')

def add_account():
    create_user()
    save_file_user(user_list)

def recursive():
    while home == 'add account':
        add_account()
        break

recursive()

inp = input('type "1" to view all your saved accounts, or "2" to save another account: ')


if inp == '1':
    heem = load_object('data.pickle')
    print(heem)

elif inp == '2':
    recursive()