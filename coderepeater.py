import tkinter as tk
from tkinter import filedialog, messagebox

def executer():
    code = zone_code.get("1.0", tk.END)  # récupérer le code tapé
    try:
        nb = int(entry.get())  # récupérer le nombre de répétitions
    except ValueError:
        output.insert(tk.END, "⚠️ Entre un nombre valide pour les répétitions !\n")
        return

    output.insert(tk.END, f"--- Exécution {nb} fois ---\n")
    for i in range(nb):
        try:
            exec(code, {})
        except Exception as e:
            output.insert(tk.END, f"Erreur à l’exécution : {e}\n")
            break
    
    output.insert(tk.END, "✅ Exécution terminée\n")
    output.insert(tk.END, "---------------------------\n")

def enregistrer():
    fichier = filedialog.asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Fichiers Python", "*.py"), ("Tous les fichiers", "*.*")]
    )
    if fichier:
        with open(fichier, "w", encoding="utf-8") as f:
            f.write(zone_code.get("1.0", tk.END))
        messagebox.showinfo("Enregistrement", f"Script sauvegardé dans {fichier}")

def charger():
    fichier = filedialog.askopenfilename(
        filetypes=[("Fichiers Python", "*.py"), ("Tous les fichiers", "*.*")]
    )
    if fichier:
        with open(fichier, "r", encoding="utf-8") as f:
            code = f.read()
        zone_code.delete("1.0", tk.END)
        zone_code.insert(tk.END, code)
        messagebox.showinfo("Chargement", f"Script chargé depuis {fichier}")

# Fenêtre principale
root = tk.Tk()
root.title("Exécuteur de code")

# Zone pour écrire le code
label_code = tk.Label(root, text="Tape ton code Python ici :")
label_code.pack(pady=5)

zone_code = tk.Text(root, height=10, width=60)
zone_code.pack(pady=5)

# Champ pour le nombre de répétitions
label_nb = tk.Label(root, text="Nombre de répétitions :")
label_nb.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)
entry.insert(0, "1")  # valeur par défaut

# Boutons
frame_btns = tk.Frame(root)
frame_btns.pack(pady=10)

button_exec = tk.Button(frame_btns, text="Exécuter", command=executer)
button_exec.grid(row=0, column=0, padx=5)

button_save = tk.Button(frame_btns, text="Enregistrer", command=enregistrer)
button_save.grid(row=0, column=1, padx=5)

button_load = tk.Button(frame_btns, text="Charger", command=charger)
button_load.grid(row=0, column=2, padx=5)

# Zone de sortie
output = tk.Text(root, height=10, width=60)
output.pack(pady=5)

root.mainloop()
