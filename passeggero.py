class Passeggero:
    def __init__(self, codice_passeggero, nome_passeggero, cognome_passeggero):
        self.codice_passeggero = codice_passeggero
        self.nome_passeggero = nome_passeggero
        self.cognome_passeggero = cognome_passeggero
        self.codice_cabina = ''

    def assegnazione(self,codice_cabina):
        self.codice_cabina = codice_cabina

    def __str__(self):
        return f"Passeggero = {self.codice_passeggero} , {self.nome_passeggero} , {self.cognome_passeggero} , {self.codice_cabina}"

    def __eq__(self, other):
        return self.codice_passeggero == other.codice_passeggero
