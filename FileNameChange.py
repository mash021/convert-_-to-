import os
import tkinter as tk
from tkinter import filedialog
import time


root = tk.Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
directory = filedialog.askdirectory()
[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('_', ' ').lower()) for f in
 os.listdir(directory)]
time.sleep(5)
print("Done!")
