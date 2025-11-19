from moduli.gusto import Gusto
from moduli.gustopremium import GustoPremium
from moduli.GustoVegano import GustoVegano
from moduli.MenuGelateria import MenuGelateria

def menu():
    print("\nMENU GELATERIA ")
    print("1. Aggiungi gusto base")
    print("2. Aggiungi gusto premium")
    print("3. Mostra tutti i gusti")
    print("4. Aggiungi gusto vegano")
    print("5. Aggiungi al menu")
    print("6. Rimuovi dal menu")
    print("7. Visualizza il menu")
    print("8. Esci")
    return input("Scegli un'opzione: ")

def chiedi_allergeni():
    allergeni = input("Inserisci allergeni separati da virgola (oppure lascia vuoto): ")
    if allergeni.strip() == "":
        return []
    return [a.strip() for a in allergeni.split(",")]

def chiedi_lista(messaggio):
    testo = input(messaggio + " (separati da virgola): ")
    return [x.strip() for x in testo.split(",")]

def main():
    gusti = MenuGelateria([])  # lista che contiene tutti i gusti creati

    while True:
        scelta = menu()

        if scelta == "1":
            print("\nNUOVO GUSTO BASE")
            nome = input("Nome: ")
            prezzo = float(input("Prezzo base: "))
            allergeni = chiedi_allergeni()

            gusto = Gusto(nome, prezzo, allergeni)
            gusti.aggiungi_gusto(gusto)
            print("Gusto base aggiunto!")

        elif scelta == "2":
            print("\nNUOVO GUSTO PREMIUM")
            nome = input("Nome: ")
            prezzo = float(input("Prezzo base: "))
            allergeni = chiedi_allergeni()
            ingredienti = chiedi_lista("Ingredienti speciali")
            sovrapprezzo = float(input("Sovrapprezzo: "))

            gusto_p = GustoPremium(nome, prezzo, allergeni, ingredienti, sovrapprezzo)
            gusti.aggiungi_gusto(gusto_p)
            print("Gusto premium aggiunto!")

        elif scelta == "3":
            print("\nLISTA DEI GUSTI")
            if len(gusti) == 0:
                print("Nessun gusto presente")
            else:
                for g in gusti:
                    if isinstance(g, GustoPremium):
                        print(g.descrizione_premium())
                    else:
                        print(g.descrizione())
        
        elif scelta == "4":
            print("\nNUOVO GUSTO VEGANO")
            nome = input("Nome: ")
            prezzo = float(input("Prezzo base: "))
            allergeni = chiedi_allergeni()
            base_vegetale = input("Base vegetale: ")

            gusto_p = GustoVegano(nome, prezzo, allergeni, base_vegetale)
            gusti.aggiungi_gusto(gusto_p)
            print("Gusto vegano aggiunto!")

        elif scelta == "8":
            print("Arrivederci")
            break

        else:
            print("Scelta non valida, riprova")

if __name__ == "__main__":
    main()
