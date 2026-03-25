#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random

def obtenir_nom():
    # Llista de noms incorrectes
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    nom_aleatori = random.choice(noms)
    # Llista de cognoms incorrectes
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]
    cognom_aleatori = random.choice(cognoms)

    #print("PENDENT: obtenir_nom")
    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït
    return str(nom_aleatori + " " + cognom_aleatori)

def afegir_nom(llista):
    nou_nom = obtenir_nom()
    #print("PENDENT: afegir_nom")
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom
    llista.append(nou_nom)
    print(f"S'ha afegit el nom: {nou_nom}")
    return llista


def llistar_noms(llista):
    #print("PENDENT: llistar_noms")
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

    print(llista)

def ordenar_noms(llista):
    #print("PENDENT: ordenar_noms")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms
    llista.sort()
    print(llista)
    return llista

def mostrar_menu():
    #print("PENDENT: mostrar_menu")
    # Hem de mostrar el menú que ens demanen a l'enunciat
    print("[A] Afegir nom")
    print("[L] Llistar noms")
    print("[O] Ordenar noms")
    print("[F] Finalitzar")
    

def demanar_opcio():
    #print("PENDENT: demanar_opcio")
    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada        
    opcio_usuari = input("Que vols fer: ")

    while opcio_usuari not in ["A", "L", "O", "F"] and opcio_usuari not in ["a", "l", "o", "f"]:
        print("Siusplau esculliu una opció valida")
        print("[A] Afegir nom")
        print("[L] Llistar noms")
        print("[O] Ordenar noms")
        print("[F] Finalitzar")
        opcio_usuari = input("Que vols fer: ")
    return opcio_usuari

def gestionar_opcio(opcio, llista):
    #print("PENDENT: gestionar_opcio")
    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    
    match opcio:
        case "A":
            afegir_nom(llista)
        case "L":
            llistar_noms(llista)
        case "O":
            ordenar_noms(llista)
        case "F":
            return False
        case "a":
          afegir_nom(llista)
        case "l":
            llistar_noms(llista)
        case "o":
            ordenar_noms(llista)
        case "f":
            return False


# Programa principal

#print("PENDENT: programa principal")
# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
llista = []
continuar = True
mostrar_menu()
while continuar == True:
    opcio = demanar_opcio()
    if gestionar_opcio(opcio, llista) == False:
        continuar = False