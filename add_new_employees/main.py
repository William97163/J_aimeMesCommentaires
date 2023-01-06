""" Voici la documentation du fichier main.py, ici vous retrouverez

* Toutes les fonctions de ce fichier 
* Les détails les expliquants   

Ce script a pour fonction principale de faire apparaître une application permettant d'insérer un employé par son nom, son prénom,
sa date d'embauche ainsi que son poste

"""

from tkinter import *
from tkinter import ttk
import pandas as pd
import csv


data = pd.read_csv("../datas/employes.csv")
print(data)

v = open("../postes.txt", "r").read()
v = v.split()


def btn_clicked():
    """Cette fonction permet d'ajouter un employé dans le fichier : "liste_employes.txt"
    """
    name = entry5.get()
    surname = entry4.get()
    hire_day = entry3.get()
    hire_mounth = entry2.get()
    hire_year = entry1.get()
    hire = (str(hire_day) + "/" + str(hire_mounth) + "/" + str(hire_year))
    fonction = entry0.get()

    if str(name) == "" or str(surname) == "" or str(hire_day) == "" or str(hire_mounth) == "" or str(hire_year) == "" or str(fonction) == "":
        error_popup()
    else:
        with open('Script/employes.csv', 'a', newline='') as fichiercsv:
            writer = csv.writer(fichiercsv)
            writer.writerow(
                [name.upper(), surname.title(), hire, fonction.title()])
        new_data = pd.read_csv("Script/employes.csv")
        print(new_data)
        validate_popup()


def error_popup():
    """Cette fonction fait apparaitre une popup si l'utilisateur oubli de rentrer un argument ou plusieurs arguments
    
    Args:
        Pas d'arguments

    Returns:
        Arguments Missing.
    """
    top = Toplevel(window)
    top.geometry("250x80")
    top.title("Error")
    Label(top, text="Arguments Missing").place(x=80, y=30)


def validate_popup():
    """Cette fonction fait apparaitre une popup si l'utilisateur rentre tous les arguments demandés
    
    Args:
        Pas de paramètre
        
    Returns:
        Task successful.
    """
    top = Toplevel(window)
    top.geometry("250x80")
    top.title("validate")
    Label(top, text="Task successful").place(x=80, y=30)


window = Tk()

window.geometry("917x688")
window.configure(bg="#0010a4")
canvas = Canvas(
    window,
    bg="#0010a4",
    height=688,
    width=917,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    461.5, 170.0,
    text="Veuillez entrez le nouvel employé",
    fill="#4356ff",
    font=("Inter-Light", int(20.0)))

canvas.create_text(
    467.5, 117.0,
    text="Bienvenue sur l'application",
    fill="#4356ff",
    font=("Inter-Light", int(40.0)))

canvas.create_text(
    377.5, 220.5,
    text="Nom",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

entry5_img = PhotoImage(file=f"../img/img_textBox5.png")
entry5_bg = canvas.create_image(
    377.0, 251.0,
    image=entry5_img)

entry5 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry5.place(
    x=337, y=241,
    width=80,
    height=18)

canvas.create_text(
    558.5, 222.5,
    text="Prénom",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

entry4_img = PhotoImage(file=f"../img/img_textBox4.png")
entry4_bg = canvas.create_image(
    559.0, 251.0,
    image=entry4_img)

entry4 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry4.place(
    x=519, y=241,
    width=80,
    height=18)

canvas.create_text(
    472.5, 316.0,
    text="Date d'embauche(jj/mm/aaaa)",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

entry3_img = PhotoImage(file=f"../img/img_textBox3.png")
entry3_bg = canvas.create_image(
    337.0, 358.0,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry3.place(
    x=322, y=348,
    width=30,
    height=18)

entry2_img = PhotoImage(file=f"../img/img_textBox2.png")
entry2_bg = canvas.create_image(
    465.0, 358.0,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry2.place(
    x=450, y=348,
    width=30,
    height=18)

canvas.create_text(
    408.5, 361.0,
    text="/",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

entry1_img = PhotoImage(file=f"../img/img_textBox1.png")
entry1_bg = canvas.create_image(
    593.0, 358.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0)

entry1.place(
    x=578, y=348,
    width=30,
    height=18)

canvas.create_text(
    536.5, 361.0,
    text="/",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

canvas.create_text(
    465.0, 412.0,
    text="Poste",
    fill="#ffffff",
    font=("Inter-Light", int(20.0)))

entry0_img = PhotoImage(file=f"../img/img_textBox0.png")
entry0_bg = canvas.create_image(
    465.0, 461.0,
    image=entry0_img)

entry0 = ttk.Combobox(window, values=v)
entry0.current(0)
entry0.pack()

entry0.place(
    x=425, y=451,
    width=80,
    height=18)

img0 = PhotoImage(file=f"../img/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=389, y=499,
    width=148,
    height=25)

window.resizable(False, False)
window.mainloop()
