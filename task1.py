import tkinter as tk
from time import strftime


# Create the main window
root = tk.Tk()
root.title("Digital Clock")


# Define the function to update the time
def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# Create and configure the label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='Black', foreground='Blue')
label.pack(anchor='center')


# Call the time function to initiate the clock
time()


# Run the main loop
root.mainloop()






