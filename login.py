import tkinter as tk
import pickle
import hashlib
import tkinter.messagebox


class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        
        # username label
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        # password label
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        
        # website label
        self.website_label = tk.Label(root, text="Website:")
        self.website_label.pack()
        self.website_entry = tk.Entry(root)
        self.website_entry.pack()
        
        # save button
        self.save_button = tk.Button(root, text="Save Account", command=self.save_account)
        self.save_button.pack()
        
        # view account button
        self.view_button = tk.Button(root, text="View Account", command=self.view_account)
        self.view_button.pack()
        
        # accounts stored in a list
        self.accounts = []
        
        # unhashed accounts 
        self.unhashed_accounts = []
        
    def save_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        website = self.website_entry.get()
        
        unhashed = password
        # hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
        # storing the account in a dictionary and append it into the list
        account = {'username': username, 'password': hashed_password, 'website': website}
        unhashed_pw = {'username': username, 'password': unhashed, 'website': website}
        self.accounts.append(account)
        self.unhashed_accounts.append(unhashed_pw)
        
        # storing the dictionaries in a pickle file
        with open('unhashed.pickle', 'wb') as r:
            pickle.dump(self.unhashed_accounts, r)
        
        with open('accounts.pickle', 'wb') as f:
            pickle.dump(self.accounts, f)
        
        self.clear_entries()
    
    def view_account(self):
        try:
            with open('accounts.pickle', 'rb') as f:
                self.accounts = pickle.load(f)
            
            for account in self.accounts:
                tkinter.messagebox.showinfo("account saved", f"Username: {account['username']}, Website: {account['website']}, Password: ******** (hashed)")
            
            with open('unhashed.pickle', 'rb') as r:
                self.unhashed_accounts = pickle.load(r)
            
            for acc in self.unhashed_accounts:
                tkinter.messagebox.showinfo("account saved", f"Username: {acc['username']}, Website: {acc['website']}, Password: {acc['password']}")
            
        except FileNotFoundError:
            print("No accounts saved yet.")
    
    # clears the entries after saving
    def clear_entries(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.website_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()




