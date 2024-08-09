import tkinter as tk
import os
from tkinter import messagebox
import subprocess

os.system("md C:\WSA")

def rm():
    os.system("rmdir /s /q C:\WSA")
    os.system("del /s /q C:\WSA")
def ask():
    question = "Do you want to install WSA?"
    if messagebox.askyesno("Question", question):
        installgithub()
def ctq():
    question = "You Selected node is microsoft.Do you want to install WSA?"
    if messagebox.askyesno("Question", question):
        ict()
def ict():
    messagebox.showinfo("tips", "During the installation process, it may suddenly become unresponsive.")
    command = "Start-BitsTransfer -Source 'http://tlu.dl.delivery.mp.microsoft.com/filestreamingservice/files/b997a699-594b-43db-ac2e-19a4c45b6af2?P1=1723214244&P2=404&P3=2&P4=h9JnFvLf5xP%2febASpNX4VAzV%2fzDoLZDlG7s4v5t1WAIEz4W0NFhkj1%2bQaYooAQ2eyPxZj5BNaka7sChQro1Nww%3d%3d' -Destination 'C:\WSA\WSA.Msixbundle'"
    result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)

    messagebox.showinfo("success", "Downloaded successfully")
    os.system("powershell Add-AppxPackage 'C:\WSA\WSA.Msixbundle'")
    messagebox.showinfo("success", "success, please look for Windows Subsystem for Android™ Settings in the 【Start】 menu.")
    question = "Do you want to delete file?"
    if messagebox.askyesno("Question", question):
        rm()

def installgithub():
    messagebox.showinfo("tips", "During the installation process, it may suddenly become unresponsive.")
    os.system("powershell Start-BitsTransfer -Source https://github.com/lookmeplus/lookmeplus.github.io/releases/download/000/WSA.Msixbundle -Destination 'C:\WSA\WSA.Msixbundle'")
    messagebox.showinfo("success", "Downloaded successfully")
    os.system("powershell Add-AppxPackage 'C:\WSA\WSA.Msixbundle'")
    messagebox.showinfo("success", "success, please look for Windows Subsystem for Android™ Settings in the 【Start】 menu.")
    question = "Do you want to delete file?"
    if messagebox.askyesno("Question", question):
        rm()
window = tk.Tk()
window.title("WSA Installer")
window.geometry("400x250")

label = tk.Label(window, text="WSA Installer", font=("Arial", 8), width=200, height=2)
label.pack()
label = tk.Label(window, text="download WSA.msixbundle", font=("Arial", 8), width=200, height=2)
label.pack()
label = tk.Label(window, text="powered by python", font=("Arial", 8), width=200, height=2)
label.pack()
label = tk.Label(window, text="The program by lookmeplus", font=("Arial", 8), width=200, height=2)
label.pack()
close_button = tk.Button(window, text="Install WSA NOW!(Github)", font=("Arial", 8), width=30, height=2, command=ask)
close_button.pack()
close_button =tk.Button(window, text="Install WSA NOW!(microsoft)", font=("Arial", 8), width=30, height=2, command=ctq)
close_button.pack()

window.mainloop()
