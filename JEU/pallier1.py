from all_variable import *
class pallier1 = (print("Les choix seront toujours en minuscule merci"
sleep(5)
print("chargement du jeu 55%")
sleep(2)
print("chargement du jeu 100%")
sleep(1)
print("chargement du jeu")
print("téléportation zone 1")
sleep(1)
print("bonjour")
name = input("Comment t'appeles tu?: ")
print("bien " + name + " tu viens de spawn dans un jeu vidéo s'appelles Just One Fire")
print("tu es un nouveau pompier, tu es dans la caserne dans la première ville du jeu")
sleep(5)
print("BIP ... BIP ...")
sleep(3)
print("une voix retentie dans les au parleurs 'RMPGP1 avec " + name + ", James, Pierre et Jean pour feu de grange'")
print("vous courez dans le RMPGP avec vos coéquipiez.")
sleep(4)
print("Vous arrivez dix minutes plus tard devant une vielle grange en feu")
sleep(1)
print("vous voyez une femmme qui semble inconsiente")
sleep(2)
sauvez_femme = input("voulez vous la sauvez: ")
if sauvez_femme == 'oui ':
    print("vous vous equipez avec une bouteille d'oxygène pour allez la sauver")
    sleep(2)
    if aléatoire == 1:
        print("vous sortez la femme de la grange pour l'enmener dans une ambulance")
        sleep(2)

    elif aléatoire == 2:
        exit("vous n'arriver pas à temps pour sauver cette femme")




elif sauvez_femme == 'non':
    print("vous la laisser mourir, ce n'est pas bien vortre metier c'est de sauver les gens pas de les laisser mourire. Mais bon")
    sleep(2)
    print("Une heure après votre chef vous convoque dans son bureau. Il vous demande comment c'est passer votre première intervention.")
    mentir = input("voulez vous lui mentir? ")
    if mentir == 'oui':
        sleep(2)
        if aléatoire == 1:
            print("vous lui dites que vous avez réussis à maitriser le feu et qu'aucune victine n'est à déplorer")
        elif aléatoire == 2:
            print("vous tentez de lui mentir mais il voit votre visage crispé")
            sleep(2)
            exit("GAME OVER")


    elif mentir == 'non':
            print("vous lui dites qu'au moment venue de sauver une vie vous avez perdue tout vos moyens")
            print("il vous répond qu'il vous remercie de votre honnêté même si vous perdu vos moyen ce n'était pas grave")


else:
    print("nous n'avons pas bien compris veuillez répétez")
    sleep(3)
    print("(répondre de préference par oui ou par non merci)")
    sauvez_femme = input("voulez vous la sauvez: ")

    #deuxième fois mdr
    if sauvez_femme == 'oui':
        print("vous vous equipez avec une bouteille d'oxygène pour allez la sauver")
    sleep(2)
    if aléatoire == 1:
        print("vous sortez la femme de la grange pour l'enmener dans une ambulance")
        sleep(2)

    elif aléatoire == 2:
        exit("vous n'arriver pas à temps pour sauver cette femme")




    elif sauvez_femme == 'non':
        print("vous la laisser mourir, ce n'est pas bien vortre metier c'est de sauver les gens pas de les laisser mourire. Mais bon")
        sleep(2)
        print("Une heure après votre chef vous convoque dans son bureau. Il vous demande comment c'est passer votre première intervention.")
        mentir = input("voulez vous lui mentir? ")
    if mentir == 'oui':
        sleep(2)
        if aléatoire == 1:
            print("vous lui dites que vous avez réussis à maitriser le feu et qu'aucune victine n'est à déplorer")
        elif aléatoire == 2:
            print("vous tentez de lui mentir mais il voit votre visage crispé")
            sleep(2)
            exit("GAME OVER")


    elif mentir == 'non':
            print("vous lui dites qu'au moment venue de sauver une vie vous avez perdue tout vos moyens")
            print("il vous répond qu'il vous remercie de votre honnêté même si vous perdu vos moyen ce n'était pas grave")




print("téléportation zone 2"))
