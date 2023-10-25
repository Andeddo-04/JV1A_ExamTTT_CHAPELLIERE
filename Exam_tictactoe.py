my_tab = []

# ***********************************************************************************
# ***********************************************************************************

def grille(tab:list)->list:
    
    for i in range(9):
        tab.append("_")
        
    return tab

# print(grille(my_tab))

# ***********************************************************************************
# ***********************************************************************************

def turn_j1(tab:list):
    
    symbole_j1 = "X"
    
    j1 = int(input("Joueur 1, où voulez vous jouer ? (1/2/3/4/5/6/7/8/9) "))
    
    tab[j1] = symbole_j1
    
    return tab,"\n"

# print(turn_j1(my_tab))

# --------------------------

def turn_j2(tab:list):
    
    symbole_j2 = "O"
    
    j2 = int(input("Joueur 2, où voulez vous jouer ? (1/2/3/4/5/6/7/8/9) "))
    
    tab[j2] = symbole_j2
    
    return tab,"\n"

# print(turn_j2(my_tab))

# ***********************************************************************************
# ***********************************************************************************

def test_win(tab:list):
    
    win_j1 = False
    win_j2 = False
    
    while win_j1 and win_j2 == False:
    
        # ---------------------------------------------------
        # On test si une ligne contient 3 fois le meme symbole
        # ---------------------------------------------------
        if tab[0] == tab[1] and tab[0] == tab[2]:
            
            if tab[0] == "X":
                win_j1 = True
            
            if tab[0] == "O":
                win_j2 = True
        
        if tab[3] == tab[4] and tab[3] == tab[5]:
            
            if tab[3] == "X":
                win_j1 = True
            
            if tab[3] == "O":
                win_j2 = True
        
        if tab[6] == tab[7] and tab[6] == tab[8]:
            
            if tab[6] == "X":
                win_j1 = True
            
            if tab[6] == "O":
                win_j2 = True
        
        # ------------------------------------------------------
        # On test si une colonne contient 3 fois le meme symbole
        # ------------------------------------------------------
        if tab[0] == tab[3] and tab[0] == tab[6]:
            
            if tab[0] == "X":
                win_j1 = True
            
            if tab[0] == "O":
                win_j2 = True
        
        if tab[1] == tab[4] and tab[1] == tab[7]:
            
            if tab[1] == "X":
                win_j1 = True
            
            if tab[1] == "O":
                win_j2 = True
        
        if tab[2] == tab[7] and tab[6] == tab[8]:
            
            if tab[2] == "X":
                win_j1 = True
            
            if tab[2] == "O":
                win_j2 = True
                
        # --------------------------------------------------------
        # On test si une diagonale contient 3 fois le meme symbole
        # --------------------------------------------------------
        if tab[0] == tab[4] and tab[0] == tab[8]:
            
            if tab[0] == "X":
                win_j1 = True
            
            if tab[0] == "O":
                win_j2 = True
        
        if tab[2] == tab[4] and tab[1] == tab[6]:
            
            if tab[2] == "X":
                win_j1 = True
            
            if tab[2] == "O":
                win_j2 = True
    
    if win_j1 == True and win_j2 == False:
        return f"Le gagnant est le joueur 1 !"
    if win_j2 == True and win_j1 == False:
        return f"Le gagnant est le joueur 2 !"

# print(test_win(my_tab))

# ***********************************************************************************
# ***********************************************************************************

def test_grille_complete(tab:list):
    
    complete = False
    compteur = 0
    
    for i in tab:
        if tab[i] != "_":
            compteur += 1

        if compteur == 9:
            complete = True
    
    return complete            

# print(test_grille_complete(my_tab))

# ***********************************************************************************
# ***********************************************************************************

def game(tab):
    
    print(grille(my_tab))
    bloqueur = test_win(tab)
    
    while bloqueur == False:
        
        print("test conculant")
        
        print(turn_j1(tab))
        test_grille_complete(tab)
        test_win(tab)
        
        print(turn_j2(tab))
        test_grille_complete(tab)
        test_win(tab)

# print("La partie peut commencer.\n")
# print(game(my_tab))

# ***********************************************************************************
# ***********************************************************************************

"""
S'il on veut programmmer un puissance 4, il nous faudra définir la hauteur de la 
grille et faire en sorte que l'on choisisse la colonne avec la quelle on souhaite
jouer et placer le pion du joueur en bas de la colonne.
"""