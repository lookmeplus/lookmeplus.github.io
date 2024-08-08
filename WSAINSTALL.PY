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
def i123q():
    question = "You Selected node is 123 cloud storage.Do you want to install WSA?"
    if messagebox.askyesno("Question", question):
        i123()
def i123():
    messagebox.showinfo("tips", "During the installation process, it may suddenly become unresponsive.")
    messagebox.showinfo("tips", "the file is 1,400,000,000 bytes, please wait patiently")
    command = "wget 'https://116-142-255-139.pd1.cjjd19.com:30443/download-cdn.cjjd19.com/123-578/50b2d7ce/1813124637-0/50b2d7ce9cebddfff8c7b4137db27242/c-m49?v=5&t=1723107138&s=172310713806bd6dbd004c7a81f312aec278c0bac9&r=4GUAK8&bzc=1&bzs=1812769958&filename=WSA.Msixbundle&x-mf-biz-cid=683162b3-1ab1-4b3e-9bb6-cc136e7a1ca7-6eaa77&auto_redirect=0&cache_type=1&xmfcid=697a72b5-8134-4807-8498-26857043191c-1-9eed82220' -o 'C:\WSA\WSA.Msixbundle'"
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
close_button =tk.Button(window, text="Install WSA NOW!(123Cloud storage)", font=("Arial", 8), width=30, height=2, command=i123q)
close_button.pack()

window.mainloop()
