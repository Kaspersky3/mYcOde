# Chapter 4 & 5: Arrêt, Stationnement, Vitesse, Autoroute (Questions 360 to 507)
# Extracted from DGTT 2011 pages 85 to 106

def get_chapitre4_5_questions():
    questions = []
    
    def q(num, chap, theme, enonce, options, rep, page, img=None, exp=None, diff=1, tags=None):
        import re
        clean_rep = rep.lower().replace('réponses', '').replace('réponse', '').replace(':', '').strip().strip('.')
        clean_rep = re.sub(r'\bet\b', ' ', clean_rep)
        tokens = re.findall(r'\b[a-e]\b|[a-e]', clean_rep)
        opt_ids = [opt[0] for opt in options]
        bonnes = sorted(list(set([t for t in tokens if t in opt_ids])))
        multi = len(bonnes) > 1
        t = tags or []
        if multi and "multi-reponses" not in t:
            t.append("multi-reponses")
        t.append("categorie-b")
        return {
            "id": f"q{num}",
            "numero": num,
            "chapitre": chap,
            "theme": theme,
            "enonce": enonce.strip(),
            "options": [{"id": opt[0], "texte": opt[1]} for opt in options],
            "bonnesReponses": bonnes,
            "multiReponses": multi,
            "image": img,
            "page": page,
            "explication": exp,
            "sourceExplication": "redige" if exp else None,
            "tags": t,
            "difficulte": diff,
            "groupeDoublon": None
        }

    # CHAPITRE IV (Questions 360 to 470)
    questions.append(q(360, 4, "Manœuvres sur chaussée", "Sur une chaussée à double sens :",
        [("a", "Je peux faire demi-tour"),
         ("b", "Je ne peux pas faire demi-tour"),
         ("c", "Je ne peux pas faire marche arrière")],
        "Réponse a", 85, exp="Le demi-tour est possible sur chaussée à double sens s'il n'y a pas de ligne continue ni de panneau l'interdisant."))

    questions.append(q(361, 4, "Flèches de rabattement", "Les flèches de rabattement m’obligent :",
        [("a", "A serrer ma gauche"),
         ("b", "A serrer ma droite"),
         ("c", "A quitter la chaussée"),
         ("d", "A réduire ma vitesse")],
        "Réponse b", 85))

    questions.append(q(362, 4, "Chaussée à plus de deux voies", "Sur une chaussée à double sens comportant plus de deux voies, il est interdit d’emprunter :",
        [("a", "La voie la plus à droite"),
         ("b", "La voie du milieu"),
         ("c", "La voie la plus à gauche")],
        "Réponse c", 85, exp="La voie la plus à gauche est réservée au sens inverse."))

    questions.append(q(363, 4, "Définition de l'arrêt", "En quoi consiste l’arrêt ?",
        [("a", "A l’immobilisation momentanée d’un véhicule, conducteur à bord"),
         ("b", "A l’immobilisation de longue durée d’un véhicule, conducteur éloigné"),
         ("c", "A l’immobilisation momentanée d’un véhicule, conducteur éloigné")],
        "Réponse a", 85, exp="Arrêt : immobilisation momentanée pour faire monter/descendre des passagers ou charger/décharger, le conducteur restant à bord ou à proximité immédiate."))

    questions.append(q(364, 4, "Conducteur lors d'un arrêt", "Lors d’un arrêt :",
        [("a", "Le conducteur est à côté du véhicule"),
         ("b", "Le conducteur s’éloigne du véhicule"),
         ("c", "Le conducteur est à bord du véhicule")],
        "Réponses a-c", 85, tags=["multi-reponses"]))

    questions.append(q(365, 4, "Définition du stationnement", "En quoi consiste le stationnement ?",
        [("a", "A l’immobilisation momentanée d’un véhicule, conducteur à bord"),
         ("b", "A l’immobilisation momentanée d’un véhicule, conducteur à côté"),
         ("c", "A l’immobilisation momentanée d’un véhicule, conducteur éloigné"),
         ("d", "A l’immobilisation de longue durée d’un véhicule")],
        "Réponses c-d", 85, tags=["multi-reponses"]))

    questions.append(q(366, 4, "Panneau stationnement interdit", "En présence du panneau de \"stationnement interdit\" je suis autorisé à :",
        [("a", "Stationner avant le panneau"),
         ("b", "Stationner après le panneau"),
         ("c", "Stationner avant la prochaine intersection")],
        "Réponse a", 85))

    questions.append(q(367, 4, "Début interdiction arrêt et stationnement", "A la rencontre du panneau \"arrêt et stationnement interdits\", l’interdiction commence :",
        [("a", "Avant le panneau"),
         ("b", "A partir du panneau"),
         ("c", "15 m après le panneau")],
        "Réponse b", 86))

    questions.append(q(368, 4, "Distance de freinage", "La distance de freinage augmente :",
        [("a", "quand la chaussée est mouillée"),
         ("b", "quand les pneus sont usés"),
         ("c", "quand les rotules sont usées"),
         ("d", "quand la chaussée est rétrécie")],
        "Réponse a-b", 86, tags=["multi-reponses"]))

    questions.append(q(369, 4, "Insertion d'un usager", "A la vue d’un usager qui veut s’insérer dans la circulation :",
        [("a", "je klaxonne"),
         ("b", "je ralentis"),
         ("c", "je fais un appel de feux"),
         ("d", "je change de voie")],
        "Réponse b", 86))

    questions.append(q(370, 4, "Distance d'arrêt facteurs", "La distance d’arrêt augmente :",
        [("a", "si le conducteur est fatigué"),
         ("b", "si la chaussée est légèrement mouillée"),
         ("c", "si les pneus sont usés"),
         ("d", "rien de tout ce qui précède")],
        "Réponse a, b, c", 86, tags=["multi-reponses"], exp="Distance d'arrêt = distance parcourue pendant temps de réaction + distance de freinage."))

    questions.append(q(371, 4, "Pluie et risques", "En cas de pluie, je risque :",
        [("a", "l’aquaplaning"),
         ("b", "la glissade"),
         ("c", "le blocage des roues")],
        "Réponse: a, b", 86, tags=["multi-reponses"]))

    questions.append(q(372, 4, "Vitesse et distances", "Plus je roule vite et plus j’augmente :",
        [("a", "le temps de réaction"),
         ("b", "la distance d’arrêt"),
         ("c", "la distance de freinage")],
        "Réponse b, c", 86, tags=["multi-reponses", "piege"], exp="Le temps de réaction (en secondes) dépend de l'état du conducteur, pas de la vitesse du véhicule."))

    questions.append(q(373, 4, "Distance de freinage dépendance", "La distance de freinage dépend :",
        [("a", "de la vitesse"),
         ("b", "de l’adhérence"),
         ("c", "du temps de réaction"),
         ("d", "de l’état physique du conducteur"),
         ("e", "de l’état des amortisseurs")],
        "Réponse : a, b", 86, tags=["multi-reponses"]))

    questions.append(q(374, 4, "Changement de direction", "Un conducteur ayant l’intention de changer de direction doit :",
        [("a", "ralentir"),
         ("b", "signaler son intention"),
         ("c", "klaxonner pour faire dégager les piétons engagés sur leur passage")],
        "Réponse : a, b", 87, tags=["multi-reponses"]))

    questions.append(q(375, 4, "Approche d'un lieu-dit", "Quel doit être votre comportement à l’approche d’un lieu-dit :",
        [("a", "rouler vite"),
         ("b", "ralentir"),
         ("c", "klaxonner")],
        "Réponse b, c", 87, tags=["multi-reponses"]))

    questions.append(q(376, 4, "Précautions virage direction", "Un conducteur ayant l’intention de changer de direction doit :",
        [("a", "s’assurer que la route qu’il veut emprunter n’est pas en sens interdit"),
         ("b", "surveiller la route vers l’avant et l’arrière"),
         ("c", "signaler son intention à l’aide du clignotant"),
         ("d", "ralentir sans freiner brusquement pour ne pas surprendre les usagers qui le suivent"),
         ("e", "respecter les priorités de passage et notamment les piétons qui traversent")],
        "Réponse a, b, c, d, e", 87, tags=["multi-reponses"]))

    questions.append(q(377, 4, "Adaptation de la vitesse", "Pour adapter sa vitesse le conducteur doit tenir compte :",
        [("a", "de l’importance du trafic"),
         ("b", "des risques prévisibles"),
         ("c", "de l’adhérence"),
         ("d", "de la visibilité"),
         ("e", "de sa propre vigilance")],
        "Réponse a, b, c, d, e", 87, tags=["multi-reponses"]))

    questions.append(q(378, 4, "Vent latéral", "Un vent latéral violent est particulièrement dangereux :",
        [("a", "lorsqu’il souffle par rafales"),
         ("b", "lors du passage de zones ventées en zones abritées"),
         ("c", "si je tracte une caravane"),
         ("d", "s’il souffle de face")],
        "Réponse: a, c", 87, tags=["multi-reponses"]))

    questions.append(q(379, 4, "Vitesse de nuit autoroute feux de route", "De nuit, seul sur autoroute, avec des feux de route éclairant à 100 mètres, je peux rouler à :",
        [("a", "130 km/h"), ("b", "110 km/h"), ("c", "100 km/h")],
        "Réponse c", 87, tags=["chiffre"]))

    questions.append(q(380, 4, "Voie d'insertion rôle", "Sur une voie d’insertion, j’accélère pour :",
        [("a", "atteindre la vitesse de circulation de la chaussée abordée"),
         ("b", "M’engager sans ralentir la circulation"),
         ("c", "M’engager avant les usagers de la route abordée")],
        "Réponse : a, b", 88, tags=["multi-reponses"]))

    questions.append(q(381, 4, "Insertion sur voie rapide", "Sur une voie d’insertion :",
        [("a", "J’accélère, je mets le clignotant, je me place dans ma voie"),
         ("b", "J’accélère en contrôlant, je mets le clignotant dès que je peux m’insérer"),
         ("c", "J’accélère jusqu’au bout de la voie, je contrôle, je m’insère si je peux")],
        "Réponse : b", 88))

    questions.append(q(382, 4, "Rayon de virage et force centrifuge", "Plus le rayon du virage est faible :",
        [("a", "Plus le virage est serré"),
         ("b", "Plus le virage est large"),
         ("c", "Plus la force centrifuge est importante"),
         ("d", "Plus la force centrifuge est faible")],
        "Réponse : a-c", 88, tags=["multi-reponses"]))

    questions.append(q(383, 4, "Stationnement accotement impraticable", "Sur route, lorsque l’accotement de droite n’est pas praticable je peux stationner :",
        [("a", "sur l’accotement de gauche"),
         ("b", "sur l’accotement de gauche en agglomération"),
         ("c", "sur la voie de droite")],
        "Réponse : a", 88))

    questions.append(q(384, 4, "Arrêt interdit conséquence", "Lorsque l’arrêt est interdit :",
        [("a", "le stationnement est interdit"),
         ("b", "le stationnement n’est pas interdit"),
         ("c", "le stationnement temporaire est interdit"),
         ("d", "seul le stationnement temporaire est autorisé")],
        "Réponse : a, c", 88, tags=["multi-reponses"], exp="Qui ne peut le moins ne peut le plus : si l'arrêt est interdit, le stationnement l'est automatiquement."))

    questions.append(q(385, 4, "Stationnement payant contrôle", "Le contrôle de la durée d’un stationnement payant peut se faire :",
        [("a", "par horodateur"),
         ("b", "par disque de stationnement"),
         ("c", "par parcmètre")],
        "Réponse : a-c", 88, tags=["multi-reponses"]))

    questions.append(q(386, 4, "Stationnement gênant", "On appelle stationnement gênant le fait de stationner :",
        [("a", "dans une voie réservée aux bus"),
         ("b", "devant une sortie de propriété"),
         ("c", "sur un pont"),
         ("d", "à proximité d’une voie ferrée")],
        "Réponse : a-b", 88, tags=["multi-reponses"]))

    questions.append(q(387, 4, "Ajuster sa vitesse", "Ajuster sa vitesse aux circonstances, c’est ralentir suffisamment :",
        [("a", "pour ne jamais dépasser la vitesse maximum autorisée"),
         ("b", "chaque fois que la visibilité est réduite"),
         ("c", "chaque fois que l’adhérence est réduite")],
        "Réponse : b-c", 89, tags=["multi-reponses"]))

    questions.append(q(388, 4, "Évaluer l'allure d'un usager", "Pour évaluer l’allure d’un autre usager venant en face, je prends en compte :",
        [("a", "le type de véhicule"),
         ("b", "la vitesse de rapprochement"),
         ("c", "l’état du conducteur")],
        "Réponse : a-b", 89, tags=["multi-reponses"]))

    questions.append(q(389, 4, "Définition temps de réaction", "Le temps de réaction est le temps nécessaire au conducteur pour :",
        [("a", "percevoir et réagir"),
         ("b", "arrêter la voiture"),
         ("c", "évaluer l’allure d’un autre usager")],
        "Réponse : a", 89))

    questions.append(q(390, 4, "Durée moyenne temps de réaction", "Le temps de réaction a une durée d’environ :",
        [("a", "un dixième de seconde"),
         ("b", "une seconde"),
         ("c", "dix secondes")],
        "Réponse : b", 89, tags=["chiffre"], exp="Le temps de réaction moyen d'un conducteur sobre et attentif est d'environ 1 seconde."))

    questions.append(q(391, 4, "Chaussée mouillée et distances", "Sur chaussée mouillée ou glissante, il y a augmentation de la distance :",
        [("a", "Parcourue pendant le temps de réaction"),
         ("b", "De freinage"),
         ("c", "D’arrêt")],
        "Réponse : b-c", 89, tags=["multi-reponses"]))

    questions.append(q(392, 4, "Calcul distance d'arrêt à 90 km/h", "A 90 km/h, dans des conditions normales, ma distance d’arrêt est d’environ :",
        [("a", "25 mètres"),
         ("b", "54 mètres"),
         ("c", "81 mètres")],
        "Réponse : c", 89, tags=["chiffre"], exp="Règle mnémotechnique : chiffre des dizaines multiplié par lui-même (9 x 9 = 81 mètres)."))

    questions.append(q(393, 4, "Objet de la réglementation stationnement", "La règlementation du stationnement a pour objet :",
        [("a", "La sécurité"),
         ("b", "La fluidité de la circulation")],
        "Réponse : a-b", 89, tags=["multi-reponses"]))

    questions.append(q(394, 4, "Types d'infractions stationnement", "Je suis en infraction si je suis en stationnement :",
        [("a", "Dangereux"),
         ("b", "Abusif"),
         ("c", "Gênant")],
        "Réponse : a-b-c", 89, tags=["multi-reponses"], exp="Les 3 catégories de stationnement illicite : dangereux, gênant, abusif."))

    questions.append(q(395, 4, "Réduire sa vitesse cas", "Dans quels cas faut-il réduire sa vitesse ?",
        [("a", "Lorsqu’il n’y a pas de panneau de signalisation"),
         ("b", "Lorsque la route n’apparaît pas libre"),
         ("c", "Dans les descentes rapides"),
         ("d", "Lorsqu’on aborde une intersection"),
         ("e", "A l’approche des montées")],
        "Réponse b-c-d", 90, tags=["multi-reponses"]))

    questions.append(q(396, 4, "Achat rapide journal", "Lorsque je quitte momentanément mon véhicule pour acheter mon journal, je suis considéré comme étant :",
        [("a", "En arrêt"),
         ("b", "En stationnement")],
        "Réponse : b", 90, exp="Dès que le conducteur s'éloigne du véhicule (même pour 1 minute), il s'agit d'un stationnement et non d'un arrêt."))

    questions.append(q(397, 4, "Stationnement en bataille", "En général, se ranger en bataille s’effectue :",
        [("a", "En marche avant"),
         ("b", "En marche arrière")],
        "Réponse : b", 90))

    questions.append(q(398, 4, "Période probatoire vitesse autoroute", "Pendant la durée de la période probatoire, la vitesse du conducteur sur une autoroute est ordinairement limitée à :",
        [("a", "100 km/h"),
         ("b", "110 km/h"),
         ("c", "130 km/h")],
        "Réponse : b", 90, tags=["chiffre"]))

    questions.append(q(399, 4, "Visibilité réduite à 50 mètres", "En cas de visibilité réduite à 50mètres, la vitesse ne peut excéder :",
        [("a", "90 km/h"),
         ("b", "60 km/h"),
         ("c", "50 km/h")],
        "Réponse : c", 90, tags=["chiffre"], exp="Règle des 50 mètres : visibilité < 50 m => vitesse max 50 km/h sur tout le réseau."))

    questions.append(q(400, 4, "Stationnement route montagne", "Sur une route de montagne, je stationne de préférence :",
        [("a", "En côte, sur la chaussée"),
         ("b", "En descente, sur la chaussée"),
         ("c", "Sur une place d’évitement")],
        "Réponse : c", 90))

    questions.append(q(401, 4, "Défaillance frein principal", "En cas de défaillance du frein principal :",
        [("a", "je rétrograde pour utiliser le frein moteur"),
         ("b", "je coupe le moteur pour arrêter le véhicule"),
         ("c", "je dose mon freinage à l’aide du frein à main déverrouillé")],
        "Réponse : a-c", 90, tags=["multi-reponses"]))

    questions.append(q(402, 4, "Comportement en dérapage", "Un conducteur d’un véhicule qui dérape doit :",
        [("a", "freiner fort pour stopper le véhicule"),
         ("b", "braquer calmement pour ramener le véhicule sur sa trajectoire"),
         ("c", "accélérer franchement pour redonner de l’adhérence aux roues arrière")],
        "Réponse : b", 91))

    questions.append(q(403, 4, "Roues mordant le bas-côté", "Si mes roues mordent sur le bas côté de la route :",
        [("a", "je freine fort et je corrige rapidement ma trajectoire"),
         ("b", "je freine légèrement et je reviens progressivement sur la chaussée")],
        "Réponses : b", 91))

    questions.append(q(404, 4, "Remorquage vitesse et signalisation", "Lorsque je fais remorquer mon véhicule par un autre usager :",
        [("a", "je ne dois pas dépasser la vitesse de 25 km/h"),
         ("b", "je dois signaler mon véhicule à l’aide des feux de détresse"),
         ("c", "je reste vigilant")],
        "Réponse : b-c", 91, tags=["multi-reponses"]))

    # Questions 405 to 470 (Pages 93 to 100)
    questions.append(q(405, 4, "Changement de direction droite", "A bord d’un véhicule de tourisme, pour tourner à droite, je dois :",
        [("a", "Serrer ma droite"),
         ("b", "Serrer ma gauche"),
         ("c", "Me déporter au milieu de la chaussée")],
        "Réponse a", 93))

    questions.append(q(406, 4, "Actions pour tourner à droite", "Pour tourner à droite, je dois :",
        [("a", "Accélérer"),
         ("b", "Mettre le clignotant à droite"),
         ("c", "Ralentir")],
        "Réponse b-c", 93, tags=["multi-reponses"]))

    questions.append(q(407, 4, "Tourner à gauche chaussée double sens", "A bord d’un véhicule de tourisme pour tourner à gauche sur une chaussée à double sens, je dois :",
        [("a", "Serrer ma droite"),
         ("b", "Me déporter au milieu de la chaussée"),
         ("c", "Serrer ma gauche")],
        "Réponse b", 93))

    questions.append(q(408, 4, "Tourner à gauche sens unique", "A bord d’un véhicule de tourisme pour tourner à gauche sur une chaussée à sens unique, je dois :",
        [("a", "Serrer ma droite et mettre le clignotant à gauche"),
         ("b", "Respecter les règles de priorité"),
         ("c", "Serrer ma gauche")],
        "Réponses b-c", 93, tags=["multi-reponses"]))

    questions.append(q(409, 4, "Cas de réduction de vitesse", "Je dois réduire ma vitesse :",
        [("a", "A l’approche d’un virage"),
         ("b", "A la hauteur d’une ligne continue"),
         ("c", "A l’approche d’une intersection")],
        "Réponses a-c", 93, tags=["multi-reponses"]))

    questions.append(q(410, 4, "Cas de réduction de vitesse bis", "Je dois réduire ma vitesse :",
        [("a", "A la sortie d’une agglomération"),
         ("b", "A la vue d’un panneau de limitation de vitesse"),
         ("c", "Pendant le dépassement"),
         ("d", "A l’approche d’un passage à niveau")],
        "Réponses b-d", 93, tags=["multi-reponses"]))

    questions.append(q(411, 4, "Bande rouge discontinue trottoir", "La bande rouge discontinue de blanc le long du trottoir, interdit :",
        [("a", "L’arrêt"),
         ("b", "Le stationnement"),
         ("c", "L’arrêt pour les véhicules légers")],
        "Réponse b", 93))

    questions.append(q(412, 4, "Durée stationnement abusif", "Après combien de jours le stationnement devient-il abusif ?",
        [("a", "10 jours"),
         ("b", "7 jours"),
         ("c", "4 jours"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse b", 94, tags=["chiffre"], exp="Un stationnement ininterrompu de plus de 7 jours consécutifs au même endroit est qualifié d'abusif."))

    questions.append(q(413, 4, "Panneau B7b interdiction", "Le panneau B7b :",
        [("a", "Interdit le stationnement à tout véhicule à moteur sauf les camions"),
         ("b", "Interdit l’accès à tous les véhicules à moteur"),
         ("c", "Interdit l’accès à tous les véhicules sauf les camions")],
        "Réponse b", 94, img="B7b"))

    questions.append(q(414, 4, "Panneau B6d portée", "A la vue du panneau B6d :",
        [("a", "Je ne peux pas m’arrêter"),
         ("b", "Je ne peux pas m’arrêter mais je peux stationner"),
         ("c", "Je ne peux ni m’arrêter ni stationner")],
        "Réponse a-c", 94, img="B6d", tags=["multi-reponses"]))

    questions.append(q(415, 4, "Utilisation frein moteur", "Dans quels cas peut-on utiliser le frein moteur ?",
        [("a", "Pour s’arrêter"),
         ("b", "Pour ralentir"),
         ("c", "Pour aborder un virage"),
         ("d", "Pour aborder une descente dangereuse")],
        "Réponse b-c-d", 94, tags=["multi-reponses"]))

    questions.append(q(416, 4, "Panneau B9c animaux", "Que signifie le panneau B9c ?",
        [("a", "Accès interdit aux chevaux"),
         ("b", "Accès interdit aux véhicules agricoles à moteur"),
         ("c", "Accès interdit aux véhicules à traction animale")],
        "Réponse c", 94, img="B9c"))

    # Notice: In the manual, questions jump from 416 to 427!
    questions.append(q(427, 4, "Fin de vitesse minimale B43", "A quelle vitesse peut-on rouler à la vue du panneau B43 ?",
        [("a", "A 30 km/h"),
         ("b", "A plus de 30 km/h"),
         ("c", "A la vitesse réglementaire"),
         ("d", "A moins de 30 km/h"),
         ("e", "Rien de tout ce qui précède")],
        "Réponse a-b-c-d", 94, img="B43", tags=["multi-reponses"]))

    questions.append(q(428, 4, "Stationnement dangereux lieux", "Le stationnement est dangereux :",
        [("a", "Dans un virage"),
         ("b", "Derrière les véhicules en stationnement"),
         ("c", "A proximité d’une intersection")],
        "Réponse a-c", 94, tags=["multi-reponses"]))

    questions.append(q(429, 4, "Stationnement hors agglomération", "Sur une route hors agglomération, les véhicules peuvent stationner :",
        [("a", "Sur le côté droit seulement"),
         ("b", "Sur le côté droit ou sur le côté gauche"),
         ("c", "Sur les accotements"),
         ("d", "Sur le côté gauche seulement")],
        "Réponse b-c", 95, tags=["multi-reponses"]))

    questions.append(q(430, 4, "Stationnement rue à sens unique", "Dans une rue à sens unique, les véhicules peuvent stationner :",
        [("a", "Sur le côté droit seulement"),
         ("b", "Sur le côté droit ou sur le côté gauche"),
         ("c", "Sur le côté gauche seulement")],
        "Réponse b", 95))

    questions.append(q(431, 4, "Virage serré paramètres", "A l’approche d’un virage à courbure très prononcée et bordé d’arbres, je dois tenir compte de :",
        [("a", "La force centrifuge"),
         ("b", "L’adhérence"),
         ("c", "La visibilité")],
        "Réponses a-b-c", 95, tags=["multi-reponses"]))

    questions.append(q(432, 4, "Vitesse en virage adhérence", "Dans un virage pour une bonne adhérence des pneus, je dois rouler :",
        [("a", "En deuxième vitesse"),
         ("b", "En troisième vitesse"),
         ("c", "En quatrième vitesse")],
        "Réponse a", 95))

    questions.append(q(433, 4, "Ligne jaune continue trottoir", "La ligne jaune continue sur la bordure du trottoir :",
        [("a", "Interdit le stationnement"),
         ("b", "Autorise l’arrêt"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponse a", 95))

    questions.append(q(434, 4, "Ligne jaune discontinue trottoir", "La ligne jaune discontinue sur la bordure du trottoir :",
        [("a", "Interdit le stationnement"),
         ("b", "Autorise l’arrêt"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponse a-b", 95, tags=["multi-reponses"]))

    questions.append(q(435, 4, "Risques virage à vive allure", "Quels sont les risques auxquels je m’expose en abordant un virage à vive allure ?",
        [("a", "Je risque de déraper et de me retrouver hors de la chaussée"),
         ("b", "Je risque de déraper et de heurter l’usager venant en sens inverse"),
         ("c", "Je risque de casser le pare-brise à cause du vent latéral")],
        "Réponses a-b", 95, tags=["multi-reponses"]))

    questions.append(q(436, 4, "Précautions pour virage", "Quelles précautions prendre pour aborder un virage ?",
        [("a", "Je passe rapidement en tenant fortement mon volant"),
         ("b", "Je maintiens ma vive allure en serrant fortement mon volant"),
         ("c", "Je réduis ma vive allure en maintenant ma droite")],
        "Réponse c", 96))

    questions.append(q(437, 4, "Ligne jaune brisée bordure", "La ligne jaune brisée en bordure de la chaussée :",
        [("a", "Interdit le dépassement"),
         ("b", "Autorise le dépassement"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponse c", 96))

    questions.append(q(438, 4, "Stationnement rase campagne", "Sur une route en rase campagne les véhicules peuvent stationner :",
        [("a", "Sur le côté droit seulement"),
         ("b", "Sur le côté droit ou sur le côté gauche"),
         ("c", "Sur le côté gauche seulement")],
        "Réponse b", 96))

    questions.append(q(439, 4, "Prendre un usager arrêt", "Pour prendre un usager de la route, je m’arrête :",
        [("a", "Sur la chaussée avec clignotant"),
         ("b", "Sur l’accotement avec les feux de détresse"),
         ("c", "Avec mon clignotant droit en me positionnant sur l’accotement"),
         ("d", "Avec mon clignotant droit en serrant ma droite")],
        "Réponse c-d", 96, tags=["multi-reponses"]))

    questions.append(q(440, 4, "Immobilisation prise directe", "Quelle est la toute première opération à effectuer par le conducteur pour immobiliser son véhicule roulant en prise directe :",
        [("a", "Débrayer"),
         ("b", "Freiner"),
         ("c", "Mettre le levier au point mort")],
        "Réponse b", 96, exp="On commence par freiner pour ralentir le véhicule, puis on débraye avant l'arrêt complet pour ne pas caler."))

    questions.append(q(441, 4, "Obstacle inopiné vive allure", "A la vue d’un obstacle inopiné à vive allure :",
        [("a", "Je débraie et je freine"),
         ("b", "Je freine en bloquant les roues"),
         ("c", "Je freine franchement et je débraie au dernier moment")],
        "Réponse c", 96, exp="Freiner franchement utilise le frein moteur ; débrayer au dernier moment évite de caler tout en raccourcissant la distance."))

    questions.append(q(442, 4, "Endroit pour demi-tour", "Où peut-on faire un demi-tour ?",
        [("a", "Sur un pont"),
         ("b", "Sur une chaussée à sens unique"),
         ("c", "Dans un virage"),
         ("d", "Sur une chaussée à double sens de circulation")],
        "Réponse d", 96))

    questions.append(q(443, 4, "Endroit pour marche arrière", "Où peut-on faire la marche arrière ?",
        [("a", "Sur un pont"),
         ("b", "Sur une chaussée à sens unique"),
         ("c", "Sur l’accotement ou sur le trottoir")],
        "Réponse b", 97))

    questions.append(q(444, 4, "Marche arrière sens interdit", "En marche arrière, peut-on rentrer dans un sens interdit ?",
        [("a", "Oui"), ("b", "Non")],
        "Réponse b", 97, exp="Il est strictement interdit de pénétrer dans un sens interdit, en marche avant comme en marche arrière."))

    questions.append(q(445, 4, "Peinture jaune continue trottoir", "La peinture jaune continue sur la bordure du trottoir signifie que :",
        [("a", "L’arrêt et le stationnement sont interdits jusqu’à la prochaine intersection"),
         ("b", "L’arrêt et le stationnement sont interdits à la hauteur de ce trottoir"),
         ("c", "Seul l’arrêt est autorisé")],
        "Réponse b", 97))

    questions.append(q(446, 4, "Distance d'arrêt 81 mètres vitesse", "Après avoir heurté un cycliste, je freine et m’arrête après 81 mètres. Je roulais donc à quelle vitesse ?",
        [("a", "60 km/h"),
         ("b", "90 km/h"),
         ("c", "70 km/h")],
        "Réponse b", 97, tags=["chiffre"], exp="Distance d'arrêt de 81 mètres correspond à 90 km/h (9 x 9 = 81)."))

    questions.append(q(447, 4, "Facteurs distance de freinage", "La distance de freinage dépend :",
        [("a", "Du type de revêtement"),
         ("b", "Du temps de réaction"),
         ("c", "De la vitesse"),
         ("d", "De l’état des pneumatiques"),
         ("e", "De l’état des amortisseurs")],
        "Réponses a-c-d", 97, tags=["multi-reponses"]))

    questions.append(q(448, 4, "Facteurs augmentant temps de réaction", "Quels sont les facteurs qui augmentent le temps de réaction ?",
        [("a", "La fatigue"),
         ("b", "L’état d’ivresse"),
         ("c", "Le manque de visibilité"),
         ("d", "L’état des pneumatiques")],
        "Réponses a-b", 97, tags=["multi-reponses"]))

    questions.append(q(449, 4, "Freinage temps de pluie", "Par temps de pluie, pour m’arrêter j’appuie sur la pédale de frein :",
        [("a", "Aussi fort que quand la chaussée est sèche"),
         ("b", "Moins fort que quand la chaussée est sèche"),
         ("c", "Plus fort que quand la chaussée est sèche")],
        "Réponse b", 97, exp="Sur chaussée mouillée, un appui trop violent entraîne le blocage des roues et le dérapage."))

    questions.append(q(450, 4, "Usage des zébras", "Les zébras sont réservés pour :",
        [("a", "Le stationnement d’urgence"),
         ("b", "L’arrêt d’urgence"),
         ("c", "Tourner et changer de direction"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 98))

    questions.append(q(451, 4, "Réduire sa vitesse circonstances", "Je dois réduire ma vitesse :",
        [("a", "A la vue d’un panneau de limitation de vitesse"),
         ("b", "Pendant le dépassement"),
         ("c", "En passant d’une zone éclairée à une zone d’ombre"),
         ("d", "A la sortie d’une agglomération"),
         ("e", "A l’approche d’une intersection")],
        "Réponse a-c-e", 98, tags=["multi-reponses"]))

    questions.append(q(452, 4, "Panneau B43 vitesses", "A la vue du panneau B43 :",
        [("a", "Je respecte une vitesse de 30 km/h obligatoirement"),
         ("b", "Je peux faire plus de 30 km/h"),
         ("c", "Je peux faire moins de 30 km/h")],
        "Réponse b-c", 98, img="B43", tags=["multi-reponses"]))

    questions.append(q(458, 4, "Voie de stockage", "La voie de stockage permet aux conducteurs de tourner :",
        [("a", "A gauche sans gêner les véhicules venant en sens inverse"),
         ("b", "A droite sans gêner les véhicules venant en sens inverse"),
         ("c", "Au milieu sans gêner les véhicules venant en sens inverse")],
        "Réponse a", 99, exp="La voie de stockage centrale permet de ralentir et d'attendre pour tourner à gauche sans bloquer le flux principal."))

    questions.append(q(459, 4, "Pistes cyclables utilisation", "Sur les bandes et les pistes cyclables :",
        [("a", "Les automobilistes peuvent s’arrêter pour prendre un passager"),
         ("b", "Les piétons peuvent circuler"),
         ("c", "Les autos peuvent stationner en cas de panne"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 99))

    questions.append(q(460, 4, "Intervalle de sécurité 90 km/h", "Pour suivre un véhicule qui roule à 90 km/h l’intervalle minimal de sécurité à conserver derrière ce véhicule est de :",
        [("a", "10m environ"),
         ("b", "15m environ"),
         ("c", "25m environ")],
        "Réponse c", 99, tags=["chiffre"]))

    questions.append(q(461, 4, "Adhérence au début de la pluie", "Il commence à pleuvoir, l’adhérence de mes pneumatiques sur la chaussée est :",
        [("a", "Aussi bonne que s’il avait plu toute la journée"),
         ("b", "Moins bonne que s’il avait plu toute la journée"),
         ("c", "Meilleure que s’il avait plu toute la journée")],
        "Réponse b", 99, exp="Au début de la pluie, l'eau mélangée aux poussières et résidus d'huile forme une boue très glissante (verglas d'été)."))

    questions.append(q(462, 4, "Bifurcation autoroutière", "La bifurcation, c’est la division d’une autoroute en :",
        [("a", "Quatre autoroutes"),
         ("b", "Deux autoroutes"),
         ("c", "Cinq autoroutes"),
         ("d", "Trois autoroutes")],
        "Réponse b", 99))

    questions.append(q(463, 4, "Contrôle stationnement durée limitée", "Le contrôle de la durée d’un stationnement à une durée limitée peut se faire :",
        [("a", "Par horodateur"),
         ("b", "Par disque de stationnement"),
         ("c", "Par parcmètre")],
        "Réponse b", 100, tags=["piege"]))

    questions.append(q(464, 4, "Rôle de la rétrogradation", "La rétrogradation permet de :",
        [("a", "Ralentir le véhicule dans une descente"),
         ("b", "Repartir après un ralentissement"),
         ("c", "Arrêter le véhicule en circulation")],
        "Réponse a-b", 100, tags=["multi-reponses"]))

    questions.append(q(465, 4, "Position en marche normale", "En marche normale :",
        [("a", "Je dois rouler au milieu de la chaussée"),
         ("b", "Je dois rouler à gauche de la chaussée"),
         ("c", "Je dois rouler près du bord droit de la chaussée autant que la permettent son profil et son état"),
         ("d", "Je dois rouler sur le trottoir")],
        "Réponse c", 100))

    questions.append(q(466, 4, "Éclatement d'un pneu", "En cas d’éclatement d’un pneumatique :",
        [("a", "Je freine fortement pour m’arrêter"),
         ("b", "Je décélère progressivement en maintenant la trajectoire"),
         ("c", "Je contre braque rapidement pour éviter une tête à queue")],
        "Réponse b", 100, exp="Ne surtout pas piler : relâcher l'accélérateur, tenir fermement le volant et décélérer en douceur."))

    questions.append(q(467, 4, "Dérapage sur chaussée glissante", "Le conducteur d’un véhicule qui dérape sur une chaussée glissante doit :",
        [("a", "Freiner fort pour stopper le véhicule"),
         ("b", "Braquer calmement pour ramener le véhicule dans sa trajectoire"),
         ("c", "Accélérer franchement pour redonner de l’adhérence aux roues arrière")],
        "Réponse b", 100))

    questions.append(q(468, 4, "Sens unique C12 bis", "Que signifie le panneau C12 ?",
        [("a", "Obligation d’aller tout droit après le panneau"),
         ("b", "Obligation d’aller tout droit jusqu’à la prochaine intersection"),
         ("c", "Circulation à sens unique")],
        "Réponse c", 100, img="C12"))

    questions.append(q(469, 4, "Lieux de stationnement dangereux", "Le stationnement est dangereux :",
        [("a", "Derrière les véhicules en stationnement"),
         ("b", "A proximité d’une intersection"),
         ("c", "Sur les accotements"),
         ("d", "Au sommet de côte"),
         ("e", "Dans les virages")],
        "Réponse b-d-e", 100, tags=["multi-reponses"]))

    questions.append(q(470, 4, "Tourner à gauche chaussée double sens", "A bord d’un véhicule de tourisme pour, tourner à gauche sur une chaussée à double sens, je dois :",
        [("a", "Mettre le clignotant à gauche et céder le passage à droite"),
         ("b", "Ralentir et serrer la gauche"),
         ("c", "Tourner sans respecter la priorité à droite")],
        "Réponse a", 101))

    # CHAPITRE V: ROUTE POUR AUTOMOBILE ET AUTOROUTE (Questions 471 to 507)
    questions.append(q(471, 5, "Accès à l'autoroute", "Comment accéder à l’autoroute ?",
        [("a", "Par voie d’accès"),
         ("b", "Par voie de décélération"),
         ("c", "Par voie d’accélération")],
        "Réponse a-c", 101, tags=["multi-reponses"]))

    questions.append(q(472, 5, "Perte de priorité route grande circulation", "La route à grande circulation perd sa priorité :",
        [("a", "En agglomération"),
         ("b", "A l’entrée d’une ville"),
         ("c", "En dehors de l’agglomération")],
        "Réponse a-b", 101, tags=["multi-reponses"]))

    questions.append(q(473, 5, "Permis moins d'un an vitesse", "Quelle est la vitesse maximale sur une route à grande circulation pour un candidat dont le permis a moins d’un an d’âge ?",
        [("a", "60 km/h"),
         ("b", "90 km/h"),
         ("c", "120 km/h")],
        "Réponse b", 101, tags=["chiffre"]))

    questions.append(q(474, 5, "Rôle de la voie d'accélération", "A quoi sert la voie d’accélération ?",
        [("a", "Permet d’atteindre la vitesse minimale autorisée sur autoroute"),
         ("b", "Permet de quitter l’autoroute"),
         ("c", "Permet de dépasser les usagers lents")],
        "Réponse a", 101))

    questions.append(q(475, 5, "Définition arrêt d'urgence", "Que signifie l’arrêt d’urgence ?",
        [("a", "Immobilisation forcée"),
         ("b", "Arrêt pour faire descendre un passager"),
         ("c", "Arrêt d’autobus")],
        "Réponse a", 101))

    questions.append(q(476, 5, "Usage de la bande d'arrêt d'urgence", "La bande d’arrêt d’urgence est utilisée :",
        [("a", "Pour s’arrêter en cas de panne"),
         ("b", "Pour s’arrêter et prendre un passager"),
         ("c", "Pour s’arrêter en cas de malaise")],
        "Réponse a-c", 101, tags=["multi-reponses"]))

    questions.append(q(477, 5, "Manœuvres interdites autoroute", "Quelles sont les manœuvres interdites sur autoroute ?",
        [("a", "Dépassement"),
         ("b", "Demi-tour"),
         ("c", "Marche arrière")],
        "Réponse b-c", 101, tags=["multi-reponses"], exp="Demi-tour et marche arrière sont formellement prohibés sur autoroute."))

    questions.append(q(478, 5, "Cédez le passage voie d'accélération", "Le panneau triangle pointe en bas au début d’une voie d’accélération :",
        [("a", "oblige les usagers circulant sur autoroute à me céder le passage"),
         ("b", "oblige à céder le passage aux usagers de l’autoroute"),
         ("c", "oblige à marquer l’arrêt")],
        "Réponse b", 102))

    questions.append(q(479, 5, "Parties d'une rue", "Les différentes parties d’une rue sont :",
        [("a", "Chaussée, accotement"),
         ("b", "Chaussée, terre-plein central, accotement"),
         ("c", "Chaussée, trottoirs"),
         ("d", "Terre plein-central, chaussée, trottoirs")],
        "Réponses c-d", 102, tags=["multi-reponses"]))

    questions.append(q(480, 5, "Trottoir définition", "Le trottoir est la partie d’une rue réservée :",
        [("a", "Pour les vendeuses"),
         ("b", "Pour les piétons"),
         ("c", "Pour le dépassement en cas de bouchon")],
        "Réponse b", 102))

    questions.append(q(481, 5, "Chaussée définition", "La chaussée est la partie d’une route réservée :",
        [("a", "A la circulation de gros camions uniquement"),
         ("b", "A la circulation des véhicules"),
         ("c", "A la circulation des taxis uniquement")],
        "Réponse b", 102))

    questions.append(q(482, 5, "Voie définition", "La voie est :",
        [("a", "Une partie de la chaussée ou le dépassement est possible"),
         ("b", "Une partie de la chaussée réservée pour la circulation des véhicules"),
         ("c", "Une partie de la chaussée réservée pour la circulation dans un sens")],
        "Réponses b-c", 102, tags=["multi-reponses"]))

    questions.append(q(483, 5, "Ennui mécanique autoroute stationnement", "Où doit-on stationner en cas d’ennui mécanique sur l’autoroute ?",
        [("a", "Sur le terre- plein"),
         ("b", "Sur la bande d’arrêt d’urgence"),
         ("c", "Sur l’aire de repos")],
        "Réponse b-c", 102, tags=["multi-reponses"]))

    questions.append(q(484, 5, "Vitesse max autoroute législation", "La vitesse maximale autorisée sur une autoroute est :",
        [("a", "90km/h"),
         ("b", "200km/h"),
         ("c", "60km/h"),
         ("d", "Fonction de la législation en vigueur dans chaque pays")],
        "Réponse d", 102, exp="Le manuel DGTT précise que la vitesse maximale autorisée dépend de la réglementation locale en vigueur."))

    questions.append(q(485, 5, "Vitesse max route pour automobile", "La vitesse maximale autorisée sur une route pour automobile est :",
        [("a", "90km/h"),
         ("b", "130km/h"),
         ("c", "110km/h"),
         ("d", "Fonction de la législation en vigueur dans chaque pays")],
        "Réponse d", 103))

    questions.append(q(486, 5, "Vitesse max agglomération", "La vitesse maximale autorisée en agglomération est :",
        [("a", "70km/h"),
         ("b", "50km/h"),
         ("c", "90km/h"),
         ("d", "100km/h")],
        "Réponse b", 103, tags=["chiffre"], exp="En agglomération au Bénin : 50 km/h maximum pour tous les véhicules."))

    questions.append(q(487, 5, "Panne de carburant autoroute", "Je suis en panne de carburant sur l’autoroute :",
        [("a", "Je vais à pied chercher du carburant à la station-service la plus proche"),
         ("b", "Je me fais remorquer par un autre usager jusqu’à la station-service la plus proche"),
         ("c", "J’utilise la cabine d’appel d’urgence pour me faire dépanner"),
         ("d", "Je place mon triangle de pré-signalisation")],
        "Réponse c", 103, exp="Sur autoroute, interdiction de marcher le long de la bande ou de se faire remorquer par un particulier : utiliser la borne d'urgence."))

    questions.append(q(488, 5, "Panne mécanique autoroute", "Mon véhicule tombe en panne sur l’autoroute :",
        [("a", "je gare sur la bande d’arrêt d’urgence"),
         ("b", "J’attends un véhicule de dépannage"),
         ("c", "Je fais du stop pour demander de l’aide"),
         ("d", "Je vais à pied jusqu'à la prochaine borne d’appel")],
        "Réponse a-d", 103, tags=["multi-reponses"]))

    questions.append(q(489, 5, "Circulation sur BAU", "La circulation sur les bandes d’arrêt d’urgence de l’autoroute est autorisée :",
        [("a", "Aux ambulances effectuant un transport urgent de blessés"),
         ("b", "A tous les véhicules en cas d’embouteillage"),
         ("c", "Aux services d’entretien se rendant sur un lieu d’intervention"),
         ("d", "Aux véhicules prioritaires en mission")],
        "Réponses a-c-d", 103, tags=["multi-reponses"]))

    questions.append(q(490, 5, "Espacement bornes d'appel autoroute", "Sur autoroute les bornes d’appel d’urgence sont placées à :",
        [("a", "tous les kilomètres"),
         ("b", "tous les deux kilomètres"),
         ("c", "tous les trois kilomètres"),
         ("d", "tous les cinq kilomètres")],
        "Réponse b", 103, tags=["chiffre"], exp="Les bornes SOS sont implantées tous les 2 kilomètres."))

    questions.append(q(491, 5, "Sortie autoroute comportement", "Quel doit être le comportement d’un conducteur à la sortie d’une autoroute ?",
        [("a", "réduire sa vitesse"),
         ("b", "se réadapter à la vitesse normale"),
         ("c", "tenir compte des intersections et de la présence des autres usagers"),
         ("d", "utiliser son avertisseur sonore pour dégager la voie")],
        "Réponse a, b, c", 104, tags=["multi-reponses"]))

    questions.append(q(492, 5, "Usagers interdits autoroute", "L’accès à l’autoroute est interdit à certaines catégories d’usagers : lesquels ?",
        [("a", "piétons"),
         ("b", "cyclomoteurs"),
         ("c", "véhicules agricoles"),
         ("d", "cavaliers"),
         ("e", "véhicules lents")],
        "Réponse a, b, c, d, e", 104, tags=["multi-reponses"]))

    questions.append(q(493, 5, "Interdiction accès autoroute", "Quels sont les usagers dont l’accès à l’autoroute est interdit ?",
        [("a", "piétons"),
         ("b", "motocyclette"),
         ("c", "cavaliers"),
         ("d", "véhicules de tourisme"),
         ("e", "véhicules lents")],
        "Réponse a, c, e", 104, tags=["multi-reponses"]))

    questions.append(q(494, 5, "Changement de voie à droite", "Pour effectuer un changement de voie à droite, je contrôle :",
        [("a", "le rétroviseur droit"),
         ("b", "le rétroviseur gauche"),
         ("c", "en vision directe, à droite"),
         ("d", "le rétroviseur intérieur")],
        "Réponse : a, d", 104, tags=["multi-reponses"]))

    questions.append(q(495, 5, "Circulation en files", "La circulation est établie en files, je peux changer de voie pour :",
        [("a", "prendre une voie qui circule plus vite"),
         ("b", "préparer un changement de direction")],
        "Réponse b", 104, exp="En file ininterrompue, le slalom est interdit : on ne change de voie que pour tourner."))

    questions.append(q(496, 5, "Jonction d'autoroute", "Une jonction d’autoroute est :",
        [("a", "Le raccordement de deux autoroutes"),
         ("b", "La séparation d’une autoroute en deux branches"),
         ("c", "Le raccordement d’une autoroute et d’une voie d’insertion")],
        "Réponse : a", 104))

    questions.append(q(497, 5, "Caractéristiques de l'autoroute", "Une autoroute est toujours une route :",
        [("a", "A sens unique"),
         ("b", "A trois voies de circulation"),
         ("c", "Interdite aux piétons, cyclistes et cyclomotoristes")],
        "Réponse : a-c", 104, tags=["multi-reponses"]))

    questions.append(q(498, 5, "Voie pour véhicules lents", "Une voie pour véhicules lents est réservée :",
        [("a", "aux poids-lourds uniquement"),
         ("b", "aux véhicules dont la vitesse est inférieure à 60km/h"),
         ("c", "aux véhicules dont la vitesse est inférieure à 80 km/h")],
        "Réponse : b", 105, tags=["chiffre"], exp="La voie pour véhicules lents est réservée à ceux dont la vitesse ne dépasse pas 60 km/h."))

    questions.append(q(499, 5, "Dépassement autoroute 3 voies", "Sur les chaussées d’autoroute à 3 voies, il est permis de dépasser :",
        [("a", "Par la droite"),
         ("b", "Par la gauche"),
         ("c", "Du côté souhaité")],
        "Réponse : b", 105))

    questions.append(q(500, 5, "Routes à accès réglementé", "Les routes à accès règlementé sont toutes :",
        [("a", "A chaussées séparées et à sens unique"),
         ("b", "A vitesse limité à 110 km/h"),
         ("c", "A chaussées à double sens"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse : d", 105))

    questions.append(q(501, 4, "Types de stationnement", "Quels sont les types de stationnement ?",
        [("a", "Bataille – créneau – perpendiculaire"),
         ("b", "Bataille – épi – créneau"),
         ("c", "Epi – créneau – oblique"),
         ("d", "En double file – épi – parallèle")],
        "Réponse b", 105))

    questions.append(q(502, 5, "Rôle du terre-plein central", "A quoi sert le terre-plein central ?",
        [("a", "A stationner"),
         ("b", "A exposer les marchandises"),
         ("c", "A faire un demi-tour"),
         ("d", "A séparer deux chaussées")],
        "Réponse d", 105))

    questions.append(q(503, 4, "Quitter stationnement", "En quittant le stationnement en marche normale pour intégrer la circulation, je dois :",
        [("a", "Utiliser le rétroviseur de droite"),
         ("b", "Mettre le clignotant de gauche, utiliser le rétroviseur de gauche et m’engager avec prudence"),
         ("c", "M’engager rapidement")],
        "Réponse b", 105))

    questions.append(q(504, 4, "Sortir d'un garage priorité", "En sortant d’un garage pour intégrer la circulation, je dois :",
        [("a", "Céder le passage aux usagers venant de la droite seulement"),
         ("b", "Céder le passage aux usagers venant de la gauche seulement"),
         ("c", "Céder le passage aux usagers venant de la droite et de la gauche")],
        "Réponse c", 105, exp="Sortie de propriété ou garage = perte totale de priorité envers tous les usagers de la voie."))

    questions.append(q(505, 4, "Sortie garage précaution", "En sortant d’un garage pour intégrer la circulation, quelle est la toute première précaution à prendre ?",
        [("a", "Jeter un coup d’œil à gauche"),
         ("b", "Klaxonner"),
         ("c", "Jeter un coup d’œil à droite")],
        "Réponse a", 106, exp="En quittant un garage, les premiers véhicules rencontrés viennent de la gauche sur notre voie."))

    questions.append(q(506, 4, "Descente d'une pente freins", "En descendant une pente, on doit utiliser :",
        [("a", "Le frein à pied seulement"),
         ("b", "Le frein à pied et le frein moteur"),
         ("c", "Le frein à pied et le frein à main")],
        "Réponse b", 106))

    questions.append(q(507, 4, "Puissance frein moteur descente", "Dans une descente, le frein à moteur sera puissant si :",
        [("a", "Je reste en quatrième vitesse"),
         ("b", "Je passe en cinquième vitesse"),
         ("c", "Je passe en deuxième")],
        "Réponse c", 106, exp="Plus le rapport de boîte est bas (ex. 2ème), plus la résistance du moteur est élevée."))

    return questions

if __name__ == '__main__':
    qs = get_chapitre4_5_questions()
    print(f"Chapitre 4 & 5 loaded: {len(qs)} questions")
