import datetime, time


class Pumps:

    def __init__(self, NAME, PRODUCTION, PERIOD, EXECUTION_TIME, PRIORITY_pumps=10):
        self.NAME = NAME
        self.PRODUCTION = PRODUCTION
        self.PERIOD = PERIOD
        self.EXECUTION_TIME = EXECUTION_TIME
        self.PRIORITY_pumps = PRIORITY_pumps  # 10 by default



class Tank(Pumps):

    def __init__(self, qte_max):
        self.qte_max = qte_max

        if self.qte_max == True:
                self.PRIORITY_pumps= 1
        else:
                self.PRIORITY_pumps = 10


class Machine1(Pumps):

    def __init__(self, QTE_Necessaire, NAME_Product, TEMPS_EXECUTION, PRIORITY_mach1=5):
        self.QTE_Necessaire = QTE_Necessaire
        self.NAME_Product = NAME_Product
        self.TEMPS_EXECUTION = TEMPS_EXECUTION
        self.PRIORITY_mach1 = PRIORITY_mach1


class Machine2(Pumps):

    def __init__(self, QTE_Ne, Nom_Produit, TPS_EXECUTION, PRIORITY_mach2=5):
        self.QTE_Ne = QTE_Ne
        self.Nom_Produit = Nom_Produit
        self.TPS_EXECUTION = TPS_EXECUTION
        self.PRIORITY_mach2 = PRIORITY_mach2



class Stock1(Machine1):

    def __init__(self, nb_wheels ):
        self.nb_wheels = nb_wheels



class Stock2(Machine2, Stock1):

    def __init__(self, nb_motors):
        self.nb_motors = nb_motors

        if self.nb_wheels/4 > nb_motors :
            self.PRIORITY_mach1 = 7
        else:
            self.PRIORITY_mach2 = 9




if __name__ == "__main__":

    # Definition of all tasks and instanciation
    Pumps_list = [
        Pumps(NAME='Pompe 1', PRODUCTION= 150, PERIOD= 'matin et soir', EXECUTION_TIME= 14, PRIORITY_pumps=10),
        Pumps(NAME='Pompe 2', PRODUCTION= 100 , PERIOD= 'matin', EXECUTION_TIME= 9, PRIORITY_pumps=10),]

    Machine1_list = [
        Machine1 (QTE_Necessaire= 40, NAME_Product= 'wheels', TEMPS_EXECUTION= 10, PRIORITY_mach1=5)
    ]

    Machine2_list = [
        Machine2(QTE_Ne= 130 , Nom_Produit = 'motors', TPS_EXECUTION= 30, PRIORITY_mach2=5)
    ]

