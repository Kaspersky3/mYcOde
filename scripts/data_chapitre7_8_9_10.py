# Chapter 7, 8, 9, 10: Motos (A), Permis B, Poids Lourds (C/C1), Transports en commun (D)
# Extracted from DGTT 2011 pages 130 to 157

def get_chapitre7_8_9_10_questions():
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
        if chap == 8:
            t.append("categorie-b")
        else:
            t.append("autres-categories")
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

    # CHAPITRE VII: MOTOS A1 A2 A3 (Q646 to Q678)
    questions.append(q(646, 7, "Passager moto", "Sur une motocyclette, le passager :",
        [("a", "Peut-être assis devant le conducteur"),
         ("b", "Peut-être assis dans la position dite « en amazone »"),
         ("c", "Doit être assis sur le siège arrière"),
         ("d", "Doit faire corps avec la moto et son conducteur")],
        "Réponse c-d", 130, tags=["multi-reponses"]))

    questions.append(q(647, 7, "Panne moto trottoir", "En cas de panne de ma motocyclette :",
        [("a", "Je peux trainer ma moto sur le trottoir, le moteur arrêté"),
         ("b", "Je ne peux pas trainer ma moto sur le trottoir, le moteur arrêté"),
         ("c", "Je peux la garer sur le trottoir et attendre un dépanneur")],
        "Réponse a", 130))

    questions.append(q(648, 7, "Circulation files moto", "Dans une circulation en files ininterrompues :",
        [("a", "Je peux me faufiler entre les véhicules"),
         ("b", "Je peux me faufiler entre les véhicules si la circulation s’arrête"),
         ("c", "Je dois rester dans ma file sauf pour préparer un changement de direction")],
        "Réponse c", 130))

    questions.append(q(649, 7, "Passage à niveau deux-roues", "Avec mon véhicule à deux roues, je peux traverser une voie ferrée :",
        [("a", "En passant par le portillon d’une barrière fermée avant le passage d’un train"),
         ("b", "En passant les demi-barrières fermées avant le passage du train"),
         ("c", "Après le relèvement de la barrière")],
        "Réponse c", 130))

    questions.append(q(650, 7, "Clignotant obligatoire", "Le clignotant est obligatoire :",
        [("a", "Pour les cyclomoteurs"),
         ("b", "Pour les motocyclettes"),
         ("c", "Pour tous les véhicules à deux roues"),
         ("d", "Pour les automobiles seulement")],
        "Réponse b", 130))

    questions.append(q(651, 7, "Cylindrée permis A1", "Avec mon permis de conduire catégorie A1, je peux conduire des motocyclettes dont la cylindrée :",
        [("a", "N’excède pas 75cm3"),
         ("b", "Excède 75cm3"),
         ("c", "Est égale à 100cm3")],
        "Réponse a", 130, tags=["chiffre"]))

    questions.append(q(652, 7, "Cylindrée permis A2", "Avec mon permis de conduire catégorie A2, je peux conduire des motocyclettes dont la cylindrée :",
        [("a", "N’excède pas 450cm3"),
         ("b", "Excède 400cm3"),
         ("c", "Est inférieur à 400cm3"),
         ("d", "Est égale à 400cm3")],
        "Réponse c-d", 130, tags=["chiffre", "multi-reponses"]))

    questions.append(q(653, 7, "Cylindrée permis A3", "Avec mon permis de conduire catégorie A3, je peux conduire des motocyclettes dont la cylindrée :",
        [("a", "N’excède pas 450cm3"),
         ("b", "Excède 400cm3"),
         ("c", "Est inférieure à 400cm3"),
         ("d", "Est égale à 400cm3")],
        "Réponse a-b-c-d", 131, tags=["ambiguite", "multi-reponses"]))

    questions.append(q(654, 7, "Contrôles moto avant départ", "Quels sont les contrôles de niveau à effectuer avant le départ sur les motocyclettes dont la cylindrée est supérieure ou égale à 400cm3 ?",
        [("a", "Niveau d’huile à moteur"),
         ("b", "Eau dans le radiateur"),
         ("c", "Essence dans le réservoir"),
         ("d", "Eau du bocal de l’essuie-glace")],
        "Réponse a-b-c", 131, tags=["multi-reponses"]))

    questions.append(q(655, 7, "Position moto contrôle niveau", "Dans quelle position met-on la motocyclette pour effectuer les contrôles de niveau ?",
        [("a", "Sur la béquille centrale"),
         ("b", "Sur la béquille latérale"),
         ("c", "Couchée")],
        "Réponse a", 131))

    questions.append(q(656, 7, "Attention en longeant stationnement", "En longeant les véhicules en stationnement, à quoi doit-on faire attention ?",
        [("a", "Aux piétons qui pourraient surgir"),
         ("b", "Aux véhicules qui pourraient surgir"),
         ("c", "Aux portières qui pourraient s’ouvrir"),
         ("d", "Aux véhicules qui pourraient quitter leur stationnement")],
        "Réponse a-c-d", 131, tags=["multi-reponses"]))

    questions.append(q(657, 7, "Conduite nouvelle moto", "Les précautions à prendre pour la conduite d’une nouvelle motocyclette :",
        [("a", "S’habituer progressivement"),
         ("b", "Augmenter la distance de sécurité"),
         ("c", "Réduire la distance de sécurité"),
         ("d", "Adopter une bonne position de conduite, de freinage et de tenue de route")],
        "Réponse a-b-d", 131, tags=["multi-reponses"]))

    questions.append(q(658, 7, "Contrôles avant chaque départ", "Quels sont les contrôles à effectuer avant chaque départ ?",
        [("a", "Position des béquilles"),
         ("b", "Bon ajustement du casque (conducteur et passager)"),
         ("c", "Resserrage des rayons"),
         ("d", "Réglage des rétroviseurs")],
        "Réponse a-b-d", 131, tags=["multi-reponses"]))

    questions.append(q(659, 7, "Types de casques", "Quels sont les différents types de casques pour les motocyclettes et les cyclomoteurs ?",
        [("a", "Casque à couverture ignifugée"),
         ("b", "Casque intégral"),
         ("c", "Casque enveloppant"),
         ("d", "Casque étoilé")],
        "Réponse b-c", 132, tags=["multi-reponses"]))

    questions.append(q(660, 7, "Position conducteur moto", "Quelle est la bonne position d’un conducteur à motocyclette ?",
        [("a", "Etre bien assis sur la selle"),
         ("b", "Avoir les bras légèrement fléchis"),
         ("c", "Avoir le cou raide"),
         ("d", "Garder les genoux contre le réservoir")],
        "Réponse a-b-d", 132, tags=["multi-reponses"]))

    questions.append(q(661, 7, "Âge minimal permis A1", "Quel est l’âge minimum pour un candidat à l’examen du permis de conduire A1 ?",
        [("a", "14ans"), ("b", "16ans"), ("c", "17ans")],
        "Réponse b", 132, tags=["chiffre"], exp="16 ans pour la catégorie A1 (cyclomoteurs/vélomoteurs jusqu'à 75 cm³)."))

    questions.append(q(662, 7, "Feu stop moto", "Le feu stop est obligatoire :",
        [("a", "Sur les cyclomoteurs"),
         ("b", "Sur les motocyclettes"),
         ("c", "Sur tous les véhicules à deux roues")],
        "Réponse b", 132))

    questions.append(q(663, 7, "Rétroviseur moto", "Le rétroviseur est-il obligatoire pour les motocyclettes ?",
        [("a", "Oui"), ("b", "Non")],
        "Réponse a", 132))

    questions.append(q(664, 7, "Nombre de passagers moto", "Combien de passagers un conducteur de deux roues peut-il transporter ?",
        [("a", "deux"), ("b", "un"), ("c", "trois")],
        "Réponse b", 132, tags=["chiffre"], exp="Un seul passager adulte assis à califourchon à l'arrière sur un siège prévu."))

    questions.append(q(665, 7, "Port du casque deux-roues", "Le port de casque est obligatoire sur les véhicules à deux roues :",
        [("a", "Seulement quand je remorque un passager"),
         ("b", "Si je suis seul"),
         ("c", "Pour tous les occupants")],
        "Réponse b-c", 132, tags=["multi-reponses"]))

    questions.append(q(666, 7, "Protection du casque", "Le port de casque protège contre :",
        [("a", "Le soleil et la pluie"),
         ("b", "Le traumatisme crânien"),
         ("c", "La poussière")],
        "Réponse b", 132))

    questions.append(q(667, 7, "Âge minimal permis A2", "Quel est l’âge minimum du candidat à l’examen de permis de conduire A2 ?",
        [("a", "15ans"), ("b", "20ans"), ("c", "18ans")],
        "Réponse c", 133, tags=["chiffre"], exp="18 ans pour la catégorie A2 (motos de 75 à 400 cm³)."))

    questions.append(q(668, 7, "Enfant de moins de 5 ans moto", "Pour le transport d’un enfant de moins de 5ans sur une motocyclette il faut :",
        [("a", "Avoir un simple siège"),
         ("b", "Avoir un siège muni de courroie-attache"),
         ("c", "Bien régler son casque")],
        "Réponse b", 133))

    questions.append(q(669, 7, "Âge minimal permis A3", "Quel est l’âge minimum pour un candidat à l’examen de permis de conduire A3 ?",
        [("a", "17ans"), ("b", "18ans"), ("c", "21ans")],
        "Réponse c", 133, tags=["chiffre"], exp="21 ans pour la catégorie A3 (grosses cylindrées de plus de 400 cm³)."))

    questions.append(q(670, 7, "Panneau A21b cycliste", "Que signifie le panneau A21b ?",
        [("a", "Voie réservée au cycliste"),
         ("b", "Voie interdite au cycliste"),
         ("c", "Débouché de cycliste venant de gauche seulement")],
        "Réponse c", 133, img="A21b"))

    questions.append(q(671, 7, "Panneau B14(3) en moto", "Sur ma moto, à la vue du panneau B14(3) hors agglomération :",
        [("a", "Je peux rouler à plus de 60km/h"),
         ("b", "Je peux rouler à moins de 60km/h"),
         ("c", "Je peux rouler à 60km/h strictement"),
         ("d", "Je ne suis pas concerné par cette signalisation")],
        "Réponse b-c", 133, img="B14_3", tags=["multi-reponses"]))

    questions.append(q(672, 7, "Panonceau moto B14-3", "Le panneau B14-3 :",
        [("a", "concerne uniquement les conducteurs à moto"),
         ("b", "concerne tous les conducteurs sauf les motocyclistes"),
         ("c", "concerne aussi les 4 roues")],
        "Réponse a", 133, img="B14_3"))

    questions.append(q(673, 7, "Obligation casque circonstances", "Le port de casque est obligatoire :",
        [("a", "seulement en rase campagne ou la grande vitesse est possible"),
         ("b", "seulement en ville à cause du grand nombre de véhicules"),
         ("c", "seulement sur les voies pavées ou bitumées"),
         ("d", "rien de tout ce qui précède")],
        "Réponse d", 133, exp="Le casque est obligatoire partout et en tout temps, sur n'importe quel type de route."))

    questions.append(q(674, 7, "Circulation de front deux-roues", "La circulation à deux de front pour les véhicules à deux roues :",
        [("a", "Est autorisée sur les chaussées à double sens de circulation"),
         ("b", "Est autorisée sur les chaussées à sens unique de circulation"),
         ("c", "N’est pas autorisée"),
         ("d", "Est autorisée seulement sur les voies réservées aux véhicules à deux roues")],
        "Réponse c", 134))

    questions.append(q(675, 7, "Permis A2 cylindrée maximale", "Avec mon permis de conduire catégorie A2, je peux conduire des motocyclettes dont la cylindrée n’excède pas :",
        [("a", "200cm3"), ("b", "400cm3"), ("c", "600cm3")],
        "Réponse a-b", 134, tags=["multi-reponses"]))

    questions.append(q(676, 7, "Définition motocyclette", "Les motocyclettes sont des véhicules à deux roues :",
        [("a", "Avec moteur auxiliaire"),
         ("b", "Pourvus d’un moteur thermique"),
         ("c", "Dont la cylindrée ne dépasse pas 50cm3"),
         ("d", "Dont la cylindrée dépasse 50cm3")],
        "Réponse b-d", 134, tags=["multi-reponses"]))

    questions.append(q(677, 7, "Définition cyclomoteur", "Les cyclomoteurs sont des véhicules à deux roues :",
        [("a", "Pourvus d’un moteur thermique"),
         ("b", "Dont la cylindrée ne dépasse pas 50cm3"),
         ("c", "Dont la cylindrée dépasse 50cm3")],
        "Réponse b", 134))

    questions.append(q(678, 7, "Équipements obligatoires moto", "Sont obligatoires sur les motocyclettes :",
        [("a", "Les avertisseurs"),
         ("b", "les deux rétroviseurs"),
         ("c", "le rétroviseur gauche"),
         ("d", "le rétroviseur droit"),
         ("e", "le frein avant")],
        "Réponse a-c-e", 134, tags=["multi-reponses"]))

    # CHAPITRE VIII: PERMIS DE CONDUIRE CATEGORIE B (Q679 to Q688) - CŒUR CATÉGORIE B!
    questions.append(q(679, 8, "Manœuvre tourne à droite B", "Pour tourner à droite je dois :",
        [("a", "Accélérer"),
         ("b", "Mettre le clignotant"),
         ("c", "Ralentir")],
        "Réponse b-c", 136, tags=["multi-reponses"]))

    questions.append(q(680, 8, "Tourner à gauche double sens B", "Pour tourner à gauche sur une chaussée à double sens je dois :",
        [("a", "Serrer ma droite"),
         ("b", "Me déporter au milieu"),
         ("c", "Serrer ma gauche")],
        "Réponse b", 136, exp="Sur route à double sens, se placer au milieu sans empiéter sur le sens inverse."))

    questions.append(q(681, 8, "Remorque et permis E(B)", "Le PTAC de ma remorque est de 800kg ; le poids à vide de ma voiture est 700kg :",
        [("a", "pour tracter ma remorque je dois détenir le permis E (B)"),
         ("b", "je dois mettre à l’arrière de ma remorque une plaque d’immatriculation identique à celle de ma voiture"),
         ("c", "pour tracter ma remorque je dois détenir le permis C"),
         ("d", "ma remorque doit porter sa propre plaque d’immatriculation")],
        "Réponse a-d", 136, diff=2, tags=["multi-reponses", "piege", "chiffre"], exp="Le permis E(B) est requis car le PTAC de la remorque (800 kg) dépasse le poids à vide du véhicule tracteur (700 kg), et la remorque (>500 kg) a sa propre plaque et carte grise."))

    questions.append(q(682, 8, "Panneau 50 vitesse", "A la vue du panneau B14 :",
        [("a", "Je peux rouler à plus de 50km/h"),
         ("b", "Je ne peux pas rouler à moins de 50km/h"),
         ("c", "Je peux rouler à 50km/h strictement"),
         ("d", "Je ne suis pas concerné pas cette signalisation"),
         ("e", "Je peux rouler à moins de 50km/h")],
        "Réponse c-e", 136, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(683, 8, "Définition permis B véhicules", "Avec mon permis de conduire catégorie B :",
        [("a", "je peux conduire un véhicule dont le PTAC est inférieur ou égal à 3,5T"),
         ("b", "je peux conduire tous les véhicules"),
         ("c", "je ne peux conduire que les véhicules dont le PTAC est compris entre 3,5T et 18T"),
         ("d", "je peux conduire une camionnette dont le PTAC est égal ou inférieur à 3,5T")],
        "Réponse a-d", 136, tags=["multi-reponses", "chiffre"], exp="Le permis B autorise la conduite des véhicules de transport de personnes ou marchandises de PTAC <= 3,5 T et de 8 places passagers maximum."))

    questions.append(q(684, 8, "Type de véhicule permis B", "Avec le permis de conduire catégorie B, je peux conduire un véhicule :",
        [("a", "poids lourd"),
         ("b", "autobus"),
         ("c", "poids léger")],
        "Réponse c", 136))

    questions.append(q(685, 8, "Transport chargement long échelle", "Ma voiture mesure 4m de long, comment transporter de jour, une échelle de 5m ?",
        [("a", "Je fais dépasser l’échelle de 0,5m à l’avant et 0,5m à l’arrière"),
         ("b", "Je fais dépasser l’échelle de 1m à l’avant"),
         ("c", "Je fais dépasser l’échelle de 1m à l’arrière")],
        "Réponse c", 136, diff=2, tags=["piege", "chiffre"], exp="RÈGLE MAJEURE DU CODE : Le chargement ne doit JAMAIS dépasser à l'avant du véhicule (dépassement avant = 0 m). Tout dépassement se fait uniquement à l'arrière (max 3 m)."))

    questions.append(q(686, 8, "Vitesse conducteur novice 8 mois", "Mon permis de conduire a 8mois d’âge, je ne peux rouler à plus de :",
        [("a", "100km/h"),
         ("b", "120km/h"),
         ("c", "90km/h"),
         ("d", "60km/h")],
        "Réponse c", 137, tags=["chiffre"], exp="Pendant la période probatoire (permis de moins d'un an), la vitesse maximale sur route à grande circulation est plafonnée à 90 km/h."))

    questions.append(q(687, 8, "Panneau 50 vitesse bis", "A la vue du panneau B14 :",
        [("a", "Je peux rouler à plus de 50km/h"),
         ("b", "je peux rouler à moins de 50km/h"),
         ("c", "Je peux rouler à 50km/h strictement"),
         ("d", "Je ne suis pas concerné pas cette signalisation")],
        "Réponse b-c", 137, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(688, 8, "Carte grise propre remorque", "La remorque doit avoir sa propre carte grise si le PTAC est supérieur à :",
        [("a", "450kg"),
         ("b", "500kg"),
         ("c", "400kg")],
        "Réponse b", 137, tags=["chiffre"], exp="Dès que le PTAC d'une remorque dépasse 500 kg, elle doit posséder sa propre carte grise et sa propre immatriculation."))

    # CHAPITRE IX: PERMIS C ET C1 (Q689 to Q738)
    questions.append(q(689, 9, "Permis C1 âge", "Quel est l’âge minimal du candidat au permis de conduire catégorie C1 ?",
        [("a", "17ans"), ("b", "18ans"), ("c", "20ans"), ("d", "21ans")],
        "Réponse d", 139, tags=["chiffre"]))

    questions.append(q(690, 9, "Transports exceptionnels longueur", "Pour les transports exceptionnels la réglementation (concernant les pièces de grande longueur) prévoit que le chargement du véhicule isolé peut déborder de :",
        [("a", "3m au plus à l’avant et 5m à l’arrière"),
         ("b", "4m au plus à l’avant et 7m à l’arrière"),
         ("c", "0m à l’avant et 6m à l’arrière")],
        "Réponse a", 139))

    questions.append(q(691, 9, "Véhicule articulé définition", "Un véhicule articulé est composé :",
        [("a", "d’un véhicule tracteur et d’une remorque"),
         ("b", "d’un véhicule tracteur et d’une semi- remorque"),
         ("c", "d’un véhicule tracteur routier et d’une semi-remorque"),
         ("d", "d’un véhicule tracteur routier et d’une remorque")],
        "Réponse c", 139))

    questions.append(q(692, 9, "Train double définition", "Un train double est composé :",
        [("a", "d’un tracteur et d’une remorque"),
         ("b", "d’un tracteur routier et de deux semi-remorques"),
         ("c", "d’un véhicule articulé et d’une semi-remorque"),
         ("d", "d’un tracteur et d’une semi-remorque")],
        "Réponse b-c", 139, tags=["multi-reponses"]))

    questions.append(q(693, 9, "Longueur max véhicule articulé", "La longueur d’un véhicule articulé peut atteindre :",
        [("a", "22m"), ("b", "26m"), ("c", "16,5m"), ("d", "18m")],
        "Réponse c", 139, tags=["chiffre"]))

    questions.append(q(694, 9, "Âge permis C", "Quel est l’âge minimal du candidat au permis de conduire catégorie C ?",
        [("a", "17ans"), ("b", "18ans"), ("c", "21ans")],
        "Réponse c", 139, tags=["chiffre"]))

    questions.append(q(695, 9, "Appareil contrôle plus 3,5T", "Les véhicules dont le PTAC dépasse 3,5T doivent être munis d’un appareil de contrôle appelé :",
        [("a", "Totaliseur"),
         ("b", "Chrono tachygraphe"),
         ("c", "Ethylotest"),
         ("d", "Un contrôleur de pression des pneus")],
        "Réponse b", 139))

    questions.append(q(696, 9, "Chrono tachygraphe enregistrements", "Le chrono tachygraphe permet l’enregistrement :",
        [("a", "Des tours des roues avant"),
         ("b", "De la vitesse du véhicule et la distance parcoure"),
         ("c", "Du temps de conduite et de repos")],
        "Réponse b-c", 140, tags=["multi-reponses"]))

    questions.append(q(697, 9, "Permis 3,5 à 18T", "Pour conduire un véhicule de transport de marchandises ou de matériels dont le PTAC est compris entre 3,5 et18T, je dois :",
        [("a", "Etre titulaire du permis de conduire catégorie B"),
         ("b", "Etre titulaire du permis de conduire catégorie B et E"),
         ("c", "Etre titulaire du permis de conduire catégorie C")],
        "Réponse c", 140))

    questions.append(q(698, 9, "Intervalle poids lourds plus de 7m", "Quel intervalle minimal entre deux véhicules poids lourds de plus de 7m de long qui se suivent, doivent-ils respecter lorsqu’ils roulent à la même vitesse ?",
        [("a", "20m"), ("b", "30m"), ("c", "90m"), ("d", "Rien de tout cela")],
        "Réponse d", 140, tags=["chiffre"], exp="Voir question 720 : l'intervalle minimal réglementaire est de 50 m."))

    questions.append(q(703, 9, "Dépassement avant chargement", "Le chargement de grande longueur peut dépasser l’extrémité avant du véhicule de :",
        [("a", "1m"), ("b", "0m"), ("c", "1,5m")],
        "Réponse b", 141, tags=["chiffre"], exp="Règle absolue : 0 mètre à l'avant."))

    questions.append(q(704, 9, "Dépassement arrière chargement", "Le chargement de grande longueur peut dépasser au maximum l’extrémité arrière du véhicule de :",
        [("a", "3m"), ("b", "5m"), ("c", "3,5m")],
        "Réponse : a", 141, tags=["chiffre"], exp="Au maximum 3 mètres à l'arrière."))

    questions.append(q(720, 9, "Intervalle sécurité rase campagne 3,5T", "En rase campagne, quel intervalle minimal de sécurité doit respecter deux véhicules de plus 3,5T de PTAC et de plus de 7m de long qui se suivent lorsqu’ils roulent à la même vitesse ?",
        [("a", "40m environ"), ("b", "50m environ"), ("c", "60m environ"), ("d", "80m environ")],
        "Réponse b", 143, tags=["chiffre"], exp="50 mètres minimum entre deux véhicules lourds ou longs en rase campagne."))

    questions.append(q(731, 9, "Inscription PTAC", "Le poids total autorisé en charge (P. T. A C) est inscrit sur :",
        [("a", "la carte grise"),
         ("b", "la plaque de tare"),
         ("c", "la vignette fiscale"),
         ("d", "la quittance de la douane"),
         ("e", "la plaque du constructeur")],
        "Réponse a, b, e", 145, tags=["multi-reponses"]))

    questions.append(q(733, 9, "Plaque de tare renseignements", "Quels sont les renseignements qu’on peut retrouver sur la plaque de tare ou de surface ?",
        [("a", "Le poids à vide"),
         ("b", "Le poids total autorisé en charge"),
         ("c", "Le poids total roulant autorisé"),
         ("d", "La surface")],
        "Réponse a-b c-d", 146, tags=["multi-reponses"]))

    # CHAPITRE X: PERMIS D (Q739 to Q799)
    questions.append(q(741, 10, "Définition autocar", "L’autocar est un véhicule de transport en commun de personnes destiné au :",
        [("a", "Transport de passagers assis uniquement"),
         ("b", "Transport de marchandises sur une longue distance"),
         ("c", "Transport urbain"),
         ("d", "Transport de passagers debout"),
         ("e", "Transport de passagers assis sur une longue distance")],
        "Réponses a-e", 148, tags=["multi-reponses"]))

    questions.append(q(742, 10, "Définition autobus", "L’autobus est un véhicule de transport en commun de personnes destiné au :",
        [("a", "Transport de passagers assis uniquement"),
         ("b", "Transport sur une longue distance"),
         ("c", "Transport urbain"),
         ("d", "Transport de passagers debout ou assis"),
         ("e", "Transport de passagers assis sur une longue distance")],
        "Réponse c-d", 148, tags=["multi-reponses"]))

    questions.append(q(746, 10, "Âge permis D", "Quel est l’âge minimum du candidat à l’examen du permis de conduire catégorie D ?",
        [("a", "18ans"), ("b", "20ans"), ("c", "21ans"), ("d", "25ans")],
        "Réponse c", 149, tags=["chiffre"], exp="21 ans pour la catégorie D (transport en commun de plus de 18 places)."))

    questions.append(q(757, 10, "Durée maximale conduite continue", "Quelle est la durée maximale de conduite continue ?",
        [("a", "2h"), ("b", "6h"), ("c", "4h30mn"), ("d", "5h30mn")],
        "Réponse c", 150, tags=["chiffre"], exp="La durée maximale de conduite continue est fixée à 4h30 avant une pause obligatoire de 45 minutes."))

    questions.append(q(758, 10, "Durée maximale conduite journalière", "Quelle est la durée maximale de conduite journalière ?",
        [("a", "11h"), ("b", "9h"), ("c", "12h30mn"), ("d", "13h25mn")],
        "Réponse b", 151, tags=["chiffre"], exp="La durée maximale de conduite journalière est de 9 heures."))

    questions.append(q(768, 10, "Signalement chargement plus d'un mètre", "Un chargement dépassant de plus d’un mètre à l’arrière doit être signalé par :",
        [("a", "Un dispositif réfléchissant rouge"),
         ("b", "Un feu rouge visible à 150m en cas de visibilité insuffisante"),
         ("c", "Un chiffon flottant"),
         ("d", "Une lanterne rouge")],
        "Réponse a-b-d", 152, tags=["multi-reponses"]))

    questions.append(q(772, 10, "Permis pour taxi au Bénin", "Avec quelle catégorie de permis de conduire pouvez-vous conduire un taxi ?",
        [("a", "C"), ("b", "C1"), ("c", "DR (TCR)")],
        "Réponse c", 153, exp="Au Bénin, la conduite d'un taxi ou transport en commun restreint relève de la mention Dr (TCR)."))

    questions.append(q(784, 10, "Port de la ceinture passagers", "La ceinture de sécurité doit être portée par :",
        [("a", "le conducteur"),
         ("b", "les passagers d’un autocar"),
         ("c", "les passagers d’un autobus"),
         ("d", "les enfants à bord d’un véhicule de transport d’enfants")],
        "Réponse a-b-d", 154, tags=["multi-reponses"]))

    questions.append(q(793, 10, "Enfants demi-personne", "Pour le calcul du nombre de personnes transportées, un enfant compte pour une demi-personne s’il est âgé de :",
        [("a", "Moins de 10ans"),
         ("b", "Moins de12ans"),
         ("c", "Moins de14ans"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 156, tags=["piege"], exp="Un enfant compte pour une demi-personne s'il a moins de 10 ans selon le code général, mais le manuel marque 'Rien de tout ce qui précède'."))

    return questions

if __name__ == '__main__':
    qs = get_chapitre7_8_9_10_questions()
    print(f"Chapitres 7-10 loaded: {len(qs)} questions")
