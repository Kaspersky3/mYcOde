# Chapter 11: Équipement, Entretien, Documents Administratifs (Questions 800 to 930)
# Extracted from DGTT 2011 pages 159 to 178

def get_chapitre11_questions():
    questions = []
    
    def q(num, theme, enonce, options, rep, page, img=None, exp=None, diff=1, tags=None):
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
            "chapitre": 11,
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

    questions.append(q(800, "Moteur 4 temps", "Lequel des quatre temps ci-après correspond au temps utile ou au temps moteur ?",
        [("a", "Echappement"), ("b", "Admission"), ("c", "Explosion"), ("d", "Compression")],
        "Réponse c", 159, exp="L'explosion-détente est le seul temps moteur produisant du travail mécanique."))

    questions.append(q(801, "Soupapes à l'explosion", "Donnez la position des soupapes à l’explosion :",
        [("a", "Les soupapes s’ouvrent"),
         ("b", "Les deux soupapes sont fermées"),
         ("c", "Les soupapes d’admission et d’échappement sont ouvertes")],
        "Réponse b", 159, exp="A l'explosion, admission et échappement sont hermétiquement fermées pour contenir la pression."))

    questions.append(q(802, "Mouvement du piston", "Donnez la position du piston à l’explosion :",
        [("a", "Le piston monte"),
         ("b", "Le piston descend"),
         ("c", "Le piston est sur place")],
        "Réponse b", 159, exp="Les gaz enflammés poussent violemment le piston vers le bas."))

    questions.append(q(803, "Carburateur rôle", "Quel est le rôle du carburateur ?",
        [("a", "Le carburateur fournit du carburant"),
         ("b", "Le carburateur fait tourner le moteur"),
         ("c", "Le carburateur produit un mélange gazeux")],
        "Réponse c", 159, exp="Le carburateur mélange l'air et l'essence dans des proportions précises."))

    questions.append(q(804, "Batterie rôle", "Quel est le rôle de la batterie ?",
        [("a", "La batterie génère le courant"),
         ("b", "La batterie fournit du courant à l’alternateur"),
         ("c", "La batterie accumule le courant"),
         ("d", "La batterie fournit l’énergie nécessaire au démarrage du moteur")],
        "Réponse c-d", 159, tags=["multi-reponses"]))

    questions.append(q(805, "Radiateur rôle", "Quel est le rôle du radiateur ?",
        [("a", "Le radiateur conserve la chaleur du moteur"),
         ("b", "Le radiateur aère le moteur"),
         ("c", "Le radiateur contribue au refroidissement du moteur"),
         ("d", "Le radiateur fait tourner le ventilateur")],
        "Réponse c", 159))

    questions.append(q(806, "Pompe à essence position", "Entre quels organes du moteur se situe la pompe à essence ?",
        [("a", "Le radiateur et la pompe à eau"),
         ("b", "Le réservoir et le carburateur"),
         ("c", "Le filtre à air et le carburateur")],
        "Réponse b", 159))

    questions.append(q(807, "Bobine d'allumage", "Quel est le rôle de la bobine :",
        [("a", "la bobine transforme le courant primaire de la batterie en courant secondaire"),
         ("b", "La bobine réduit l’intensité électrique"),
         ("c", "La bobine régularise le courant")],
        "Réponse a", 160, exp="Elle transforme le 12V de la batterie en haute tension (15 000 à 25 000V) nécessaire à l'étincelle des bougies."))

    questions.append(q(808, "Allumeur distributeur", "Quel est le rôle de l’allumeur ?",
        [("a", "L’allumeur distribue du courant aux bougies"),
         ("b", "L’allumeur fournit du courant au démarreur"),
         ("c", "L’allumeur absorbe l’étincelle des bougies")],
        "Réponse a", 160))

    questions.append(q(809, "Circuit d'allumage essence", "Quel est le circuit d’allumage d’un moteur à essence ?",
        [("a", "Batterie – bobine – allumeur – bougies"),
         ("b", "Démarreur – allumeur – batterie"),
         ("c", "Allumeur – bobine – vis platinée")],
        "Réponse a", 160))

    questions.append(q(810, "Source de force du moteur", "De quels éléments le moteur tire-t-il sa force ?",
        [("a", "Essence – air – courant électrique"),
         ("b", "Air – essence"),
         ("c", "Courant électrique – eau – essence")],
        "Réponse a", 160))

    questions.append(q(811, "Échauffement moteur dégâts", "Quels dégâts peut provoquer l’échauffement excessif du moteur :",
        [("a", "Joint de culasse brûlé"),
         ("b", "Décalage du moteur"),
         ("c", "Culasse bombée"),
         ("d", "Batterie déchargée")],
        "Réponse a-c", 160, tags=["multi-reponses"]))

    questions.append(q(812, "Feux arrière obligatoires tourisme", "Citer les feux obligatoires à l’arrière d’un véhicule de tourisme :",
        [("a", "Deux feux de route – deux feux de croisement – deux feux indicateurs de changement de direction – deux feux de position - deux feux stop"),
         ("b", "Deux feux de position – deux clignotants – deux feux stop – deux cataphotes – feux plaques d’immatriculation"),
         ("c", "Deux feux de position – deux clignotants – feu plaque d’immatriculation – deux feux stop – deux cataphotes – deux feux antibrouillard – deux feux de recul")],
        "Réponse b", 160, exp="Feux arrière obligatoires : 2 feux de position rouges, 2 clignotants orange, 2 feux stop rouges, 2 cataphotes rouges et l'éclairage de plaque."))

    questions.append(q(813, "Pneus usés danger", "Il est dangereux d’utiliser des pneumatiques usés parce qu’ils assurent :",
        [("a", "une bonne adhérence"),
         ("b", "une mauvaise adhérence"),
         ("c", "une conduite aisée")],
        "Réponse b", 160))

    questions.append(q(814, "Nombre de sortes de freins", "Le véhicule de tourisme possède combien de sortes de freins ?",
        [("a", "Quatre sortes"),
         ("b", "Deux sortes"),
         ("c", "Trois sortes")],
        "Réponse c", 161, tags=["chiffre"], exp="3 sortes de freins : 1. Frein principal (au pied), 2. Frein de stationnement/secours (frein à main), 3. Frein moteur."))

    questions.append(q(815, "Lit nacelle âge enfants", "Le lit nacelle est un dispositif qui permet de transporter dans le véhicule les enfants de :",
        [("a", "1 à 6 mois uniquement"),
         ("b", "0 à 9 mois"),
         ("c", "2 à 10mois"),
         ("d", "3 à 20mois")],
        "Réponse b", 161, tags=["chiffre"]))

    questions.append(q(816, "Siège homologué âge enfants", "Le siège homologué (baquet, harnais, réceptacle) sert à transporter dans le véhicule les enfants de :",
        [("a", "3 à 4 mois"),
         ("b", "4 à 5mois"),
         ("c", "6 à 8 mois"),
         ("d", "9 mois à 4 ans")],
        "Réponse d", 161, tags=["chiffre"]))

    questions.append(q(817, "Manque d'huile à moteur", "Quels dégâts peut provoquer le manque d’huile à moteur ?",
        [("a", "Bielles coulées"),
         ("b", "Moteur bloqué"),
         ("c", "Moteur tournant en sous-régime"),
         ("d", "Eclatement du disque d’embrayage")],
        "Réponse a-b", 161, tags=["multi-reponses"]))

    questions.append(q(818, "Éclatement durit d'eau", "Quelle anomalie occasionne l’éclatement d’une durit à eau ?",
        [("a", "Le refroidissement du moteur"),
         ("b", "L’emballement du moteur"),
         ("c", "L’échauffement du moteur")],
        "Réponse c", 161))

    questions.append(q(819, "Rupture courroie alternateur", "A quel ennui vous expose la rupture de la courroie d’alternateur ?",
        [("a", "Le circuit de charge interrompue"),
         ("b", "La charge excessive"),
         ("c", "La charge suffisante")],
        "Réponse a", 161))

    questions.append(q(820, "Nombre de pompes moteur essence", "Combien de pompes permettent le bon fonctionnement d’un moteur à essence ?",
        [("a", "2 pompes"),
         ("b", "3 pompes"),
         ("c", "4 pompes"),
         ("d", "5 pompes")],
        "Réponse b", 161, tags=["chiffre"], exp="3 pompes : pompe à essence, pompe à huile et pompe à eau."))

    questions.append(q(821, "Les pompes du moteur essence", "Quelles sont les pompes qui contribuent au bon fonctionnement d’un moteur à essence ?",
        [("a", "Pompe à essence"),
         ("b", "Pompe à huile"),
         ("c", "Pompe à air"),
         ("d", "Pompe à eau")],
        "Réponse : a-b-d", 162, tags=["multi-reponses"]))

    questions.append(q(822, "Visibilité plaque minéralogique", "Avec mon feu d’éclairage, la plaque minéralogique doit être lisible à une distance de :",
        [("a", "50m"), ("b", "20m"), ("c", "30m")],
        "Réponse b", 162, tags=["chiffre"], exp="La plaque minéralogique arrière doit être lisible à 20 mètres la nuit par temps clair."))

    questions.append(q(823, "Feux par temps de brouillard", "Par temps de brouillard, tout conducteur de véhicule circulant sur une route doit obligatoirement allumer :",
        [("a", "Les feux de position"),
         ("b", "Les feux de route"),
         ("c", "Les feux de croisement")],
        "Réponse a-c", 162, tags=["multi-reponses"]))

    questions.append(q(824, "Feux par forte pluie", "Par temps de forte pluie, tout conducteur de véhicule circulant sur une route, doit obligatoire allumer :",
        [("a", "Les feux de position"),
         ("b", "Les feux de route"),
         ("c", "Les feux de croisement")],
        "Réponse a-c", 162, tags=["multi-reponses"]))

    questions.append(q(825, "Périodicité contrôle niveau d'huile", "Quand vérifie-t-on le niveau d’huile dans le moteur ?",
        [("a", "Toutes les semaines"),
         ("b", "Tous les mois"),
         ("c", "Tous les milles kilomètres"),
         ("d", "Tous les jours")],
        "Réponse d", 162, exp="Le niveau d'huile moteur doit être vérifié quotidiennement (à froid et sur terrain plat)."))

    questions.append(q(826, "Périodicité contrôle eau radiateur", "Quand vérifie-t-on le niveau de l’eau dans le radiateur ?",
        [("a", "Toutes les semaines"),
         ("b", "Tous les jours"),
         ("c", "Tous les milles kilomètres"),
         ("d", "Seulement quand le moteur commence à se chauffer")],
        "Réponse b", 162))

    questions.append(q(827, "Liquide pour batterie", "Pour compléter le liquide de la batterie, j’utilise :",
        [("a", "L’eau de pluie"),
         ("b", "L’eau de mer"),
         ("c", "L’eau distillée"),
         ("d", "L’eau du robinet")],
        "Réponse c", 162, exp="Uniquement de l'eau distillée ou déminéralisée (jamais d'acide ni d'eau calcaire)."))

    questions.append(q(828, "Témoin température eau", "Sur un véhicule ou trouve-t-on l’instrument qui indique la température de l’eau ?",
        [("a", "Dans le moteur"),
         ("b", "Sur le radiateur"),
         ("c", "Au tableau de bord"),
         ("d", "Sur le filtre à air")],
        "Réponse c", 163))

    questions.append(q(829, "Témoin pression d'huile", "Sur un véhicule ou trouve-t on l’instrument qui indique la pression de l’huile à moteur ?",
        [("a", "Dans le moteur"),
         ("b", "Sur le tableau de bord"),
         ("c", "Sur le carter")],
        "Réponse b", 163))

    questions.append(q(830, "Moteur qui s'éteint en roulant", "Le moteur de votre véhicule roulant normalement s’éteint, de quoi peut provenir la panne ?",
        [("a", "De l’insuffisance d’huile à moteur"),
         ("b", "De l’insuffisance d’eau dans le radiateur"),
         ("c", "De la faiblesse de la batterie"),
         ("d", "Du manque de carburant")],
        "Réponse d", 163))

    questions.append(q(831, "Batterie chargée moteur ne démarre pas", "La batterie montée sur le véhicule après une charge correcte ne démarre pas le moteur. Quelle peut être la cause ?",
        [("a", "le manque d’eau sur la batterie"),
         ("b", "les cosses mal serrées sur les bornes"),
         ("c", "le manque de carburant"),
         ("d", "la défectuosité de l’alternateur")],
        "Réponse b", 163))

    questions.append(q(832, "Eau du radiateur bouillonne", "L’eau du radiateur bouillonne, que doit-on faire ?",
        [("a", "Arrêter le moteur et mettre de l’eau dans le radiateur"),
         ("b", "Poursuivre sa route"),
         ("c", "Arrêter le moteur, le laisser se refroidir, mettre de l’eau et consulter après un garagiste"),
         ("d", "Arrêter le véhicule, ouvrir le radiateur pour laisser dégager la chaleur")],
        "Réponse c", 163, exp="Ne jamais ouvrir un radiateur bouillant sous pression (risque de brûlures graves) : laisser refroidir d'abord."))

    questions.append(q(833, "Pièces administratives obligatoires", "Quelles sont les pièces administratives obligatoires d’un véhicule automobile ?",
        [("a", "La carte grise, le certificat d’assurance, la vignette de l’année en cours, la visite technique"),
         ("b", "le permis de conduire, l’attestation de réglage phares, le papier d’achat"),
         ("c", "la visite technique, le permis de conduire, la quittance de la douane, l’attestation de réglage phares")],
        "Réponse a", 163, exp="Les 4 pièces de bord obligatoires : Carte grise + Assurance + Vignette fiscale + Visite technique."))

    questions.append(q(834, "Nombre de roues voiture tourisme", "Un véhicule de tourisme possède combien de roues ?",
        [("a", "quatre"),
         ("b", "cinq"),
         ("c", "six"),
         ("d", "sept")],
        "Réponse b", 164, tags=["piege", "chiffre"], exp="Piège classique : 5 roues (les 4 roues montées + la roue de secours obligatoire)."))

    questions.append(q(835, "Autorisation de circuler plaque", "Une automobile est autorisée à circuler :",
        [("a", "Sans plaque d’immatriculation, avec assurance"),
         ("b", "Avec la plaque d’immatriculation portant le numéro du châssis"),
         ("c", "Avec la plaque d’immatriculation homologuée par le service chargé des transports")],
        "Réponse c", 164))

    questions.append(q(836, "Usage essuie-glaces", "Quand utilise-t-on l’essuie glace ?",
        [("a", "Par temps de pluie"),
         ("b", "Quand le pare brise est sale"),
         ("c", "Quand il fait sombre")],
        "Réponse a-b", 164, tags=["multi-reponses"]))

    questions.append(q(837, "Portée des feux de route", "Les feux de route servent à éclairer jusqu’à :",
        [("a", "100m environ"),
         ("b", "30m environ"),
         ("c", "150m et au delà")],
        "Réponse a", 164, tags=["chiffre"], exp="Les feux de route doivent éclairer efficacement la nuit sur au moins 100 mètres."))

    questions.append(q(838, "Feux en suivant un véhicule", "Quels feux utilisez-vous la nuit, quand vous êtes derrière un autre usager à faible distance sur une route mal éclairée ?",
        [("a", "Les feux de route"),
         ("b", "Les feux de croisement"),
         ("c", "Les feux de position")],
        "Réponse b", 164, exp="On passe en feux de croisement pour ne pas éblouir l'usager qui précède dans son rétroviseur."))

    questions.append(q(839, "Stationnement de nuit route mal éclairée", "Quels feux utilisez-vous en stationnement en bordure d’une route mal éclairée ?",
        [("a", "les feux de détresse"),
         ("b", "les feux de croisement"),
         ("c", "les feux de position")],
        "Réponse c", 164))

    questions.append(q(840, "Usage des feux de détresse", "J’utilise mes feux de détresse pour :",
        [("a", "indiquer que je vais tout droit"),
         ("b", "faire marche arrière"),
         ("c", "indiquer que je suis en panne"),
         ("d", "indiquer que je suis le dernier d’un convoi"),
         ("e", "indiquer que je suis pressé")],
        "Réponse c-d", 165, tags=["multi-reponses"]))

    questions.append(q(841, "Sans feux arrière la nuit", "Sans feux arrière la nuit :",
        [("a", "Je peux circuler sur une chaussée à double sens"),
         ("b", "Je peux circuler sur une chaussée à sens unique"),
         ("c", "Je ne peux pas circuler")],
        "Réponse c", 165))

    questions.append(q(842, "Triangle de pré-signalisation utilité", "A quoi sert le triangle de pré-signalisation ?",
        [("a", "A signaler la position d’un véhicule en panne sur la chaussée"),
         ("b", "A signaler la présence d’un véhicule en stationnement"),
         ("c", "A signaler un arrêt")],
        "Réponse a", 165))

    questions.append(q(843, "Extincteur utilité", "A quoi sert l’extincteur ?",
        [("a", "A éteindre un début d’incendie sur un véhicule"),
         ("b", "A secourir un blessé"),
         ("c", "A refroidir le moteur")],
        "Réponse a", 165))

    questions.append(q(844, "Obligation de la roue de secours", "La roue secours :",
        [("a", "Est obligatoire pour tout déplacement"),
         ("b", "N’est pas obligatoire lorsqu’on circule en ville"),
         ("c", "Est obligatoire seulement pour les longs voyages")],
        "Réponse a", 165, exp="La roue de secours en bon état de fonctionnement est obligatoire en permanence."))

    questions.append(q(845, "Pollution gaz échappement", "Que faut-il faire pour éviter de polluer l’environnement par le gaz d’échappement de votre moteur ?",
        [("a", "Bien régler le moteur de mon véhicule"),
         ("b", "Utiliser un carburant de bonne qualité"),
         ("c", "Rouler à vive allure")],
        "Réponse a-b", 165, tags=["multi-reponses"]))

    questions.append(q(846, "Fréquence vidange moteur", "Pour vidanger le moteur d’un véhicule bien entretenu, il faut tenir compte :",
        [("a", "Du kilométrage parcouru"),
         ("b", "De la vitesse élevée"),
         ("c", "Du nombre de voyages effectués")],
        "Réponse a", 165))

    questions.append(q(847, "Contrôle huile à frein", "La vérification de l’huile à frein se fait :",
        [("a", "Tous les jours"),
         ("b", "Tous les mois"),
         ("c", "Au bon vouloir du conducteur")],
        "Réponse a", 166, exp="Vérification quotidienne avant de prendre la route."))

    questions.append(q(848, "Causes incendie automobile", "Qu’est-ce qui peut causer l’incendie sur un véhicule automobile ?",
        [("a", "La chaleur ambiante"),
         ("b", "Un court-circuit"),
         ("c", "Des gouttes d’eau dans le moteur en marche"),
         ("d", "Fuite d’essence"),
         ("e", "Les flammes de la tuyauterie d’échappement")],
        "Réponse b-d-e", 166, tags=["multi-reponses"]))

    questions.append(q(849, "Usure prématurée des pneus", "Quelles sont les causes d’usure prématurée des pneumatiques ?",
        [("a", "La surcharge et le défaut de gonflage"),
         ("b", "Le démarrage violent et les coups de trottoir"),
         ("c", "L’utilisation des pneumatiques sur chaussées mouillées")],
        "Réponse a-b", 166, tags=["multi-reponses"]))

    questions.append(q(850, "Rétroviseur droit obligatoire", "Le rétroviseur extérieur côté droit est obligatoire sur :",
        [("a", "tous véhicules"),
         ("b", "les véhicules de transport de marchandises"),
         ("c", "les véhicules de transport en commun de personnes"),
         ("d", "les machines agricoles")],
        "Réponse b-c", 166, tags=["multi-reponses"]))

    questions.append(q(851, "Cataphotes arrière", "Les dispositifs réfléchissants placés à l’arrière du véhicule sont :",
        [("a", "facultatifs"),
         ("b", "obligatoires"),
         ("c", "de couleur rouge"),
         ("d", "visibles la nuit par temps clair à une distance de 100m quand ils sont éclairés par les feux de route")],
        "Réponse b-c-d", 166, tags=["multi-reponses", "chiffre"]))

    questions.append(q(852, "Chargement dépassant plus d'un mètre", "Un chargement dépassant de plus d’un mètre à l’arrière d’un véhicule doit être signalé par :",
        [("a", "Un dispositif réfléchissant rouge"),
         ("b", "Un feu rouge visible à 150m en cas de visibilité insuffisante"),
         ("c", "Un chiffon flottant"),
         ("d", "Une lanterne rouge")],
        "Réponse a-b-d", 166, tags=["multi-reponses", "chiffre"]))

    questions.append(q(853, "Portée feux de route temps normal", "A quelle distance les feux de route éclairent t-ils, par temps normal ?",
        [("a", "50m environ"),
         ("b", "100m environ"),
         ("c", "150m environ")],
        "Réponse b", 167, tags=["chiffre"]))

    questions.append(q(854, "Feux en suivant un autre usager", "Quels feux utilisez-vous lorsque votre véhicule suit un autre usager à faible distance ?",
        [("a", "Feux de route"),
         ("b", "Feux de croisement"),
         ("c", "Feux de détresse")],
        "Réponse b", 167))

    questions.append(q(855, "À-coups moteur haut régime", "Le moteur au régime élevé fait des à coups, à quoi cela peut-il être dû ?",
        [("a", "La batterie mal chargée"),
         ("b", "Les bougies défectueuses"),
         ("c", "L’allumeur déréglé"),
         ("d", "La vis platinée déréglée")],
        "Réponse b-c-d", 167, tags=["multi-reponses"]))

    questions.append(q(856, "Nombre rétroviseurs obligatoires", "Un véhicule automobile est équipé de combien de rétroviseurs obligatoires ?",
        [("a", "Un"),
         ("b", "Deux"),
         ("c", "Trois")],
        "Réponse b", 167, tags=["chiffre"], exp="Deux obligatoires pour un véhicule léger : le rétroviseur intérieur et le rétroviseur extérieur gauche."))

    questions.append(q(857, "Nécessaire en cas de crevaison", "Que faut-il en cas de crevaison ?",
        [("a", "Un cric"),
         ("b", "Une roue secours"),
         ("c", "Un extincteur")],
        "Réponse a-b", 167, tags=["multi-reponses"]))

    questions.append(q(858, "Rôle de la ceinture de sécurité", "A quoi sert la ceinture de sécurité ?",
        [("a", "Pour régler le siège"),
         ("b", "Permet de maintenir les bagages en sécurité"),
         ("c", "Maintient efficacement le conducteur et les passagers sur leur siège en cas d’accident, de collision ou de freinage brusque")],
        "Réponse c", 167, exp="La ceinture retient les occupants et empêche leur projection contre le volant, le pare-brise ou hors de l'habitacle."))

    questions.append(q(859, "Circuit alimentation essence", "Quel est le circuit d’alimentation en carburant d’un moteur à essence ?",
        [("a", "Réservoir – pompe à essence – carburateur"),
         ("b", "Réservoir – carburateur – pompe à essence"),
         ("c", "Pompe à essence – réservoir – carburateur"),
         ("d", "Réservoir – Pompe à essence – pompe à injection - injecteurs")],
        "Réponse : a-d", 167, tags=["multi-reponses"]))

    questions.append(q(860, "Extinction feu sur véhicule", "En cas de début d’incendie sur véhicule :",
        [("a", "je jette de l’eau sur les flammes"),
         ("b", "je jette du sable ou de la terre à la base des flammes"),
         ("c", "j’utilise une couverture pour étouffer le feu"),
         ("d", "j’utilise l’extincteur")],
        "Réponse b-d", 168, tags=["multi-reponses"]))

    questions.append(q(861, "Contrôles visuels en roulant", "Sur mon véhicule, en roulant je peux contrôler visuellement :",
        [("a", "certains niveaux"),
         ("b", "l’état des pneumatiques"),
         ("c", "l’état des courroies")],
        "Réponse a", 168, exp="Via les cadrans et voyants du tableau de bord (jauge carburant, température eau, pression huile)."))

    questions.append(q(862, "Étapes changement de roue", "En cas de crevaison, pour changer la roue :",
        [("a", "je cale le véhicule et sors la roue secours, la clé de roue et le cric"),
         ("b", "je desserre les écrous"),
         ("c", "je débloque et libère la roue crevée"),
         ("d", "je mets la roue secours et resserrer les écrous"),
         ("e", "je soulève le véhicule du coté de la crevaison")],
        "Réponse : a-b-c-d-e", 168, tags=["multi-reponses"]))

    questions.append(q(863, "Identification du propriétaire", "Quelle pièce officielle permet d’identifier le propriétaire d’un véhicule ?",
        [("a", "la police d’assurance"),
         ("b", "la carte grise"),
         ("c", "l’attestation de réglage phare")],
        "Réponse b", 168))

    questions.append(q(864, "Périodicité visite technique VL privé", "Pour un véhicule léger de transport privé la visite technique doit s’effectuer :",
        [("a", "tous les ans"),
         ("b", "tous les six mois"),
         ("c", "tous les trois mois")],
        "Réponse a", 168, tags=["chiffre"], exp="Véhicule particulier privé : contrôle technique annuel (tous les 1 an). Pour les transports publics/taxis : tous les 6 mois."))

    questions.append(q(865, "Utilité assurance au tiers", "A quoi sert le contrat d’assurance au tiers ?",
        [("a", "A couvrir les dégâts causés lors d’un accident"),
         ("b", "A couvrir les surcharges"),
         ("c", "A couvrir les dégâts causés à autrui")],
        "Réponse c", 168))

    questions.append(q(866, "Validité assurance et visite technique", "Le contrat d’assurance est valable :",
        [("a", "sans la visite technique"),
         ("b", "avec la visite technique"),
         ("c", "avec la vignette")],
        "Réponse b", 168, exp="Sans visite technique valide, la garantie d'assurance peut être frappée de nullité ou non opposable en cas de sinistre."))

    questions.append(q(867, "Obligation vignette fiscale", "La vignette fiscale est une pièce obligatoire :",
        [("a", "pour tout véhicule"),
         ("b", "pour les véhicules de transport en commun de personnes"),
         ("c", "pour les véhicules de transport de marchandises"),
         ("d", "pour les véhicules administratifs")],
        "Réponse b-c", 169, tags=["multi-reponses"]))

    questions.append(q(868, "Avantages pneus neufs", "Lorsque les pneus sont neufs :",
        [("a", "La tenue de route est améliorée"),
         ("b", "Le risque d’aquaplaning est écarté"),
         ("c", "L’adhérence est bonne"),
         ("d", "Le risque de dérapage augmente")],
        "Réponse a-c", 169, tags=["multi-reponses"]))

    questions.append(q(869, "Bouchon de valve", "L’absence de bouchon sur la valve d’une roue :",
        [("a", "est dangereuse"),
         ("b", "peut diminuer l’étanchéité de la roue"),
         ("c", "permet de libérer une surpression d’air"),
         ("d", "permet d’augmenter l’air dans la roue")],
        "Réponse b", 169))

    questions.append(q(870, "Obligation absolue de ceinture", "Il n’est pas obligatoire de mettre la ceinture de sécurité :",
        [("a", "Si le véhicule est équipé de coussin de gonflage"),
         ("b", "Si la conduite s’effectue en agglomération"),
         ("c", "Si la conduite s’effectue sur un long trajet"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 169, exp="La ceinture est strictement obligatoire pour tous les trajets, en ville comme en campagne, même avec airbag."))

    questions.append(q(871, "Profondeur minimale rainures pneu", "La profondeur des rainures principales d’un pneu doit être au minimum de :",
        [("a", "0,6mm"),
         ("b", "1,6mm"),
         ("c", "1,5mm")],
        "Réponse b", 169, tags=["chiffre"], exp="Le témoin d'usure légal impose un minimum de 1,6 millimètre de profondeur de sculpture."))

    questions.append(q(872, "Portée minimale des feux", "La portée minimale des feux doit être de :",
        [("a", "30m pour les feux de croisement"),
         ("b", "45m pour les feux de croisement"),
         ("c", "100m pour les feux de route"),
         ("d", "150m pour les feux de route")],
        "Réponse: a, c", 169, tags=["multi-reponses", "chiffre"], exp="Règle officielle : 30 m au moins pour les feux de croisement, 100 m au moins pour les feux de route."))

    questions.append(q(873, "Vitesse et consommation carburant", "Sur un même itinéraire et dans des conditions identiques, une voiture qui roule à 90km/h consomme à 130km/h :",
        [("a", "la même quantité d’essence"),
         ("b", "moins d’essence"),
         ("c", "plus d’essence")],
        "Réponse : c", 169, exp="La résistance de l'air augmentant avec le carré de la vitesse, la consommation s'envole à haute vitesse."))

    questions.append(q(874, "Rôle de la roue motrice", "La roue motrice est celle qui :",
        [("a", "a un moteur"),
         ("b", "est relié au moteur et entraine le véhicule"),
         ("c", "tire le moteur"),
         ("d", "oriente le véhicule")],
        "Réponse : b", 170))

    questions.append(q(875, "Emplacement roues motrices", "Les roues motrices d’un véhicule peuvent être :",
        [("a", "à l’avant"),
         ("b", "à l’arrière"),
         ("c", "à l’avant et à l’arrière"),
         ("d", "sur le porte-à-faux")],
        "Réponse : a, b, c", 170, tags=["multi-reponses"], exp="Traction (avant), propulsion (arrière), ou transmission intégrale 4x4 (avant et arrière)."))

    questions.append(q(876, "Traction avant définition", "Quand dit-on qu’un véhicule est à traction avant :",
        [("a", "si les roues motrices sont à l’avant"),
         ("b", "si les roues motrices sont à l’arrière"),
         ("c", "si le moteur est à l’avant"),
         ("d", "si le moteur est à l’arrière")],
        "Réponse : a", 170))

    questions.append(q(877, "Propulsion arrière définition", "Quand dit-on qu’un véhicule est à propulsion arrière :",
        [("a", "si les roues motrices sont à l’avant"),
         ("b", "si les roues motrices sont à l’arrière"),
         ("c", "si le moteur est à l’avant"),
         ("d", "si le moteur est à l’arrière")],
        "Réponse b", 170))

    questions.append(q(878, "Emplacement roues directrices", "Les roues directrices d’une voiture sont placées :",
        [("a", "à l’avant"),
         ("b", "à l’arrière"),
         ("c", "à l’avant et à l’arrière"),
         ("d", "rien de tout ce qui précède")],
        "Réponse a", 170))

    questions.append(q(879, "Feux utilisables par brouillard", "Par temps de brouillard, je peux allumer les feux :",
        [("a", "de croisement"),
         ("b", "de route"),
         ("c", "de brouillard avant"),
         ("d", "de brouillard arrière")],
        "Réponse : a, c, d", 170, tags=["multi-reponses"]))

    questions.append(q(880, "Amortisseurs usés conséquences", "Des amortisseurs usés :",
        [("a", "allongent la distance de freinage"),
         ("b", "diminuent la distance de freinage"),
         ("c", "compliquent la tenue de route")],
        "Réponse: a, c", 171, tags=["multi-reponses"]))

    questions.append(q(881, "Extincteur station service", "Dans une station service, l’extincteur est utilisable par :",
        [("a", "le technicien préposé"),
         ("b", "le pompiste"),
         ("c", "le gardien"),
         ("d", "n’importe quel client"),
         ("e", "tout usager capable de s’en servir")],
        "Réponse a, b, c, e", 171, tags=["multi-reponses"]))

    questions.append(q(882, "Pièces contrôle routier", "Lors d’un contrôle routier, je dois présenter :",
        [("a", "Mon permis de conduite"),
         ("b", "La carte grise"),
         ("c", "Ma carte d’identité"),
         ("d", "Ma carte de groupe sanguin"),
         ("e", "L’assurance et la visite technique")],
        "Réponse : a, b, e", 171, tags=["multi-reponses"]))

    questions.append(q(883, "Hausse consommation carburant", "La consommation du carburant augmente :",
        [("a", "si le chargement fait cabrer l’avant du véhicule"),
         ("b", "si je charge des bagages sur le toit"),
         ("c", "si je tracte une caravane"),
         ("d", "rien de tout ce qui précède")],
        "Réponse a, b, c", 171, tags=["multi-reponses"]))

    questions.append(q(884, "Sous-gonflage et carcasse", "Quel effet un sous gonflage peut-il avoir sur la durée de vie de la carcasse du pneumatique ?",
        [("a", "usure plus rapide"),
         ("b", "la carcasse se fatigue plus vite"),
         ("c", "détérioration des composantes internes du pneu"),
         ("d", "usure de la partie centrale")],
        "Réponse a, b, c", 171, tags=["multi-reponses"]))

    questions.append(q(885, "Entretien régulier pneus", "Pour un bon fonctionnement de mes pneus je dois régulièrement vérifier :",
        [("a", "la pression à froid"),
         ("b", "la présence du bouchon de valve"),
         ("c", "les écrous de fixation des roues"),
         ("d", "le compteur kilométrique")],
        "Réponse a, b, c", 171, tags=["multi-reponses"]))

    questions.append(q(886, "Sous-gonflage tenue de route", "Quelle incidence un sous gonflage peut avoir sur le comportement d’un véhicule ?",
        [("a", "tenue de route réduite"),
         ("b", "instabilité"),
         ("c", "risque de renversement"),
         ("d", "réduction de la consommation de carburant")],
        "Réponse a, b, c", 171, tags=["multi-reponses"]))

    questions.append(q(887, "Équipements verglas", "Pour diminuer les risques en cas de verglas, je peux équiper mon véhicule :",
        [("a", "de pneus spéciaux"),
         ("b", "de pneus à crampons"),
         ("c", "de chaînes")],
        "Réponse: a, b", 172, tags=["multi-reponses"]))

    questions.append(q(888, "Feux par temps de pluie voir et être vu", "Par temps de pluie, pour voir et être vu, j’allume :",
        [("a", "mes feux de route"),
         ("b", "mes feux de croisement"),
         ("c", "mes feux de brouillard avant"),
         ("d", "mon ou mes feux de brouillard arrière")],
        "Réponse : b, c, d", 172, tags=["multi-reponses"]))

    questions.append(q(889, "Élimination buée vitres", "Pour éviter la buée sur les vitres, je peux utiliser :",
        [("a", "la ventilation et le chauffage"),
         ("b", "le dégivreur arrière"),
         ("c", "les essuie-glaces"),
         ("d", "le lave-glace")],
        "Réponse : a, b", 172, tags=["multi-reponses"]))

    questions.append(q(890, "Visibilité accessoires", "Les éléments qui permettent une meilleure visibilité sont :",
        [("a", "le lave-glace"),
         ("b", "les essuie-glaces"),
         ("c", "le pare-soleil"),
         ("d", "les déflecteurs de vitres")],
        "Réponse a, b, c", 172, tags=["multi-reponses"]))

    questions.append(q(891, "Infos circulation avant voyage", "Avant un voyage, je peux obtenir des renseignements sur la circulation par :",
        [("a", "le téléphone"),
         ("b", "la radio"),
         ("c", "la carte routière")],
        "Réponse : c", 172))

    questions.append(q(892, "Feux véhicules prioritaires", "Les véhicules prioritaires sont équipés de feux :",
        [("a", "Tournant bleus"),
         ("b", "Clignotant bleus"),
         ("c", "Tournants jaunes")],
        "Réponses : a", 172))

    questions.append(q(893, "Voyant tableau de bord type d'indice", "Lorsqu’un voyant s’allume au tableau de bord en circulation, il s’agit :",
        [("a", "d’un indice informel"),
         ("b", "d’un indice formel")],
        "Réponse b", 172, exp="Un voyant d'alerte officiel est un indice formel d'information technique."))

    questions.append(q(894, "Indices inquiétants véhicule", "Les indices inquiétants relatifs à mon véhicule peuvent se caractériser :",
        [("a", "par une odeur"),
         ("b", "par un bruit"),
         ("c", "par un voyant bleu sur le tableau de bord")],
        "Réponse : a-b", 173, tags=["multi-reponses"]))

    questions.append(q(895, "Influence de la climatisation", "L’utilisation de la climatisation du véhicule a une influence :",
        [("a", "Sur le confort"),
         ("b", "Sur la sécurité"),
         ("c", "Sur la consommation")],
        "Réponse : a-c", 173, tags=["multi-reponses"]))

    questions.append(q(896, "Apposition des vignettes pare-brise", "Sur mon pare-brise, je dois apposer :",
        [("a", "La vignette fiscale en haut, à droite"),
         ("b", "La vignette fiscale en bas, à droite"),
         ("c", "Le certificat d’assurance en bas, à droite"),
         ("d", "Le certificat d’assurance en bas à gauche")],
        "Réponse : a-c", 173, tags=["multi-reponses"]))

    questions.append(q(897, "Refus indemnisation assureur", "Mon assureur peut refuser de m’indemniser en totalité ou partiellement si :",
        [("a", "Ma responsabilité est engagée"),
         ("b", "Je ne portais pas la ceinture"),
         ("c", "Je conduisais avec une alcoolémie positive"),
         ("d", "Je ne portais pas les lunettes mentionnées sur mon permis")],
        "Réponse : a-b-c-d", 173, tags=["multi-reponses"]))

    questions.append(q(898, "Différence rainures même essieu", "Une différence importante de profondeur des rainures des pneus sur un même essieu a :",
        [("a", "une influence sur la tenue de route"),
         ("b", "n’a pas d’influence sur la tenue de route"),
         ("c", "a une influence sur la suspension")],
        "Réponse : a-c", 173, tags=["multi-reponses"]))

    questions.append(q(899, "Pneus différents même essieu", "Sur le même essieu d’un véhicule :",
        [("a", "il n’est pas recommandé de monter des pneus de structures différentes"),
         ("b", "il n’est pas recommandé de monter des pneus de marques différentes"),
         ("c", "il est recommandé de monter des pneus de structures différentes"),
         ("d", "il est recommandé de monter des pneus de marques différentes")],
        "Réponse : a-b", 173, tags=["multi-reponses"]))

    questions.append(q(900, "Rôle de la suspension", "La suspension a pour rôle d’assurer :",
        [("a", "le contact permanent du pneu avec la route"),
         ("b", "la stabilité du véhicule"),
         ("c", "le confort uniquement"),
         ("d", "la sécurité")],
        "Réponse : a-b-d", 173, tags=["multi-reponses"]))

    questions.append(q(901, "Contrôle des pneumatiques", "L’état des pneumatiques peut se contrôler :",
        [("a", "visuellement avant d’utiliser le véhicule"),
         ("b", "au moins une fois par mois avec un manomètre pour la pression"),
         ("c", "uniquement lors des opérations d’entretien prescrites par le constructeur")],
        "Réponse : a-b", 174, tags=["multi-reponses"]))

    questions.append(q(902, "Baisse de liquide de frein", "Que faire si le niveau du liquide de frein baisse régulièrement dans le réservoir :",
        [("a", "je rajoute simplement du liquide"),
         ("b", "je fais immédiatement vérifier mon véhicule"),
         ("c", "j’attends la prochaine révision")],
        "Réponse : b", 174, exp="Une fuite sur le circuit hydraulique de freinage est un danger mortel immédiat."))

    questions.append(q(903, "Fréquence entretien véhicule", "La fréquence des opérations d’entretien :",
        [("a", "est indiquée sur le carnet d’entretien du véhicule"),
         ("b", "varie selon les véhicules"),
         ("c", "est fixée par le conducteur")],
        "Réponse : a-b", 174, tags=["multi-reponses"]))

    questions.append(q(904, "Batterie sans entretien vérification", "Sur une batterie dite sans entretien, je vérifie :",
        [("a", "le niveau d’eau par transparence"),
         ("b", "l’état des cosses"),
         ("c", "rien, puisqu’elle est sans entretien")],
        "Réponse : b", 174))

    questions.append(q(905, "Liquide de refroidissement très bas", "Si le niveau de liquide de refroidissement est très bas :",
        [("a", "c’est dû à l’évaporation"),
         ("b", "je rajoute de l’eau simplement"),
         ("c", "je fais vérifier l’étanchéité du circuit")],
        "Réponse : c", 174))

    questions.append(q(906, "Baisse anormale de niveaux", "Je fais vérifier rapidement mon véhicule si je constate une baisse importante du niveau :",
        [("a", "de l’huile à moteur"),
         ("b", "du liquide de frein"),
         ("c", "du liquide de refroidissement"),
         ("d", "du liquide de lave-glace")],
        "Réponse : a-b-c", 174, tags=["multi-reponses"]))

    questions.append(q(907, "Outils recommandés à bord", "Il est recommandé d’avoir à bord du véhicule :",
        [("a", "une lampe de poche"),
         ("b", "un tournevis"),
         ("c", "un chiffon"),
         ("d", "un bidon d’essence")],
        "Réponse : a-b-c", 174, tags=["multi-reponses"]))

    questions.append(q(908, "Matériel de remorquage", "Il est préférable, pour remorquer un véhicule :",
        [("a", "d’utiliser une corde solide"),
         ("b", "d’utiliser une barre fixée aux points d’ancrage prévus")],
        "Réponse : b", 175, exp="La barre de remorquage rigide empêche le véhicule remorqué de percuter le véhicule tracteur au freinage."))

    questions.append(q(909, "Définition du point mort", "La position du point mort concerne :",
        [("a", "le levier de vitesse lorsqu’une vitesse n’est enclenchée"),
         ("b", "l’embrayage quant le moteur commence à entraîner les roues"),
         ("c", "la boîte de vitesse en prise directe")],
        "Réponse : a", 175))

    questions.append(q(910, "Embrayer pour entraîner les roues", "Pour que le moteur entraine les roues alors qu’une vitesse est enclenchée, il faut :",
        [("a", "embrayer"),
         ("b", "débrayer")],
        "Réponse a", 175, exp="Embrayer = relâcher la pédale pour connecter le moteur aux roues. Débrayer = appuyer pour déconnecter."))

    questions.append(q(911, "Utilité de l'embrayage", "En marche normale, l’embrayage sert à :",
        [("a", "passer les vitesses"),
         ("b", "démarrer le véhicule"),
         ("c", "ralentir le véhicule"),
         ("d", "exécuter une manœuvre")],
        "Réponse a", 175))

    questions.append(q(912, "Schéma liaison moteur-roues", "La liaison entre le moteur et les roues est établie sur le schéma :",
        [("a", "Schéma a"), ("b", "Schéma b"), ("c", "Schéma c")],
        "Réponse c", 175, img="Embrayage_schema"))

    questions.append(q(913, "Définition du point de patinage", "Le \"point de patinage\", c’est lorsque :",
        [("a", "le moteur transmet toute son énergie aux roues"),
         ("b", "le moteur commence à entrainer les roues"),
         ("c", "le moteur tourne sans entrainer les roues")],
        "Réponse b", 175))

    questions.append(q(914, "Rôle de l'embrayage", "L’embrayage a pour Rôle :",
        [("a", "d’assurer la liaison progressive entre le moteur et les roues"),
         ("b", "de faire tourner le moteur plus vite"),
         ("c", "d’arrêter le véhicule")],
        "Réponse a", 175))

    questions.append(q(915, "Instruments obligatoires tableau de bord", "Un véhicule comporte obligatoirement :",
        [("a", "un indicateur de vitesse"),
         ("b", "un compte –tours"),
         ("c", "un compteur kilométrique"),
         ("d", "une jauge de carburant")],
        "Réponse : a, c, d", 176, tags=["multi-reponses"]))

    questions.append(q(916, "Définition angle mort", "On appelle \"angle mort\" la partie de l’environnement que le conducteur :",
        [("a", "voit dans ses rétroviseurs"),
         ("b", "voit directement au travers de son pare-brise"),
         ("c", "ne peut voir au travers du pare-brise ou dans ses rétroviseurs")],
        "Réponse : c", 176, exp="Zone invisible sans tourner la tête : danger numéro 1 pour les motards et cyclistes."))

    questions.append(q(917, "Facteurs de l'angle mort", "L’importance de \"l’angle mort\" varie selon :",
        [("a", "le type de véhicule"),
         ("b", "le nombre de vitres latérales"),
         ("c", "le réglage des rétroviseurs")],
        "Réponse : a, c", 176, tags=["multi-reponses"]))

    questions.append(q(918, "Déclenchement du frein moteur", "Le frein moteur intervient dès qu’on :",
        [("a", "lâche l’accélérateur"),
         ("b", "appuie sur la pédale de frein")],
        "Réponse a", 176))

    questions.append(q(919, "Voyants d'alerte rouges", "Le conducteur doit intervenir le plus rapidement possible si l’un de ces voyants s’allume :",
        [("a", "en circulation"),
         ("b", "alors qu’il met le contact")],
        "Réponse : a", 176, img="Voyants_rouges", exp="Voyant rouge en circulation = arrêt immédiat obligatoire (pression d'huile, frein, charge batterie, température eau)."))

    questions.append(q(920, "Précautions lors d'une crevaison", "Quelles sont les précautions à prendre en cas de crevaison :",
        [("a", "baliser les lieux"),
         ("b", "caler le véhicule"),
         ("c", "faire appel à son mécanicien")],
        "Réponse : a-b", 177, tags=["multi-reponses"]))

    questions.append(q(921, "Extincteur feu d'hydrocarbures", "Quel type d’extincteur faut-il recommander pour combattre un feu d’hydrocarbure ?",
        [("a", "extincteur à poudre"),
         ("b", "extincteur à eau"),
         ("c", "extincteur à mousse ou CO2"),
         ("d", "extincteur polyvalent ABC")],
        "Réponse a-c-d", 177, tags=["multi-reponses"], exp="L'eau pure ne doit jamais être utilisée sur un feu de carburant/huile (risque de projection et d'extension du feu)."))

    questions.append(q(922, "Anomalies de freinage", "Je fais contrôler le système de freinage :",
        [("a", "Si la voiture se déporte à droite ou à gauche au freinage"),
         ("b", "Si la course de la pédale est trop longue"),
         ("c", "Si j’entends des grincements au freinage"),
         ("d", "Si mes feux de position ne s’allument pas au freinage")],
        "Réponse a-b-c", 177, tags=["multi-reponses"]))

    questions.append(q(923, "Économies de carburant astuces", "Pour réduire la consommation du carburant il faut :",
        [("a", "avoir le système d’allumage bien régler"),
         ("b", "rouler avec porte-bagages chargé"),
         ("c", "rouler avec des pneumatiques bien gonflés"),
         ("d", "adapter la vitesse au régime du moteur")],
        "Réponse a-c-d", 177, tags=["multi-reponses"]))

    questions.append(q(924, "Moyens de pré-signalisation", "La pré-signalisation doit être indiquée par :",
        [("a", "les plaques d’immatriculation"),
         ("b", "les feux de croisement"),
         ("c", "le signal de détresse"),
         ("d", "le triangle de pré-signalisation")],
        "Réponse c-d", 177, tags=["multi-reponses"]))

    questions.append(q(925, "Feux avant obligatoires tourisme", "Quels sont les feux obligatoires à l’avant d’un véhicule de tourisme :",
        [("a", "deux feux de route – deux feux de croisement – deux feux stop – deux feux de position – deux indicateurs de changement de direction – deux feux antibrouillard"),
         ("b", "deux phares – deux codes – deux clignotants – deux feux de position – feux plaque d’immatriculation – deux feux anti brouillard"),
         ("c", "deux feux de route – deux indicateurs de changement de direction – deux feux de croisement – deux feux de position")],
        "Réponse c", 177, exp="A l'avant : 2 feux de route (blancs/jaunes), 2 feux de croisement, 2 clignotants, 2 feux de position."))

    questions.append(q(926, "Organes moteur 4 temps", "Quels sont les organes essentiels pour le fonctionnement d’un moteur à 4 temps ?",
        [("a", "La batterie – le carburateur – l’alternateur"),
         ("b", "Les phares – le pneu – les feux de croisement"),
         ("c", "La boite régulatrice - l’allumeur et la bougie"),
         ("d", "Les feux stop – le rétroviseur – le klaxon")],
        "Réponse a-c", 177, tags=["multi-reponses"]))

    questions.append(q(927, "Ordre 4 temps moteur essence", "Quels sont dans l’ordre les 4 temps d’un moteur à essence ?",
        [("a", "Admission – compression – échappement – explosion"),
         ("b", "Compression – admission – explosion – échappement"),
         ("c", "Admission – compression – explosion – échappement")],
        "Réponse c", 178, exp="Ordre chronologique fondamental : 1. Admission, 2. Compression, 3. Explosion (temps moteur), 4. Échappement."))

    questions.append(q(928, "Panonceau remorque PTAC", "Ce panonceau concerne les véhicules tractant une remorque d’un PTAC de :",
        [("a", "Plus de 250 kilogrammes"),
         ("b", "240 kilogrammes"),
         ("c", "80 kilogrammes")],
        "Réponse : a", 178, tags=["chiffre"], img="M6c"))

    questions.append(q(929, "Allumage feux stop", "Les feux de stop s’allument lorsque :",
        [("a", "Je rétrograde"),
         ("b", "Je freine avec la pédale"),
         ("c", "J’enclenche la marche arrière"),
         ("d", "Je change de direction")],
        "Réponse : b", 178, exp="Les feux stop rouges s'allument dès que le conducteur actionne la pédale de frein de service."))

    questions.append(q(930, "Éléments de suspension", "Les éléments qui font partie de la suspension d’un véhicule automobile sont :",
        [("a", "Les ressorts et la transmission"),
         ("b", "Les pneus"),
         ("c", "Les amortisseurs et la boite de vitesses"),
         ("d", "Les ressorts et les amortisseurs")],
        "Réponse : b, d", 178, tags=["multi-reponses"]))

    return questions

if __name__ == '__main__':
    qs = get_chapitre11_questions()
    print(f"Chapitre 11 loaded: {len(qs)} questions")
