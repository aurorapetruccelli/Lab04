from cabina import Cabina
from passeggero import Passeggero
from cabina_deluxe import CabinaDeluxe
from cabina_animali import CabinaAnimali
from operator import attrgetter


class Crociera:
    def __init__(self, nome):
        self._nome= nome
        self.lista_passeggeri = []
        self.lista_cabine = []
        self.lista_passeggero_e_cabina = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if nome=='':
            raise Exception('Nome non vuoto')
        self._nome = nome


    def carica_file_dati(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                import csv
                csv_reader = csv.reader(infile, delimiter=',')
                for row in csv_reader:
                    if len(row) == 3:
                        codice_passeggero,nome,cognome = row
                        passeggero = Passeggero(codice_passeggero, nome, cognome)
                        self.lista_passeggeri.append(passeggero)
                    elif len(row) == 4:
                        codice_cabina, num_letti,ponte,prezzo = row
                        cabina = Cabina(codice_cabina, int(num_letti), int(ponte), int(prezzo))
                        self.lista_cabine.append(cabina)
                    else:
                        codice_cabina = row[0]
                        num_letti = int(row[1])
                        ponte = int(row[2])
                        prezzoiniziale = int(row[3])
                        try:
                            int(row[4])
                            intero = True
                        except ValueError:
                            intero = False

                        if intero:
                            num_animali = int(row[4])
                            prezzo = prezzoiniziale*(1+0.1*num_animali)
                            cab_animali=CabinaAnimali(codice_cabina,num_letti,ponte,prezzo,num_animali)
                            self.lista_cabine.append(cab_animali)
                        else:
                            tipologia = str(row[4])
                            prezzo = prezzoiniziale * 1.2
                            cab_deluxe = CabinaDeluxe(codice_cabina,num_letti,ponte,prezzo,tipologia)
                            self.lista_cabine.append(cab_deluxe)

        except FileNotFoundError:
            print("File not found")
            return None

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        cabina = None
        for c in self.lista_cabine:
            if c.codice_cabina == codice_cabina:
                cabina = c
                break

        if cabina is None:
            raise Exception(f"La cabina {codice_cabina} non esiste")

        if not cabina.disponibile:
            raise Exception(f"La cabina {codice_cabina} non è disponibile")

        passeggero = None
        for p in self.lista_passeggeri:
            if p.codice_passeggero == codice_passeggero:
                passeggero = p
                break

        if passeggero is None:
            raise Exception(f" Il passeggero {codice_passeggero} non esiste")

        if passeggero.codice_cabina != '':
            raise Exception(f"Il passeggero {codice_passeggero} è stato già assegnato a una cabina")


        cabina.disponibile = False
        passeggero.assegnazione(codice_cabina)


    def cabine_ordinate_per_prezzo(self):
        return sorted(self.lista_cabine, key = attrgetter("prezzo"))


    def elenca_passeggeri(self):
        for passeggero in self.lista_passeggeri:
            if passeggero.codice_cabina != '':
                self.lista_passeggero_e_cabina.append(f"{passeggero.codice_passeggero},{passeggero.codice_cabina}")
            else:
                self.lista_passeggero_e_cabina.append(f"{passeggero.codice_passeggero}")

        print(self.lista_passeggero_e_cabina)

