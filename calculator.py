from tkinter import *
import tkinter.messagebox
import math

"""
Une calculatrice graphique avec interface Tkinter.
Permet d'effectuer des opérations mathématiques de base ainsi que des fonctions
comme le calcul de factorielle, racine carrée, logarithme, etc.
"""

# Création de la fenêtre principale
root = Tk()
root.geometry("700x500+300+300")
root.title("Calculatrice")


def btn1_clicked():
    """Gère le clic sur le bouton '1'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    """Gère le clic sur le bouton '2'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    """Gère le clic sur le bouton '3'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    """Gère le clic sur le bouton '4'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    """Gère le clic sur le bouton '5'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    """Gère le clic sur le bouton '6'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    """Gère le clic sur le bouton '7'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    """Gère le clic sur le bouton '8'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    """Gère le clic sur le bouton '9'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    """Gère le clic sur le bouton '0'"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def btnp_clicked():
    """Gère le clic sur le bouton '+'"""
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm_clicked():
    """Gère le clic sur le bouton '-'"""
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    """Gère le clic sur le bouton '*'"""
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    """Gère le clic sur le bouton '/'"""
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    """Efface l'affichage et réinitialise à '0'"""
    disp.delete(0, END)
    disp.insert(0, '0')


def pow_clicked():
    """Gère le clic sur le bouton puissance"""
    pos = len(disp.get())
    disp.insert(pos, '**')


def round_clicked():
    """Arrondit le nombre affiché à l'entier le plus proche"""
    try:
        ans = float(disp.get())
        ans = round(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")


def logarithm_clicked():
    """Calcule le logarithme base 10 du nombre affiché"""
    try:
        ans = float(disp.get())
        ans = math.log10(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")


def fact_clicked():
    """Calcule la factorielle du nombre affiché"""
    try:
        ans = int(float(disp.get()))
        if ans < 0:
            tkinter.messagebox.showerror("Erreur", "Le factoriel n'est défini que pour les nombres positifs")
            return
        ans = math.factorial(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except ValueError:
        tkinter.messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif")
    except OverflowError:
        tkinter.messagebox.showerror("Erreur", "Le résultat est trop grand")
    except Exception:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")


def sqr_clicked():
    """Calcule la racine carrée du nombre affiché"""
    try:
        ans = float(disp.get())
        ans = math.sqrt(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")


def dot_clicked():
    """Ajoute un point décimal"""
    pos = len(disp.get())
    disp.insert(pos, '.')


def pi_clicked():
    """Insère la valeur de π"""
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, str(math.pi))


def bl_clicked():
    """Insère une parenthèse ouvrante"""
    pos = len(disp.get())
    disp.insert(pos, '(')


def br_clicked():
    """Insère une parenthèse fermante"""
    pos = len(disp.get())
    disp.insert(pos, ')')


def del_clicked():
    """Supprime le dernier caractère saisi"""
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])


def btneq_clicked(*args):
    """Évalue l'expression mathématique saisie"""
    try:
        ans = disp.get()
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

    except:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")
        
def hex_clicked():
    """Convertit le nombre en hexadécimal"""
    try:
        ans = int(disp.get())
        ans = hex(ans)
        ans = ans[2::]
        disp.delete(0, END)
        disp.insert(0, ans)
        
    except:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")


def bin_clicked():
    """Convertit le nombre en binaire"""
    try:
        ans = int(disp.get())
        ans = bin(ans)
        ans = ans[2::]
        disp.delete(0, END)
        disp.insert(0, ans)
        
    except:
        tkinter.messagebox.showerror("Erreur", "Veuillez revérifier votre calcul")
        
def key_event(*args):
    """Gère les événements clavier"""
    if disp.get() == '0':
        disp.delete(0, END)

def validate_input(P):
    """Valide les caractères saisis"""
    valid_chars = "0123456789.+-*/()π "
    return all(char in valid_chars for char in P)

# Configuration de la validation des entrées
vcmd = (root.register(validate_input), '%P')
        
# Création et configuration du champ de saisie/affichage
disp = Entry(root, font="Verdana 20", fg="black", bg="#abbab1", bd=0, justify=RIGHT, insertbackground="#abbab1", cursor="arrow", validate="key", validatecommand=vcmd)
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind(".", key_event)
disp.insert(0, '0')                   # Valeur initiale
disp.focus_set()                      # Focus sur le champ de saisie
disp.pack(expand=TRUE, fill=BOTH)

# Création des rangées de boutons

# Première rangée
btnrow1 = Frame(root)
btnrow1.pack(expand=TRUE, fill=BOTH)

hex_btn = Button(btnrow1, text=" bin ", font="Segoe 10 bold", bd=0, command=bin_clicked, fg="white", bg="#333333")
hex_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pi_btn = Button(btnrow1, text="π", font="Segoe 18", bd=0, command=pi_clicked, fg="white", bg="#333333")
pi_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

fact_btn = Button(btnrow1, text=" x! ", font="Segoe 16", bd=0, command=fact_clicked, fg="white", bg="#333333")
fact_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23", bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", bd=0,  command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnp = Button(btnrow1, text="+", font="Segoe 18", bd=0, command=btnp_clicked, fg="yellow", bg="orange")
btnp.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Deuxième rangée
btnrow2 = Frame(root)
btnrow2.pack(expand=TRUE, fill=BOTH)

hex_btn = Button(btnrow2, text=" hex ", font="Segoe 10 bold", bd=0, command=hex_clicked, fg="white", bg="#333333")
hex_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(btnrow2, text=" √x ", font="Segoe 18", bd=0, command=sqr_clicked, fg="white", bg="#333333")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow2, text="round", font="Segoe 10 bold", bd=0, command=round_clicked, fg="white", bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(btnrow2, text="4", font="Segoe 23", bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(btnrow2, text="5", font="Segoe 23", bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(btnrow2, text="6", font="Segoe 23", bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(btnrow2, text="-", font="Segoe 25", bd=0, command=btnm_clicked, fg="yellow", bg="orange")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Troisième rangée
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow3, text=" • ", font="Segoe 20", bd=0, command=dot_clicked, fg="cyan", bg="blue")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 18", bd=0, command=logarithm_clicked, fg="white", bg="#333333")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 17", bd=0, command=pow_clicked, fg="white", bg="#333333")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23", bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23", bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Segoe 24", bd=0, command=btnml_clicked, fg="yellow", bg="orange")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Quatrième rangée
btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Segoe 21", bd=0, command=bl_clicked, fg="cyan", bg="blue")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Segoe 21", bd=0, command=br_clicked, fg="cyan", bg="blue")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", bd=0, command=btnc_clicked, fg="white", bg="black")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="⌫", font="Segoe 20", bd=0, command=del_clicked, fg="white", bg="black")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", bd=0, command=btneq_clicked, fg="yellow", bg="orange")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 28", bd=0, command=btnd_clicked, fg="yellow", bg="orange")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Lancement de la boucle principale
root.mainloop()