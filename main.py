# python c:/Users/Bukowski/Desktop/CDA/Mini_app/main.py
from fonctions.fonctions import *
# faire écrire des fonctions de debug (dd) 
# exemple 
# def debug (_message, _nom_variable):
#  	return print(_message + str(_nom_variable))

# debug("Debug ma variable : ", maison)
# print("Debug ma variable : " + str(maison))

# def super_input(_type, _message):
#     return _type(input(str(_message) + " : "))
choix = affiche_menu()

while choix != "0":
    match (choix):
        case "1":
            montant = float(input('Votre montant : '))
            remise = float(input('Votre remise : '))
            calcul_remise(montant, remise)
        case "2":
            # Choix du nb de faces par l'utilisateur
            nb_de_faces = int(input('Choisir un nombre de faces pour le dé : '))
            nb_de_lance = int(input("Nombre de lancé : "))
            lancer_de(nb_de_lance, nb_de_faces)
            lancer_de(nb_de_lance)
        case "3":
            juste_prix(0, 10)
        case "4":
            horloge_numerique("20")
        case "5":
            jeu_du_pendu()
        case "6":
            decodeur_cesar()
        case "7":
            gestionnaire_contact()
    choix = affiche_menu()

# sortie de while
print("*** FIN DU PROGRAMME ***")