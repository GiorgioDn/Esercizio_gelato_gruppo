class Gusto:#Creo la classe base Gusto
    def __init__(self, nome: str, prezzo_base: float, allergeni: list):#Costruttore con parametri e relativo tipo
        self.__nome = nome#Creo l'attributo privato nome
        self.__prezzo_base = prezzo_base#Creo l'attributo privato prezzo_base
        self.__allergeni = allergeni#Creo l'attributo privato allergeni

    def get_nome(self):#Metodo che permette di leggere il valore del nome fuori dalla classe
        return self.__nome

    def set_nome(self, nome):#Metodo che permette di modificare il nome 
        self.__nome = nome

    def get_prezzo_base(self):#Metodo che permette di leggere il valore del prezzo_base fuori dalla classe
        return self.__prezzo_base

    def set_prezzo_base(self, prezzo):#Metodo che permette di modificare il prezzo_base
        self.__prezzo_base = prezzo

    def get_allergeni(self):#Metodo che permette di leggere il valore degli allergeni fuori dalla classe
        return self.__allergeni

    def set_allergeni(self, allergeni):#Metodo che permette di modificare gli allergeni
        self.__allergeni = allergeni

    def descrizione(self):#Creo il metodo descrizione
        return f"Gusto: {self.__nome} - Prezzo base: {self.__prezzo_base}€ - Allergeni: {', '.join(self.__allergeni)}"
