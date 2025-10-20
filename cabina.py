class Cabina:
    def __init__(self, codice_cabina,num_letti,ponte, prezzo,disponibile=True):
        self.codice_cabina = codice_cabina
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibile = disponibile


    def __str__(self):
        if self.disponibile:
            self.disponibile = "Disponibile"
        else:
            self.disponibile = "Non disponibile"
        return f"Cabina  = {self.codice_cabina} , {self.num_letti} , {self.ponte} , {self.prezzo} , {self.disponibile}"

    def __eq__(self, other):
        return self.codice_cabina == other.codice_cabina

