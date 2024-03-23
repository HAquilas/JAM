import tkinter as tk

current_player = 1  # Le joueur actuel, 1 ou 2
b = 0
c = 0

def ButtonClick(row, col):
    global current_player, b, c
    print("Position cliquée:", row, col)

    # Vérifier si la case est vide
    if buttons[row][col]['text'] == ' ':
        # Mettre à jour le texte du bouton en fonction du joueur actuel
        if current_player == 1:
            buttons[row][col]['text'] = "X"
            current_player = 2  # Passer au joueur 2
            b += 1
        else:
            buttons[row][col]['text'] = "O"
            current_player = 1  # Passer au joueur 1
            c += 1

def on_click(row, col):
    ButtonClick(row, col)

root = tk.Tk()

size = 5  # Taille de la table de jeu (4x4 pour 16 cases)
buttons = [[None] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        buttons[i][j] = tk.Button(root, text=' ', width=20, height=10,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=0, pady=0)

root.mainloop()