from tkinter import filedialog
from validate_email import validate_email
import tkinter as tk
import threading
import time

# Create the main window
root = tk.Tk()
email_count = 0
root.title("E-mail Checker")
root.geometry("500x500")

def t(name):
    n = threading.Thread(target=name)
    n.start()

def open_file():
    email_count = 0
    
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()
    filePath = tk.Label(root, text=file_path)
    filePath.place(x=150, y=20)

    def start():
        invalid = 0
        vaild = 0
        f = open("GOOD.txt", "w+")
        with open(file_path, 'r') as file:
            for line in file:
                mail = line.split(":")
                if validate_email(mail[0], verify=True, check_mx=True):
                    f.write(f"{line} \n")
                    vaild += 1
                    vaild_emails.config(text=f"Vaild E-mails : {vaild}")
                else:
                    invalid += 1
                    invaild_emails.config(text=f"Invaild E-mails : {invalid}")
        f.close()

    if file_path[-3::] == 'txt':
        selected.config(text="Ok, Ready")
        file_status = "Ok, Ready"
        # Read the contents of the selected file
        with open(file_path, 'r') as file:
            for line in file:
                email_count += 1
        all_emails = tk.Label(root, text=f"All E-mails : {email_count}")
        all_emails.place(x=200, y=150)

        bottom_button = tk.Button(root, text="Start", command=lambda : t(start))
        bottom_button.place(x=10, y=460)

# Create a button for opening a text file
open_button = tk.Button(root, text="File : ", command=open_file)
open_button.place(x=50, y=20)


# Create the labels
# selected Label
selected = tk.Label(root, text="No File Select !")
selected.place(x=180, y=480)

# vaild e-mail
vaild_emails = tk.Label(root, text="Vaild E-mails : 0")
vaild_emails.place(x=200, y=220)

# invaild e-mail
invaild_emails = tk.Label(root, text="Invaild E-mails : 0")
invaild_emails.place(x=200, y=290)

# show emails
all_emails = tk.Label(root, text=f"All E-mails : {email_count}")
all_emails.place(x=200, y=150) 

# timer
timer_label = tk.Label(root, text="")
timer_label.place(x=320, y=480)

# Start the timer
start_time = time.time()
def update_timer():
    # Update the timer label with the current time
    elapsed_time = time.time() - start_time
    timer_label.config(text="time: {:.2f} seconds".format(elapsed_time))
    root.after(1000, update_timer)

update_timer()

# Start the main loop
root.mainloop()