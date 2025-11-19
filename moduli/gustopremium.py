from .gusto import Gusto #Importo la classe base Gusto

class GustoPremium(Gusto):#Creo la sottoclasse GustoPremium
    def __init__(self, nome: str, prezzo_base: float, allergeni: list,#Aggiungo i nuvi attributi
                 ingredienti_speciali: list, sovrapprezzo: float):
        super().__init__(nome, prezzo_base, allergeni)#Chiamo il costruttore della classe base
        self.__ingredienti_speciali = ingredienti_speciali#Definisco gli attributi specifici di GustoPremium
        self.__sovrapprezzo = sovrapprezzo

    def get_ingredienti_speciali(self):#Metodo che permette di leggere il valore di ingredienti_speciali fuori dalla classe
        return self.__ingredienti_speciali

    def set_ingredienti_speciali(self, lista):#Metodo che permette di modificare gli ingredienti_speciali
        self.__ingredienti_speciali = lista

    def get_sovrapprezzo(self):#Metodo che permette di leggere il valore del sovrapprezzo fuori dalla classe
        return self.__sovrapprezzo

    def set_sovrapprezzo(self, sovrap):#Metodo che permette di modificare il sovrapprezzo
        self.__sovrapprezzo = sovrap

    def descrizione_premium(self):
        base = super().descrizione() #Richiamo con super() il metodo descrizione della classe base
        special = ", ".join(self.__ingredienti_speciali)#Trasformo la lista in una stringa unica quando stampo
        return (f"{base} | Ingredienti speciali: {special} | "
                f"Sovrapprezzo: {self.__sovrapprezzo}€")
