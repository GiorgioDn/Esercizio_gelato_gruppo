from .gusto import Gusto
from .gustopremium import GustoPremium
from .GustoVegano import GustoVegano

class MenuGelateria():
    def __init__(self, gusti:list[Gusto] = []):
        self.__gusti = gusti
        
    def lista_gusti(self):
        if len(self.__gusti) > 0:
            
            formatting_list = []
            for n in self.__gusti:
                if type(n) == GustoPremium:
                    print(f"Gelato {n.get_nome()} - {n.get_prezzo_base()} euro - Allergeni: {n.get_allergeni()} - Con la possibilità di aggiungere: {n.get_ingredienti_speciali()} con un sovraprezzo di {n.get_sovraprezzo()} euro")
                elif type(n) == GustoVegano:
                    print(f"Gelato {n.get_nome()} - {n.get_prezzo_base()} euro - Allergeni: {n.get_allergeni()} - Con la possibilità di aggiungere: {n.get_base_vegetale()}")
                else:
                    print(f"Gelato {n.get_nome()} - {n.get_prezzo_base()} euro - Allergeni: {n.get_allergeni()}")
        else:
            return False
        
    def aggiungi_gusto(self, gusto:Gusto):
        self.__gusti.append(gusto)
    
    def rimuovi_gusto(self, nome_gusto:str):
        for n in self.__gusti:
            if n.get_nome() == nome_gusto:
                self.__gusti.remove(n)