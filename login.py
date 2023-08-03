import pickle
import tkinter as tk
import tkinter.messagebox
 
def save_account():
    # Get the user input
    username = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    
    
    
    tkinter.messagebox.showinfo("Account saved", "Account is Saved!" )

    # Check if the username and password are not empty strings
    if not username or not password:
        tkinter.messagebox.showerror("Error", "Please enter a username and password")
        return

    # Save the account information
    try:
        with open("data.pickle", "wb") as file:
            pickle.dump({
            "username": username,
            "password": password,
            "website": website,
        }, file, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        tkinter.messagebox.showerror("Error", e)
    
    tkinter.messagebox.showinfo("Account saved",f"Username: {username}" + 
                                f"Password: {password}" + 
                                f"Website: {website}" )
        
def view_accounts():
    # Load the saved account information
    try:
        with open("data.pickle", "rb") as file:
            accounts = pickle.load(file)
    except Exception as e:
        tkinter.messagebox.showerror("Error (unpickle)", e)
        
        
    # Display the saved account information
    for account in accounts:
        tkinter.messagebox.showinfo("Account saved",
                                  f"Username: {int(account['username'])}" +
                                  f"Password: {account['password']}" +
                                  f"Website: {account['website']}")



# Create a Tkinter window
root = tk.Tk()
root.title("Account Manager")


# Create a text box to collect user input
username_entry = tk.Entry(root)
password_entry = tk.Entry(root)
website_entry = tk.Entry(root)


# Create buttons to save the account information and view the saved accounts
save_button = tk.Button(root, text="Save Account", command=save_account)
view_button = tk.Button(root, text="View Accounts", command=view_accounts)


# Pack the widgets into the window
username_entry.pack()
password_entry.pack()
website_entry.pack()
save_button.pack()
view_button.pack()


# Start the Tkinter loop
root.mainloop()










