from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self,codice_cabina,num_letti,ponte,prezzo,num_animali,disponibile=True):
        super().__init__(codice_cabina,num_letti,ponte,prezzo)
        self.num_animali = num_animali
        self.disponibile = disponibile

    def __str__(self):
        if self.disponibile:
            self.disponibile = "Disponibile"
        else:
            self.disponibile = "Non disponibile"
        return f" Cabina = {self.codice_cabina} , {self.num_letti} , {self.ponte} , {self.prezzo} , {self.num_animali} , {self.disponibile} "