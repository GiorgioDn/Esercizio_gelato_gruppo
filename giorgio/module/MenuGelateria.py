from .Gusto import Gusto
from .GustoPremium import GustoPremium
from .GustoVegano import GustoVegano

class MenuGelateria():
    def __init__(self, gusti:list[Gusto] = []):
        self.__gusti = gusti
        
    def lista_gusti(self):
        if len(self.__gusti) > 0:
            
            formatting_list = []
            for n in self.__gusti:
                if type(n) == GustoPremium:
                    formatting_list.append([n.get_nome(), n.get_prezzo_base(), n.get_allergeni(), n.get_ingredienti_speciali(), n.get_sovraprezzo()])
                elif type(n) == GustoVegano:
                    formatting_list.append([n.get_nome(), n.get_prezzo_base(), n.get_allergeni(), n.get_base_vegetale()])
                else:
                    formatting_list.append([n.get_nome(), n.get_prezzo_base(), n.get_allergeni()])
        else:
            return False
        
    def aggiungi_gusto(self, gusto:gusto):
        self.__gusti.append(gusto)
    
    def rimuovi_gusto(self, nome_gusto):
        for n in self.__gusti:
            if n.get_nome() == nome_gusto:
                self.__gusti.remove(n)