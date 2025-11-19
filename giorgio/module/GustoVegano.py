from .Gusto import Gusto

class GustoVegano(Gusto):
    #prende i dati della super classe gusto in aggiunta alla stringa base_vegetale
    def __init__(self, nome:str, prezzo_base:float, allergeni:list[str], base_vegetale:str):
        super().__init__(nome, prezzo_base, allergeni)
        self.__base_vegetale=base_vegetale
    
    #restituisco il parametro privato base_vegetale 
    def get_base_vegetale(self):
        if len(self.__base_vegetale) > 0:
            return self.__base_vegetale
        else:
            return False
    
    def set_base_vegetale(self, base_vegetale):
        if len(self.__base_vegetale) > 0:
            self.__base_vegetale = base_vegetale
        else:
            return False
    
    
    def descrizione(self):
        base = super().descrizione()
        return f"Il gelato {base} ha la base vegetale al {self.__base_vegetale}"