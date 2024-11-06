class Calcul:
    montant = 0
    remise = 0

    def __init__(self, montant, remise):
        self.montant = montant
        self.remise = remise

    def calculRemise(self):
        resultat = round(self.montant - self.montant * (self.remise/100), 2)
        return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

    def calculAireCarre(self):
        return

resultat = Calcul(100, 20)

resultat.calculRemise()