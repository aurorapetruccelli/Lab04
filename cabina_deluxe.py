from cabina import Cabina

class CabinaDeluxe(Cabina):
    def __init__(self,codice_cabina,num_letti,ponte,prezzo,tipologia,disponibile = True):
        super().__init__(codice_cabina,num_letti,ponte,prezzo)
        self.tipologia = tipologia
        self.disponibile = disponibile

    def __str__(self):
        if self.disponibile:
            self.disponibile = "Disponibile"
        else:
            self.disponibile = "Non disponibile"
        return f" Cabina = {self.codice_cabina} , {self.num_letti} , {self.ponte} , {self.prezzo} , {self.tipologia} , {self.disponibile}"