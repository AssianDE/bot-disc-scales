from random import randint
from operator import itemgetter

class Lancer:
    def lancer_de_des(self, carac, comp, mana=1):
        liste_de_des = []
        for i in range(carac+comp):
            d = randint(1,10)
            if mana > 0:
                sauvegarde = d
                while d == 10:
                    d = randint(1,10)
                    sauvegarde += d
                d = sauvegarde
                mana-=1
                liste_de_des.append([d,"M"])
            else :
                liste_de_des.append([d,"N"])

        liste_triee = sorted(liste_de_des, key=itemgetter(0),reverse=True)

        seuil=0
        qr=0

        for i in range(len(liste_triee)):
            if carac > 0:
                seuil += liste_triee[i][0]
                liste_triee[i][0] = f"**{liste_triee[i][0]}**"
                carac -= 1
            elif comp >= 0:
                qr += liste_triee[i][0]
                liste_triee[i][0] = f"{liste_triee[i][0]}"
                comp -= 1
            if liste_triee[i][1]=="M":
                liste_triee[i][0] = f"{liste_triee[i][0]}*"

        qr = qr // 5

        return (liste_triee,seuil,qr)

    
    def lancer_init(self, reflex):
        d = randint(1, 10)
        modificateur = max(min((d - 5) // 2, 2), -2)
        return reflex + modificateur
