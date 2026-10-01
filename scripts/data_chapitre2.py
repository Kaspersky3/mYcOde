# Chapter 2: Signalisation (Questions 1 to 205)
# Extracted from DGTT 2011 pages 9 to 41

def get_chapitre2_questions():
    questions = []
    
    # helper
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
            "chapitre": 2,
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

    # Pages 9-11
    questions.append(q(1, "Signalisation générale", "Quelles sont les différentes signalisations routières ?", 
        [("a", "La signalisation verticale, horizontale, lumineuse et les signes des agents"),
         ("b", "Les intersections en X, en Y et en T"),
         ("c", "Les lignes continues, les lignes discontinues et les lignes mixtes")],
        "Réponse a", 9, exp="Le manuel distingue 4 grands types de signalisation : verticale (panneaux), horizontale (marquages), lumineuse (feux) et signes des agents."))
    
    questions.append(q(2, "Signalisation horizontale", "La signalisation horizontale est :",
        [("a", "L’ensemble des marques peintes sur la chaussée"),
         ("b", "L’ensemble des signes des agents de sécurité"),
         ("c", "L’ensemble des règles applicables en agglomération")],
        "Réponse a", 9))

    questions.append(q(3, "Signalisation horizontale", "La ligne continue blanche centrale :",
        [("a", "Autorise le dépassement"),
         ("b", "Interdit le dépassement"),
         ("c", "Est réservée pour l’arrêt des bus")],
        "Réponse b", 9, exp="Une ligne continue blanche centrale interdit formellement le franchissement et le dépassement."))

    questions.append(q(4, "Signalisation horizontale", "La ligne discontinue blanche centrale :",
        [("a", "Interdit la circulation à droite"),
         ("b", "Autorise le dépassement"),
         ("c", "Est réservée pour l’arrêt des bus")],
        "Réponse b", 9))

    questions.append(q(5, "Signalisation horizontale", "Les traits de la ligne discontinue blanche centrale hors agglomération ont une longueur de :",
        [("a", "20m"), ("b", "1,33m"), ("c", "3m")],
        "Réponse c", 9, diff=2, tags=["chiffre"], exp="Hors agglomération, les traits de guidage mesurent 3 m avec un intervalle de 10 m."))

    questions.append(q(6, "Signalisation horizontale", "La ligne mixte autorise le dépassement :",
        [("a", "Si la ligne discontinue est plus proche du conducteur"),
         ("b", "Si la ligne continue est plus proche du conducteur"),
         ("c", "Si la chaussée est assez large")],
        "Réponse a", 9))

    questions.append(q(7, "Marquage sur trottoir", "La ligne jaune continue sur la bordure du trottoir :",
        [("a", "Interdit le stationnement"),
         ("b", "Autorise l’arrêt"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponse a", 9, exp="La ligne jaune continue sur la bordure interdit le stationnement (et selon les règles générales l'arrêt également)."))

    questions.append(q(8, "Signalisation horizontale", "L’intervalle entre deux traits d’une ligne discontinue blanche centrale est de :",
        [("a", "10m"), ("b", "5m"), ("c", "15m")],
        "Réponse a", 10, diff=2, tags=["chiffre"]))

    questions.append(q(9, "Marquage sur trottoir", "La ligne jaune discontinue sur la bordure du trottoir :",
        [("a", "Interdit le stationnement"),
         ("b", "Autorise l’arrêt"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponses a-b", 10, tags=["piege", "multi-reponses"], exp="Une ligne jaune discontinue sur le trottoir interdit le stationnement tout en autorisant l'arrêt temporaire."))

    questions.append(q(10, "Marquage arrêt de bus", "La ligne jaune brisée en bordure de la chaussée :",
        [("a", "Interdit le dépassement"),
         ("b", "Autorise le dépassement"),
         ("c", "Indique une zone d’arrêt de bus")],
        "Réponse c", 10))

    questions.append(q(11, "Flèches de rabattement", "A la vue de la flèche de rabattement, je dois :",
        [("a", "M’arrêter"), ("b", "Serrer ma droite"), ("c", "Rétrograder"), ("d", "Dépasser")],
        "Réponse b", 10))

    questions.append(q(12, "Autoroute et BAU", "La circulation sur les bandes d’arrêt d’urgence de l’autoroute est autorisée :",
        [("a", "Aux ambulances effectuant un transport urgent de blessés"),
         ("b", "A tous les véhicules en cas d’embouteillage"),
         ("c", "Aux services d’entretien se rendant sur un lieu d’intervention"),
         ("d", "Aux véhicules prioritaires en mission")],
        "Réponses a-c-d", 10, diff=2, tags=["multi-reponses"]))

    questions.append(q(13, "Marquage sur trottoir", "La bande rouge discontinue de blanc le long du trottoir, interdit :",
        [("a", "L’arrêt"), ("b", "Le stationnement"), ("c", "L’arrêt pour les véhicules légers")],
        "Réponse b", 10))

    questions.append(q(14, "Marquage au sol - Zébras", "Sur les lignes hachurées appelées zébras :",
        [("a", "Je peux stationner"), ("b", "Je peux circuler"), ("c", "Je ne peux ni stationner, ni circuler, ni m’arrêter"), ("d", "Je peux m’arrêter")],
        "Réponse c", 10))

    questions.append(q(15, "Panneaux d'indication", "A la vue du panneau C13 :",
        [("a", "Je suis sur un chemin sans issue"),
         ("b", "Je suis prioritaire à la prochaine intersection"),
         ("c", "Je dois aller tout droit seulement")],
        "Réponse a", 11, img="C13"))

    questions.append(q(16, "Priorité et Arrêt", "A la rencontre du panneau \"STOP\" que dois-je faire ?",
        [("a", "Je cède le passage à droite"),
         ("b", "Je cède le passage à droite et à gauche"),
         ("c", "Je m’arrête avant le panneau et je cède le passage aux usagers venant de ma droite et de ma gauche"),
         ("d", "Je m’arrête après le panneau et je cède le passage aux usagers venant de ma gauche et de ma droite")],
        "Réponse d", 11, img="AB4_STOP", diff=2, tags=["piege"], exp="Attention au piège de formulation du manuel : l'arrêt physique s'effectue à la ligne blanche d'arrêt (souvent située après le panneau)."))

    questions.append(q(17, "Panneaux de danger", "Que signifie le panneau A15 c ?",
        [("a", "Voie réservée aux chevaux"),
         ("b", "Endroits fréquentés par les animaux domestiques"),
         ("c", "Passage de cavaliers")],
        "Réponse c", 11, img="A15c"))

    questions.append(q(18, "Panneaux de danger", "Que m’indique le panneau A19 ?",
        [("a", "Chute de grêle"),
         ("b", "Chute de neige"),
         ("c", "Risque de chute de pierres sur la chaussée"),
         ("d", "Présence de pierres sur la chaussée")],
        "Réponse c et d", 11, img="A19", tags=["multi-reponses"]))

    questions.append(q(19, "Panneaux de danger", "Que signifie le panneau A21a ?",
        [("a", "Voie réservée aux cyclistes"),
         ("b", "Débouché de cyclistes ou cyclomotoristes venant de droite ou de gauche"),
         ("c", "Débouché de cyclistes ou de cyclomotoristes venant de droite seulement")],
        "Réponse b", 11, img="A21a"))

    questions.append(q(20, "Panneaux de priorité", "Devant le panneau triangulaire pointe en bas, que dois-je faire ?",
        [("a", "Je cède le passage à droite et à gauche"),
         ("b", "Je cède le passage à droite seulement"),
         ("c", "Je passe")],
        "Réponse a", 11, img="AB3a"))

    questions.append(q(21, "Panneaux de priorité", "Qu’indique le panneau triangulaire portant une flèche barrée ?",
        [("a", "Arrêt obligatoire"), ("b", "Priorité à droite"), ("c", "Priorité à gauche"), ("d", "Priorité de passage")],
        "Réponse d", 11, img="AB2"))

    questions.append(q(22, "Panneaux de priorité", "A la vue du panneau AB6 que dois-je faire à la prochaine intersection ?",
        [("a", "Je m’arrête"), ("b", "Je cède le passage à droite"), ("c", "Je passe"), ("d", "Je cède le passage à gauche")],
        "Réponse c", 12, img="AB6", exp="AB6 indique une route à caractère prioritaire : vous avez la priorité de passage."))

    questions.append(q(23, "Panneaux de danger", "Que m’indique le panneau A1d1 ?",
        [("a", "Succession de virage dont le 1er est à droite à 5 km"),
         ("b", "Succession de virage sur 5 km dont le 1er est à gauche"),
         ("c", "Succession de virage sur 5 km dont le 1er est à droite")],
        "Réponse b", 12, img="A1d1", diff=2, tags=["piege", "chiffre"]))

    questions.append(q(24, "Panneaux de danger", "Que signifie le panneau A3a1 ?",
        [("a", "Chaussée rétrécie par la gauche à 200m"),
         ("b", "Chaussée rétrécie par la droite sur 200m"),
         ("c", "Chaussée rétrécie par la gauche sur 200m"),
         ("d", "Chaussée rétrécie par la droite à 200m")],
        "Réponse d", 12, img="A3a1", diff=2, tags=["piege", "chiffre"], exp="Le panonceau sans flèches latérales indique une distance (« à 200m ») et non une étendue (« sur 200m »)."))

    questions.append(q(25, "Panneaux d'intersection", "A la vue du panneau triangulaire pointe en bas à une intersection, quel genre de panneau peuvent rencontrer les usagers venant de gauche et de droite ?",
        [("a", "Panneau \"STOP\""),
         ("b", "Panneau losange fond jaune barré"),
         ("c", "Panneau flèche barrée"),
         ("d", "Panneau losange fond jaune")],
        "Réponses c-d", 12, img="AB3a", tags=["multi-reponses"]))

    questions.append(q(26, "Distance d'implantation", "En agglomération, les panneaux de danger sont implantés à quelle distance du danger ?",
        [("a", "150m"), ("b", "200m"), ("c", "50m"), ("d", "250m")],
        "Réponse c", 12, tags=["chiffre"], exp="En agglomération, les panneaux de danger sont placés à 50 m avant le danger."))

    questions.append(q(27, "Distance d'implantation", "En rase campagne, à quelle distance sont implantés les panneaux de danger ?",
        [("a", "50m"), ("b", "150m"), ("c", "200m"), ("d", "250m")],
        "Réponse b", 12, tags=["chiffre"], exp="En rase campagne, les panneaux de danger sont placés à 150 m du danger."))

    questions.append(q(28, "Comportement au danger", "Que dois-je faire devant un panneau de danger ?",
        [("a", "Augmenter ma vitesse"), ("b", "Réduire ma vitesse"), ("c", "Maintenir ma vitesse")],
        "Réponse b", 13))

    questions.append(q(29, "Arrêt et stationnement", "Devant un panneau de danger :",
        [("a", "Je peux marquer un arrêt"), ("b", "Je peux stationner"), ("c", "Je ne peux ni m’arrêter ni stationner")],
        "Réponse c", 13))

    questions.append(q(30, "Panneaux de danger", "Quel danger signale le panneau A21b ?",
        [("a", "Voie réservée aux cyclistes"),
         ("b", "Voie interdite aux cyclistes"),
         ("c", "Débouché de cyclistes venant de gauche seulement"),
         ("d", "Débouché de cyclistes venant de gauche ou de droite")],
        "Réponse c", 13, img="A21b"))

    questions.append(q(31, "Panneaux de danger", "Quel danger signale le panneau A20 ?",
        [("a", "Débouché sur un pont mobile"),
         ("b", "Débouché sur un quai ou une berge"),
         ("c", "Descente dangereuse")],
        "Réponse b", 13, img="A20"))

    questions.append(q(32, "Panneaux de danger", "Quel danger signale le panneau A16 ?",
        [("a", "Débouché sur un quai ou une berge"),
         ("b", "Descente dangereuse"),
         ("c", "Débouché sur un pont mobile"),
         ("d", "Débouché sur un quai ou une berge")],
        "Réponse b", 13, img="A16"))

    questions.append(q(33, "Panneaux de danger", "Quel danger signale le panneau A6 ?",
        [("a", "Descente dangereuse"),
         ("b", "Débouché sur un pont mobile"),
         ("c", "Débouché sur un quai ou une berge")],
        "Réponse b", 13, img="A6"))

    questions.append(q(34, "Panneaux d'interdiction", "Que signifie le panneau B6a1 ?",
        [("a", "Stationnement interdit avant le panneau"),
         ("b", "Arrêt et stationnement interdits"),
         ("c", "Stationnement interdit à partir du panneau")],
        "Réponse c", 13, img="B6a1", exp="Le panneau rond bleu bordé de rouge avec une seule barre oblique interdit le stationnement à partir du panneau jusqu'à la prochaine intersection."))

    questions.append(q(35, "Panneaux d'interdiction", "A la vue du panneau B6a1 :",
        [("a", "Je peux m’arrêter avant ou après le panneau"),
         ("b", "Je peux stationner après le panneau"),
         ("c", "Je peux stationner avant le panneau")],
        "Réponses a-c", 14, img="B6a1", tags=["multi-reponses", "piege"], exp="Le stationnement est interdit après le panneau mais reste autorisé avant (si rien d'autre ne l'interdit). L'arrêt simple reste possible."))

    questions.append(q(36, "Panneaux d'interdiction de zone", "A la vue du panneau B6b1 :",
        [("a", "Je peux stationner dans la première rue à droite après le panneau"),
         ("b", "Je peux stationner dans la rue où se trouve le panneau mais à gauche"),
         ("c", "Je ne peux stationner nulle part dans la rue où se trouve le panneau")],
        "Réponse c", 14, img="B6b1"))

    questions.append(q(37, "Panneaux d'interdiction", "Le panneau B0 :",
        [("a", "M’interdit de circuler dans les deux sens"),
         ("b", "M’interdit quelque chose qui sera indiqué après"),
         ("c", "M’oblige à faire demi-tour si possible")],
        "Réponse a-c", 14, img="B0", tags=["multi-reponses"]))

    questions.append(q(38, "Panneaux d'interdiction", "Le panneau B7a :",
        [("a", "Interdit aux motocyclistes de dépasser les voitures"),
         ("b", "Interdit l’accès aux autos et aux motos"),
         ("c", "Interdit l’accès aux deux roues")],
        "Réponse b", 14, img="B7a"))

    questions.append(q(39, "Panneaux d'obligation", "A la vue du panneau B25 :",
        [("a", "Je peux rouler à 25km/h"),
         ("b", "Je peux rouler à 40km/h"),
         ("c", "Je dois rouler au moins à 30 km/h")],
        "Réponses b-c", 14, img="B25", tags=["multi-reponses"], exp="B25 indique une vitesse minimale obligatoire de 30 km/h."))

    questions.append(q(40, "Panneaux d'obligation", "Le panneau B21-1 m’oblige à :",
        [("a", "Tourner à droite à la prochaine intersection"),
         ("b", "Tourner à droite avant le panneau"),
         ("c", "Tourner à droite après le panneau")],
        "Réponse b", 14, img="B21_1", diff=2, tags=["piege"]))

    questions.append(q(41, "Balises", "La balise J4 annonce :",
        [("a", "Un virage très dangereux"),
         ("b", "Une déviation prochaine"),
         ("c", "Un rétrécissement de la chaussée")],
        "Réponse a-c", 14, img="J4", tags=["multi-reponses"]))

    questions.append(q(42, "Pistes cyclables", "Sur les bandes et les pistes cyclables :",
        [("a", "Les automobilistes peuvent s’arrêter pour prendre un passager"),
         ("b", "Les piétons peuvent circuler"),
         ("c", "Les automobilistes peuvent stationner en cas de panne"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 15))

    questions.append(q(43, "Sens giratoire", "Le panneau A25 signifie :",
        [("a", "Carrefour à sens giratoire"),
         ("b", "Terre-plein à contourner par la droite"),
         ("c", "Céder le passage aux usagers venant de droite"),
         ("d", "Céder le passage aux usagers venant de gauche")],
        "Réponse a-b-d", 15, img="A25", tags=["multi-reponses"]))

    questions.append(q(44, "Panneaux de priorité", "Que signifie le panneau B15 ?",
        [("a", "Chaussée à double sens"),
         ("b", "Céder le passage aux usagers venant en sens inverse"),
         ("c", "Circulation à sens unique")],
        "Réponse b", 15, img="B15"))

    questions.append(q(45, "Panneaux de danger", "Quel danger signale le panneau A18 ?",
        [("a", "Céder le passage aux usagers venant en sens inverse"),
         ("b", "Circulation dangereuse dans les deux sens"),
         ("c", "Chaussée rétrécie dans les deux sens")],
        "Réponse b", 15, img="A18"))

    questions.append(q(46, "Distance d'implantation", "A quelle distance du danger est implanté le panneau A18 ?",
        [("a", "150m"), ("b", "50m"), ("c", "0m")],
        "Réponse c", 15, tags=["piege", "chiffre"], exp="Le panneau A18 (circulation dans les deux sens) prend effet immédiatement à hauteur du panneau (0 m)."))

    questions.append(q(47, "Panneaux de priorité en vis-à-vis", "A la rencontre du panneau B15, quel panneau l’usager venant en sens inverse aurait rencontré ?",
        [("a", "Le panneau \"sens interdit\""),
         ("b", "Le panneau \"chaussée rétrécie\""),
         ("c", "Le panneau \"priorité par rapport à la circulation venant en sens inverse\"")],
        "Réponse c", 15, img="B15"))

    questions.append(q(48, "Sens interdit et sens unique", "A la vue du panneau B1, quel panneau l’usager venant en sens inverse aurait rencontré ?",
        [("a", "Le panneau \"priorité par rapport à la circulation venant en sens inverse\""),
         ("b", "Le panneau \"céder le passage à la circulation venant en sens inverse\""),
         ("c", "Le panneau \"circulation à sens unique\"")],
        "Réponse c", 15, img="B1"))

    questions.append(q(49, "Panneaux d'interdiction", "Que signifie le panneau B8 ?",
        [("a", "Voie réservée aux véhicules de transport de marchandises"),
         ("b", "Voie réservée aux véhicules de transport en commun de personnes"),
         ("c", "Accès interdit aux véhicules de transport de marchandises")],
        "Réponse c", 16, img="B8"))

    questions.append(q(50, "Matières dangereuses", "Que signifie le panneau B18a ?",
        [("a", "Accès interdit aux véhicules transportant des produits explosifs ou facilement inflammables"),
         ("b", "Accès interdit aux véhicules transportant des produits de nature à polluer les eaux"),
         ("c", "Accès interdit aux véhicules transportant des matières dangereuses")],
        "Réponse a", 16, img="B18a"))

    questions.append(q(51, "Conduite en virage", "A la vue du panneau A1c, je ralentis :",
        [("a", "Avant chaque virage"),
         ("b", "Dans chaque virage"),
         ("c", "Après chaque virage")],
        "Réponse a", 16, img="A1c", exp="On ralentit toujours avant d'aborder le virage pour maîtriser la trajectoire et contrer la force centrifuge."))

    questions.append(q(52, "Stationnement interdit", "En présence du panneau \"stationnement interdit\", je suis autorisé à :",
        [("a", "Stationner avant le panneau"),
         ("b", "Stationner après le panneau"),
         ("c", "Stationner avant la prochaine intersection")],
        "Réponse a", 16, img="B6a1"))

    questions.append(q(53, "Hauteur limitée et panonceau", "Que signifie le panneau B12(1) :",
        [("a", "Accès interdit à 10km au véhicule dont la hauteur avec ou sans chargement dépasse 3,5m"),
         ("b", "Accès interdit sur 10km au véhicule dont la hauteur avec ou sans chargement dépasse 3,5m"),
         ("c", "Accès interdit au véhicule dont la hauteur avec ou sans chargement dépasse 3,5m"),
         ("d", "Vitesse limitée à 10km/h aux véhicules dont la hauteur avec ou sans chargement dépasse 3,5m")],
        "Réponse a", 16, diff=2, tags=["piege"]))

    questions.append(q(54, "Fin d'interdiction de dépasser", "Que signifie le panneau B34a ?",
        [("a", "Dépassement interdit aux camions"),
         ("b", "Fin d’interdiction de dépasser aux véhicules de transport de marchandise dont le PTAC excède 3,5T"),
         ("c", "Interdiction de dépasser tout véhicule"),
         ("d", "Fin d’interdiction de dépasser")],
        "Réponse b", 16, img="B34a"))

    questions.append(q(55, "Voie réservée transports en commun", "Que signifie le panneau B45 ?",
        [("a", "Accès interdit aux véhicules de transport en commun de personnes"),
         ("b", "Stationnement interdit aux véhicules de transport en commun de personnes"),
         ("c", "Fin de voie réservée aux véhicules de transport en commun de personnes"),
         ("d", "Arrêt interdit aux véhicules de transport en commun de personnes")],
        "Réponse c", 17, img="B45"))

    questions.append(q(56, "Voie réservée transports en commun", "Que signifie le panneau B27 ?",
        [("a", "Arrêt d’autobus"),
         ("b", "Parking réservé aux autobus"),
         ("c", "Voie réservée aux véhicules de transport en commun de personnes"),
         ("d", "Arrêt obligatoire aux autobus")],
        "Réponse c", 17, img="B27"))

    questions.append(q(57, "Interdiction deux-roues", "Que signifie le panneau B9g ?",
        [("a", "Accès interdit aux cyclomoteurs"),
         ("b", "Accès interdit aux motocyclistes"),
         ("c", "Accès interdit aux cyclomoteurs et aux motocyclistes"),
         ("d", "Voie réservée aux cyclomoteurs")],
        "Réponse a", 17, img="B9g"))

    questions.append(q(58, "Longueur limitée", "Que signifie le panneau B10a ?",
        [("a", "Accès interdit aux véhicules dont la longueur dépasse 10m avec ou sans chargement"),
         ("b", "Accès interdit uniquement aux véhicules de transport de marchandises dont la longueur dépasse 10m"),
         ("c", "Accès interdit uniquement aux véhicules de transport en commun de personnes dont la longueur dépasse 10m")],
        "Réponse a", 17, img="B10a"))

    questions.append(q(59, "Limitation par catégorie", "Que signifie le panneau B14(3) ?",
        [("a", "Vitesse limitée à 60km/h pour les deux roues"),
         ("b", "Vitesse limitée à 60km/h pour les cyclomoteurs"),
         ("c", "Vitesse limitée à 60km/h pour les motocyclettes"),
         ("d", "Vitesse limitée à 60km/h pour les cyclomoteurs et les motocyclettes")],
        "Réponse c", 17, img="B14_3", diff=2, tags=["piege"]))

    questions.append(q(60, "Véhicules lents", "Le panneau B29(2) :",
        [("a", "Ne concerne pas les motocyclettes roulant à moins de 60km/h"),
         ("b", "Concerne tout véhicule à moteur roulant à moins de 60km/h"),
         ("c", "Concerne seulement les véhicules automobiles roulant à moins de 60km/h")],
        "Réponse b", 17, img="B29_2"))

    questions.append(q(61, "Poids et marchandises", "Le panneau B8 interdit l’accès :",
        [("a", "A tout véhicule de transport de marchandises"),
         ("b", "Aux véhicules de transport de marchandises dont le PTAC est supérieur à 3,5T"),
         ("c", "A tout véhicule de transport")],
        "Réponse a-b", 18, img="B8", tags=["multi-reponses"]))

    questions.append(q(62, "Poids maximal", "Que signifie le panneau B13 ?",
        [("a", "Accès interdit aux véhicules pesant 5,5T"),
         ("b", "Accès interdit aux véhicules pesant plus de 5,5T"),
         ("c", "Accès interdit aux véhicules pesant moins de 5,5T")],
        "Réponse b", 18, img="B13"))

    questions.append(q(63, "Limitation avec panonceau", "Le panneau B14(4) concerne :",
        [("a", "Les véhicules de transport en commun de personnes"),
         ("b", "Les véhicules de transport de marchandises"),
         ("c", "Tout véhicule de transport"),
         ("d", "Tout véhicule de tourisme")],
        "Réponse b", 18, img="B14_4"))

    questions.append(q(64, "Comportement au danger", "A la rencontre d’un panneau de danger, que dois-je faire ?",
        [("a", "Accélérer et passer le danger signalé"),
         ("b", "Ralentir, serrer sa droite et passer en faisant attention au danger"),
         ("c", "Serrer sa droite, accélérer et passer"),
         ("d", "Faire demi-tour")],
        "Réponse b", 18))

    questions.append(q(65, "Passage à niveau", "A la rencontre du panneau A7, que dois-je faire ?",
        [("a", "Accélérer et passer"),
         ("b", "Ralentir, serrer ma droite et passer avec prudence"),
         ("c", "Ralentir, serrer ma droite et klaxonner")],
        "Réponse b", 18, img="A7"))

    questions.append(q(66, "Passage à niveau", "A quoi peut-on s’attendre à la vue du panneau A7 ?",
        [("a", "A voir les rails uniquement"),
         ("b", "A voir une barrière et des rails"),
         ("c", "A voir une barrière automatique")],
        "Réponse b", 18, img="A7", exp="A7 représente un passage à niveau avec barrière."))

    questions.append(q(67, "Passage à niveau sans barrière", "A quoi peut-on s’attendre après le panneau A8 ?",
        [("a", "A voir des rails et une barrière"),
         ("b", "A voir un panneau de position uniquement"),
         ("c", "A voir un panneau de position et des rails")],
        "Réponse c", 19, img="A8", exp="A8 représente une locomotive : passage à niveau sans barrière."))

    questions.append(q(68, "Passage à niveau sans barrière", "Que doit-on faire à la vue du panneau A8 ?",
        [("a", "Accélérer et passer en vérifiant la gauche et la droite"),
         ("b", "Ralentir, regarder à gauche et à droite avant de traverser les rails"),
         ("c", "Accélérer et passer tout simplement")],
        "Réponse b", 19, img="A8"))

    questions.append(q(69, "Endroit fréquenté par des enfants", "Que doit-on faire à la rencontre du panneau A13a ?",
        [("a", "Passer en utilisant son avertisseur sonore pour faire dégager les enfants qui se trouveraient sur la route"),
         ("b", "Ralentir, faire attention aux enfants et s’arrêter au besoin pour les laisser passer"),
         ("c", "Klaxonner et passer rapidement")],
        "Réponse b", 19, img="A13a"))

    questions.append(q(70, "Croisement et rétrécissement", "A la rencontre du panneau A3, que faire lorsqu’un véhicule arrive en sens inverse ?",
        [("a", "S’arrêter et laisser le véhicule passer"),
         ("b", "Poursuivre sa route"),
         ("c", "Serrer sa droite, s’arrêter et laisser le véhicule passer")],
        "Réponse c", 19, img="A3"))

    questions.append(q(71, "Sens interdit", "Que peut-on faire à la vue du panneau B1 ?",
        [("a", "Poursuivre sa route en ralentissant"),
         ("b", "Garer son véhicule"),
         ("c", "Changer de direction"),
         ("d", "Faire demi-tour")],
        "Réponse b-c-d", 19, img="B1", tags=["multi-reponses"]))

    questions.append(q(72, "Interdiction de dépasser", "A la vue du panneau B3 :",
        [("a", "Un véhicule peut dépasser un autre véhicule"),
         ("b", "Une voiture peut dépasser un camion"),
         ("c", "Un camion peut dépasser un autre camion"),
         ("d", "Aucun dépassement n’est autorisé")],
        "Réponse d", 19, img="B3", exp="Le panneau B3 interdit à tout véhicule automobile de dépasser les véhicules à moteur (autres que 2-roues sans side-car)."))

    questions.append(q(73, "Dépassement camions", "A la rencontre du panneau B33 (fin ou interdiction camions B3a) :",
        [("a", "A un véhicule poids lourd, de dépasser une voiture"),
         ("b", "A un véhicule poids lourd, de dépasser un autre véhicule poids lourd"),
         ("c", "A un petit véhicule de dépasser un véhicule poids lourd"),
         ("d", "A un véhicule poids lourd de croiser un véhicule léger")],
        "Réponses a-b", 19, img="B3a", tags=["multi-reponses"]))

    questions.append(q(74, "Limitation de vitesse 50", "A quelle vitesse peut-on rouler à la vue du panneau B14 (50) ?",
        [("a", "A moins de 50km /h"),
         ("b", "A 50km/h"),
         ("c", "A plus de 50km/h")],
        "Réponses a-b", 20, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(75, "Priorité en sens inverse", "Que doit-on faire à la vue du panneau B15 ?",
        [("a", "Passer sans prendre en compte, l’usager venant en sens inverse"),
         ("b", "Passer en serrant sa droite"),
         ("c", "S’arrêter pour laisser l’usager venant en sens inverse")],
        "Réponse c", 20, img="B15"))

    questions.append(q(76, "Obligation de tourner", "Que doit-on faire à la vue du panneau B21c1 ?",
        [("a", "Tourner immédiatement à droite"),
         ("b", "Tourner à droite à la prochaine intersection"),
         ("c", "Tourner à droite avant le panneau")],
        "Réponse b", 20, img="B21c1"))

    questions.append(q(77, "Vitesse minimale 30", "A quelle vitesse peut-on rouler à la vue du panneau B25 (30) ?",
        [("a", "A moins de 30km/h"),
         ("b", "A la vitesse voulue"),
         ("c", "A 30km/h"),
         ("d", "A plus de 30km/h")],
        "Réponses c-d", 20, img="B25", tags=["multi-reponses"]))

    questions.append(q(78, "Fin d'interdiction B31", "Que m’indique le panneau B31 ?",
        [("a", "La fin de toutes les intersections sauf le panneau \"STOP\""),
         ("b", "La fin de tous les panneaux"),
         ("c", "La fin de tous les panneaux d’interdiction sauf ceux de stationnement et d’arrêt interdit")],
        "Réponse c", 20, img="B31", exp="Le panneau de fin de toutes interdictions ne met pas fin aux interdictions de stationnement et d'arrêt."))

    questions.append(q(79, "Fin de limitation de vitesse", "A quelle vitesse peut-on rouler à la vue du panneau B33 (fin 50) ?",
        [("a", "A n’importe quelle vitesse tout en respectant la règlementation en vigueur"),
         ("b", "A moins de 50km/h"),
         ("c", "A plus de 50km/h")],
        "Réponses a-b-c", 20, img="B33", tags=["multi-reponses"]))

    questions.append(q(80, "Fin d'interdiction de dépasser", "Qu’indique le panneau B34 ?",
        [("a", "Le dépassement est interdit à tous véhicules"),
         ("b", "Il est mis fin à l’interdiction de dépasser à tout véhicule"),
         ("c", "Il est mis fin à l’interdiction aux petits véhicules seuls de se dépasser")],
        "Réponse b", 20, img="B34"))

    questions.append(q(81, "Croix de Saint-André", "Que doit-on faire à la rencontre du panneau G1 ?",
        [("a", "Passer les rails très rapidement"),
         ("b", "Ralentir pour passer les rails"),
         ("c", "Ralentir, s’assurer qu’aucun train n’arrive ni de droite ni de gauche sur les rails avant de passer")],
        "Réponse c", 21, img="G1"))

    questions.append(q(82, "Ordre feux tricolores", "Les feux tricolores s’allument dans l’ordre suivant :",
        [("a", "Vert-jaune-rouge"),
         ("b", "Jaune-vert-rouge"),
         ("c", "Rouge-vert-jaune")],
        "Réponses a-c", 21, tags=["ambiguite", "multi-reponses"], exp="Le manuel valide deux séquences selon le point de départ du cycle : vert-jaune-rouge et rouge-vert-jaune."))

    questions.append(q(83, "Comportement au feu vert", "Au feu vert :",
        [("a", "Je passe sans ralentir"),
         ("b", "Je ralentis et je passe"),
         ("c", "Je ralentis et je m’arrête"),
         ("d", "Je cède le passage aux usagers venant de droite")],
        "Réponse b", 21, exp="Au feu vert, on ne s'engage pas à l'aveugle : on ralentit et s'assure que le carrefour est dégagé."))

    questions.append(q(84, "Ordre feux tricolores bis", "Les feux tricolores s’allument dans l’ordre suivant :",
        [("a", "Vert-jaune-rouge"),
         ("b", "Jaune-vert-rouge"),
         ("c", "Rouge-jaune-vert"),
         ("d", "Rouge-vert-jaune")],
        "Réponses a-d", 21, tags=["ambiguite", "multi-reponses"]))

    questions.append(q(85, "Feu rouge", "A une intersection munie de feux tricolores dont le rouge est allumé, que faire ?",
        [("a", "Je passe si je veux tourner à droite"),
         ("b", "Je ralentis et je passe si la voie est libre"),
         ("c", "Je m’arrête")],
        "Réponse c", 21))

    questions.append(q(86, "Agent vs Feux", "A une intersection munie de feux tricolore où un agent de sécurité réglemente la circulation, que faire ?",
        [("a", "Je suis les indications de l’agent de sécurité"),
         ("b", "Je respecte les feux"),
         ("c", "Je passe si le feu est au vert")],
        "Réponse a", 21, exp="Les ordres et gestes des agents prévalent toujours sur les feux et tous les autres signaux."))

    questions.append(q(87, "Ordre feux tricolores ter", "Dans quel ordre s’allument les feux tricolores :",
        [("a", "Rouge-jaune-vert"),
         ("b", "Jaune-vert-rouge"),
         ("c", "Vert-jaune-rouge")],
        "Réponse c", 21))

    questions.append(q(88, "Feu vert allumé", "A une intersection munie de feux tricolores dont le feu vert est allumé, que dois-je faire ?",
        [("a", "Je m’arrête"),
         ("b", "Je ralentis et je m’arrête"),
         ("c", "Je passe avec prudence")],
        "Réponse c", 22))

    questions.append(q(89, "Feu jaune", "Le feu jaune annonce :",
        [("a", "Le feu vert"), ("b", "Le feu rouge"), ("c", "Le feu orange")],
        "Réponse b", 22))

    questions.append(q(90, "Feu orange fixe", "A une distance raisonnable du feu orange fixe ; je me prépare :",
        [("a", "A passer"), ("b", "A m’arrêter"), ("c", "A céder le passage")],
        "Réponse b", 22))

    questions.append(q(91, "Feu jaune clignotant", "A une intersection munie de feux tricolores où seul le feu jaune clignote :",
        [("a", "Je m’arrête"),
         ("b", "Je ralentis et je passe"),
         ("c", "J’applique la règle de priorité à droite")],
        "Réponse c", 22, exp="Le feu jaune clignotant sans panneau associé signifie l'application de la règle générale de priorité à droite."))

    questions.append(q(92, "Feux clignotant avec panneau", "Aux feux tricolores munis de panneau, dont le jaune seul clignote :",
        [("a", "Je me conforme au panneau"),
         ("b", "Je me conforme au feu jaune clignotant"),
         ("c", "J’applique la priorité à droite")],
        "Réponse a", 22, exp="Quand les feux sont clignotants ou en panne, on applique la signalisation des panneaux implantés sur le mât."))

    questions.append(q(93, "Feu rouge et virage", "Aux feux tricolores dont le rouge est allumé :",
        [("a", "Je passe avec prudence"),
         ("b", "Je m’arrête"),
         ("c", "Je ralentis, je serre ma droite et je tourne")],
        "Réponse b", 22))

    questions.append(q(94, "Feux normaux et panneau", "Aux feux tricolores fonctionnant normalement et munis de panneau :",
        [("a", "Je me conforme au panneau"),
         ("b", "Je me conforme aux feux"),
         ("c", "Je passe librement")],
        "Réponse b", 22, exp="Quand les feux fonctionnent normalement, ils prévalent sur les panneaux de priorité."))

    questions.append(q(95, "Feux éteints", "A une intersection munie de feux tricolores où tous les feux sont éteints :",
        [("a", "Je pratique la règle de la priorité à droite"),
         ("b", "Je cède le passage à droite et à gauche"),
         ("c", "J’ai la priorité de passage")],
        "Réponse a", 23))

    questions.append(q(96, "Rôle de l'agent", "Quel est le rôle de l’agent de sécurité à l’intersection ?",
        [("a", "Réglementer la circulation"),
         ("b", "Perturber la circulation"),
         ("c", "Contrôler les pièces"),
         ("d", "Surveiller les passants")],
        "Réponse a", 23))

    questions.append(q(97, "Geste de l'agent de profil", "Lorsque vous voyez de profil l’agent réglementant la circulation, que faire ?",
        [("a", "Je m’arrête"), ("b", "Je cède le passage à droite"), ("c", "Je passe"), ("d", "Je ralentis pour céder le passage")],
        "Réponse c", 23, exp="Profil = PASSAGE AUTORISÉ (équivaut au feu vert)."))

    questions.append(q(98, "Geste de l'agent face ou dos", "Lorsque je vois de face ou de dos l’agent réglementant la circulation, que faire ?",
        [("a", "Je passe"), ("b", "Je ralentis et je passe"), ("c", "Je m’arrête"), ("d", "J’accélère")],
        "Réponse c", 23, exp="Face ou dos = ARRÊT OBLIGATOIRE (équivaut au feu rouge)."))

    questions.append(q(99, "Bras levé de l'agent", "Quand l’agent de sécurité réglementant la circulation lève le bras, que faire ?",
        [("a", "Je passe si je suis engagé dans l’intersection"),
         ("b", "Je ralentis et je passe, si je le vois de face"),
         ("c", "Je ralentis et je m’arrête, si je le vois de face")],
        "Réponse a-c", 23, tags=["multi-reponses"]))

    questions.append(q(100, "Hiérarchie des signaux", "De toutes les signalisations routières, laquelle prime sur les autres ?",
        [("a", "La signalisation lumineuse"),
         ("b", "La signalisation horizontale"),
         ("c", "La signalisation verticale"),
         ("d", "Les signes des agents")],
        "Réponse d", 23, exp="Hiérarchie absolue : 1. Agents > 2. Feux lumineux > 3. Panneaux (verticale) > 4. Marquages (horizontale) > 5. Priorité à droite."))

    questions.append(q(101, "Agent face ou dos bis", "A la vue de face ou de dos d’un agent réglementant la circulation :",
        [("a", "Je passe"), ("b", "Je m’arrête"), ("c", "J’applique la règle de la priorité à droite")],
        "Réponse b", 23))

    questions.append(q(102, "Agent de profil bis", "A la vue de profil d’un agent réglementant la circulation :",
        [("a", "Je passe"), ("b", "Je m’arrête"), ("c", "J’applique la règle de priorité à droite")],
        "Réponse a", 24))

    questions.append(q(103, "Panneau AB2 priorité ponctuelle", "Le panneau triangle – flèche barrée (AB2) annonce que :",
        [("a", "Les usagers venant de gauche et de droite ont la priorité de passage"),
         ("b", "Les usagers arrivant de gauche ou de droite perdent la priorité"),
         ("c", "Seuls les usagers arrivant de gauche perdent la priorité")],
        "Réponse b", 24, img="AB2"))

    questions.append(q(104, "Arrêt STOP AB4", "A la vue de la signalisation «STOP\" (AB4), le conducteur doit :",
        [("a", "Marquer un arrêt et céder le passage à gauche et à droite"),
         ("b", "Céder le passage à droite seulement"),
         ("c", "Marquer l’arrêt après le panneau")],
        "Réponse a", 24, img="AB4_STOP"))

    questions.append(q(105, "Intersection feu clignotant", "Que faire à une intersection munie de feux tricolores dont le feu jaune clignote ?",
        [("a", "Céder le passage à ma gauche"),
         ("b", "Céder le passage à ma droite"),
         ("c", "Appliquer la priorité de passage")],
        "Réponse b", 24, exp="Céder le passage à sa droite revient à appliquer la priorité à droite."))

    questions.append(q(106, "Arrêt STOP AB4 bis", "A la vue du panneau \"STOP\" (AB4), que dois-je faire ?",
        [("a", "Je cède le passage à droite"),
         ("b", "Je cède le passage à droite et à gauche"),
         ("c", "Je m’arrête et je cède le passage aux usagers venant de ma droite et de ma gauche")],
        "Réponse c", 24, img="AB4_STOP"))

    questions.append(q(107, "Cédez le passage AB3a", "A la vue du panneau triangle pointe en bas (AB3a), que dois-je faire ?",
        [("a", "Je passe"),
         ("b", "Je cède le passage à droite seulement"),
         ("c", "Je cède le passage à droite et à gauche")],
        "Réponse c", 24, img="AB3a"))

    questions.append(q(108, "Interdiction véhicules à moteur", "Le panneau B7b :",
        [("a", "Interdit le stationnement à tout véhicule à moteur sauf les camions"),
         ("b", "Interdit l’accès à tous les véhicules à moteur"),
         ("c", "Interdit l’accès à tous les véhicules sauf les camions")],
        "Réponse b", 24, img="B7b"))

    questions.append(q(109, "Arrêt et stationnement interdits B6d", "A la vue du panneau B6d :",
        [("a", "Je ne peux pas m’arrêter"),
         ("b", "Je ne peux pas m’arrêter mais je peux stationner"),
         ("c", "Je ne peux ni m’arrêter ni stationner")],
        "Réponse a-c", 25, img="B6d", tags=["multi-reponses"]))

    questions.append(q(110, "Interdiction traction animale", "Que signifie le panneau B9c ?",
        [("a", "Accès interdit aux chevaux"),
         ("b", "Accès interdit aux véhicules agricoles à moteur"),
         ("c", "Accès interdit aux véhicules à traction animal")],
        "Réponse c", 25, img="B9c"))

    questions.append(q(111, "Fin de vitesse minimale B43", "A quelle vitesse peut-on rouler à la vue du panneau B43 ?",
        [("a", "A 30 km/h"),
         ("b", "A plus de 30 km/h"),
         ("c", "A la vitesse réglementaire"),
         ("d", "A moins de 30 km/h"),
         ("e", "Rien de tout ce qui précède")],
        "Réponse a-b-c-d", 25, img="B43", tags=["ambiguite", "multi-reponses"], exp="Fin de vitesse minimale obligatoire : toutes ces vitesses sont autorisées dans le respect du code général."))

    questions.append(q(112, "Fin de vitesse minimale B43 bis", "A la vue du panneau B43 :",
        [("a", "Je respecte une vitesse de 30 km/h obligatoirement"),
         ("b", "Je peux faire plus de 30 km/h"),
         ("c", "Je peux faire moins de 30 km/h")],
        "Réponse b-c", 25, img="B43", tags=["multi-reponses"]))

    questions.append(q(113, "Précautions en virage", "Quelles sont les précautions à prendre pour aborder un virage ?",
        [("a", "Garder la même vitesse pour vite aborder le virage"),
         ("b", "Ralentir avant d’aborder le virage"),
         ("c", "Rouler au milieu de la chaussée avant d’atteindre le virage"),
         ("d", "Bien serrer la droite avant d’aborder le virage")],
        "Réponse b-d", 25, tags=["multi-reponses"]))

    questions.append(q(114, "Demi-tour interdit", "Que signifie le panneau B2c ?",
        [("a", "Interdiction de tourner à gauche"),
         ("b", "Interdiction de faire marche arrière"),
         ("c", "Interdiction de faire demi-tour jusqu’à la prochaine intersection"),
         ("d", "Interdiction de faire marche arrière jusqu’à la prochaine intersection incluse")],
        "Réponse c", 25, img="B2c"))

    questions.append(q(115, "Stationnement avant le panneau", "A la vue du panneau B6a1 :",
        [("a", "Je peux stationner avant ou après le panneau"),
         ("b", "Je peux stationner après le panneau"),
         ("c", "Je peux stationner avant le panneau"),
         ("d", "Je ne peux stationner ni avant ni après le panneau")],
        "Réponse c", 25, img="B6a1"))

    questions.append(q(116, "Obligation d'aller tout droit", "A la vue du panneau B21b :",
        [("a", "Je peux tourner à droite"),
         ("b", "Je peux tourner à gauche"),
         ("c", "Je vais tout droit à la prochaine intersection")],
        "Réponse c", 26, img="B21b"))

    questions.append(q(117, "Fin de vitesse minimale B43 ter", "Que signifie le panneau B43 ?",
        [("a", "Stationnement interdit à 30m devant le panneau"),
         ("b", "Stationnement interdit à 30m après le panneau"),
         ("c", "Fin de vitesse minimale obligatoire")],
        "Réponse c", 26, img="B43"))

    questions.append(q(118, "Sens unique C12", "Que signifie le panneau C12 ?",
        [("a", "Obligation d’aller tout droit après le panneau"),
         ("b", "Obligation d’aller tout droit jusqu’à la prochaine intersection"),
         ("c", "Circulation à sens unique")],
        "Réponse c", 26, img="C12"))

    questions.append(q(119, "Débouché cycliste A21b", "Que signifie le panneau A21b ?",
        [("a", "Voie réservée au cycliste"),
         ("b", "Voie interdite au cycliste"),
         ("c", "Débouché de cycliste venant de gauche seulement")],
        "Réponse c", 26, img="A21b"))

    questions.append(q(120, "Limitation 50 B14", "A la vue du panneau B14 (50) :",
        [("a", "Je peux rouler à plus de 50km/h"),
         ("b", "Je ne peux pas rouler à moins de 50km/h"),
         ("c", "Je peux rouler à 50km/h strictement"),
         ("d", "Je ne suis pas concerné pas cette signalisation"),
         ("e", "Je peux rouler à moins de 50km/h")],
        "Réponse c-e", 26, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(121, "Limitation 50 B14 bis", "A la vue du panneau B14 (50) :",
        [("a", "Je peux rouler à plus de 50km/h"),
         ("b", "je peux rouler à moins de 50km/h"),
         ("c", "Je peux rouler à 50km/h strictement"),
         ("d", "Je ne suis pas concerner pas cette signalisation")],
        "Réponse b-c", 26, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(122, "Limitation avec panonceau moto", "En voiture à la vue du panneau B14 (3) hors agglomération :",
        [("a", "Je peux rouler à plus de 60km/h"),
         ("b", "Je peux rouler à moins de 60km/h"),
         ("c", "Je peux rouler à 60km/h strictement"),
         ("d", "Je ne suis pas concerné par cette signalisation")],
        "Réponse a-b-c-d", 27, img="B14_3", tags=["ambiguite", "multi-reponses"], exp="Le panonceau moto ne visant que les motos, la voiture n'est pas contrainte par ce 60 km/h."))

    questions.append(q(123, "Fin d'interdiction de dépasser B3", "Quels sont les panneaux qui mettent fin à ce panneau (B3) ?",
        [("a", "Panneau de fin de toutes interdictions"),
         ("b", "Panneau B34a (fin interdiction camions)"),
         ("c", "Panneau B34 (fin interdiction générale)"),
         ("d", "Panneau d'entrée d'agglomération (Dassa / RIE)")],
        "Réponse a-c-d", 27, img="B3_fin", tags=["multi-reponses", "piege"]))

    questions.append(q(124, "Entrée d'agglomération", "A la vue du panneau indiquant l’entrée d’une localité, quelles sont les règles à observer ?",
        [("a", "vitesse limitée à 50km/h"),
         ("b", "perte du caractère prioritaire de la route"),
         ("c", "usage de l’avertisseur sonore interdit, sauf cas de danger")],
        "Réponse a-b-c", 27, img="EB10", tags=["multi-reponses", "chiffre"], exp="L'entrée d'agglomération impose 3 effets majeurs : vitesse max 50 km/h, fin de la route prioritaire, et interdiction du klaxon sauf danger immédiat."))

    questions.append(q(125, "Flèches de rabattement sur chaussée", "Sur une chaussée à double sens comportant plus de deux voies, les flèches de rabattement peintes sur une voie :",
        [("a", "me demande de quitter le plus tôt cette voie"),
         ("b", "m’annoncent la présence très proche d’une ligne continue"),
         ("c", "me demandent de garer sur l’accotement"),
         ("d", "me demandent de tourner à droite à la prochaine intersection")],
        "Réponse a", 27))

    questions.append(q(126, "Flèches de sélection", "Sur une chaussée à plusieurs voies, des flèches de sélection aussi appelées flèches directionnelles peuvent jouer les rôles suivants :",
        [("a", "m’indiquent la voie que je dois emprunter selon la direction ou je veux aller.je gagne cette voie dès la première flèche"),
         ("b", "pour tourner, je me place dans la voie comportant des flèches orientées vers la direction que je veux emprunter"),
         ("c", "pour aller tout droit, je me place dans la voie comportant des flèches droites"),
         ("d", "les voies peuvent comporter des flèches bifides (à deux pointes), donnant le choix entre deux directions"),
         ("e", "m’obligeant à m’arrêter pour chercher la direction dans laquelle je dois aller")],
        "Réponse a-b-c-d", 27, tags=["multi-reponses"]))

    questions.append(q(127, "Double sens à 150m A18-1", "A la vue du panneau A18-1 :",
        [("a", "La circulation est alternée à 150m"),
         ("b", "La circulation est alternée sur 150m"),
         ("c", "Circulation à double sens à 150m")],
        "Réponse c", 28, img="A18_1"))

    questions.append(q(128, "Stationnement interdit après panneau", "A la vue du panneau B6a1 il est interdit :",
        [("a", "de s’arrêter avant le panneau"),
         ("b", "de stationner avant le panneau"),
         ("c", "de s’arrêter après le panneau"),
         ("d", "de stationner après le panneau")],
        "Réponse d", 28, img="B6a1"))

    questions.append(q(129, "Balises d'intersection J3", "Les balises (J3) à anneau rouge :",
        [("a", "Indiquent le régime de priorité à appliquer"),
         ("b", "Précisent la position d’une intersection"),
         ("c", "Délimitent la chaussée")],
        "Réponse b", 28, img="J3", exp="Les balises J3 (blanches avec anneau rouge) précisent la position exacte d'une intersection."))

    questions.append(q(130, "Signalisation entrée d'agglomération", "Cette signalisation (panneau d'entrée Savè) indique :",
        [("a", "une entrée d’agglomération"),
         ("b", "une fin d’interdiction de klaxonner"),
         ("c", "une limitation de vitesse"),
         ("d", "une interdiction de klaxonner")],
        "Réponse a, c, d", 28, img="EB10_Save", tags=["multi-reponses"]))

    questions.append(q(131, "Fin d'interdiction B31 portée", "Le panneau (B31) peut mettre fin à une interdiction :",
        [("a", "de dépasser"),
         ("b", "de s’arrêter"),
         ("c", "de stationner"),
         ("d", "de rouler à plus de 70km")],
        "Réponse a, d", 28, img="B31", tags=["multi-reponses", "piege"]))

    questions.append(q(132, "Virages successifs A1c", "A la vue de ce panneau A 1c :",
        [("a", "je vais aborder une succession de virage"),
         ("b", "je dois accélérer pour réduire les effets de la force centrifuge"),
         ("c", "je dois réduire ma vitesse avant le premier virage pour diminuer les effets de la force centrifuge")],
        "Réponse a, c", 28, img="A1c", tags=["multi-reponses"]))

    questions.append(q(133, "Signalisation temporaire couleur", "Quelle couleur utilise-t-on pour distinguer la signalisation temporaire de la permanente ?",
        [("a", "verte"), ("b", "rouge"), ("c", "jaune"), ("d", "bleue")],
        "Réponse c", 28, exp="La couleur jaune caractérise la signalisation temporaire (chantiers, déviations)."))

    questions.append(q(134, "Feux bicolores", "Les feux bicolores permettent de réglementer :",
        [("a", "la circulation par voie"),
         ("b", "la circulation par véhicule"),
         ("c", "la circulation par conducteur poids lourds")],
        "Réponse a", 29))

    questions.append(q(135, "Passage à niveau automatique", "A la vue du panneau A7-1 je dois rencontrer un passage à niveau équipé de :",
        [("a", "deux barrières à fonctionnement manuel"),
         ("b", "deux demi – barrière à fonctionnement automatique"),
         ("c", "deux demi – barrière à fonctionnement automatique avec feux clignotant")],
        "Réponse c", 29, img="A7_1"))

    questions.append(q(136, "Panneau B31 fin limitation", "Le panneau B31 peut signaler la fin :",
        [("a", "d’une route à caractère prioritaire"),
         ("b", "d’une limitation de vitesse"),
         ("c", "d’une interdiction de stationnement"),
         ("d", "d’une interdiction d’arrêter")],
        "Réponse b", 29, img="B31"))

    questions.append(q(137, "Priorité ponctuelle AB2", "A la vue du panneau AB2, j’ai la priorité :",
        [("a", "a la prochaine intersection"),
         ("b", "A toutes les intersections"),
         ("c", "Seulement avant la prochaine intersection")],
        "Réponse a", 29, img="AB2", exp="AB2 confère la priorité uniquement à la prochaine intersection abordée."))

    questions.append(q(138, "Fin de priorité AB7", "A la vue du panneau AB7 (fin de route prioritaire), je peux rencontrer un panneau :",
        [("a", "Cédez le passage"),
         ("b", "Stop"),
         ("c", "Sens interdit"),
         ("d", "D’intersection de routes de même nature")],
        "Réponse a, b, d", 29, img="AB7", tags=["multi-reponses"]))

    questions.append(q(139, "Implantation AB1 rase campagne", "En rase campagne, le panneau AB1 est implanté à quelle distance de l’intersection ?",
        [("a", "0m"), ("b", "30m"), ("c", "50m"), ("d", "150m"), ("e", "Rien de tout ce qui précède")],
        "Réponse d", 29, img="AB1", tags=["chiffre"]))

    questions.append(q(140, "Implantation AB2 rase campagne", "En rase campagne, le panneau AB2 est implanté à combien de mètre environ de l’intersection :",
        [("a", "100 mètres"), ("b", "50 mètres"), ("c", "150 mètres"), ("d", "0 mètres"), ("e", "Rien de tout ce qui précède")],
        "Réponse c", 30, img="AB2", tags=["chiffre"]))

    questions.append(q(141, "Implantation AB2 agglomération", "En agglomération, le panneau AB2 est implanté à combien de mètre environ de l’intersection :",
        [("a", "100 mètres"), ("b", "50 mètres"), ("c", "150 mètres"), ("d", "0 mètre"), ("e", "A proximité de l’intersection")],
        "Réponse e", 30, img="AB2", tags=["piege"]))

    questions.append(q(142, "Réglementation feux tricolores", "Les feux tricolores permettent de réglementer :",
        [("a", "la circulation aux intersections"),
         ("b", "la circulation par véhicule"),
         ("c", "la circulation par conducteur de poids lourd")],
        "Réponse a", 30))

    questions.append(q(143, "Panneau AK22 gravillons", "A la vue de ce panneau (AK 22), je ralentis car :",
        [("a", "je risque de déraper"),
         ("b", "je risque de projeter des gravillons sur les autres véhicules"),
         ("c", "c’est un danger permanent")],
        "Réponse b", 30, img="AK22"))

    questions.append(q(144, "Panneau arrêt péage B5c", "A la vue de cette signalisation (B5c) :",
        [("a", "je m’arrête à la hauteur du panneau"),
         ("b", "je ralentis et poursuis ma route"),
         ("c", "je ralentis et je m’arrête au poste de péage")],
        "Réponse c", 30, img="B5c"))

    questions.append(q(145, "Double panneau B14 et B25", "A la vue de cette signalisation (B14 et B25 : max 50 et min 30) je peux rouler à :",
        [("a", "20km/h"), ("b", "40km/h"), ("c", "50km/h"), ("d", "80km/h")],
        "Réponse b, c", 30, img="B14_B25", tags=["multi-reponses", "chiffre"]))

    questions.append(q(146, "Sens interdit B1", "Ce panneau (B1) indique que :",
        [("a", "L’accès est interdit à tous les véhicules"),
         ("b", "L’accès est interdit aux véhicules à moteur seulement"),
         ("c", "La rue en sens inverse est à sens unique")],
        "Réponse a-c", 31, img="B1", tags=["multi-reponses"]))

    questions.append(q(147, "Passage piétons A13b", "Ce panneau (A13b) indique :",
        [("a", "un passage pour piétons"),
         ("b", "l’obligation aux piétons d’emprunter la voie réservée"),
         ("c", "un seul passage pour piétons"),
         ("d", "plusieurs passages aux piétons sur 100m")],
        "Réponse a, b, c", 31, img="A13b", tags=["multi-reponses", "ambiguite"]))

    questions.append(q(148, "Chaines à neige B26", "La signalisation (B26) m’oblige à mettre les chaines à neige au moins sur les deux roues motrices :",
        [("a", "oui"), ("b", "non")],
        "Réponse a", 31, img="B26"))

    questions.append(q(149, "Limitation de vitesse B14 portée", "A la vue de ce panneau (B14) la limitation de vitesse concerne :",
        [("a", "tous les véhicules"),
         ("b", "pas tous les véhicules"),
         ("c", "elle commence à hauteur du panneau"),
         ("d", "elle commence après le panneau")],
        "Réponse b, c", 31, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(150, "Animaux domestiques A15a1", "A la vue de ce panneau A15a1 :",
        [("a", "je peux rencontrer des animaux sauvages"),
         ("b", "je peux rencontrer des animaux domestiques"),
         ("c", "je ralentis")],
        "Réponse b, c", 31, img="A15a1", tags=["multi-reponses"]))

    questions.append(q(151, "Vitesse après B43", "A partir de ce panneau (B43), je peux rouler à :",
        [("a", "plus de 30 km/h"),
         ("b", "moins de 30 km/h"),
         ("c", "la vitesse voulue, en respectant la règlementation en vigueur")],
        "Réponse a-b-c", 31, img="B43", tags=["multi-reponses"]))

    questions.append(q(152, "Forme triangulaire", "Un panneau triangulaire indique :",
        [("a", "un danger"), ("b", "une obligation"), ("c", "une interdiction"), ("d", "une indication")],
        "Réponse a", 31))

    questions.append(q(153, "Forme ronde fond bleu", "Un panneau rond bleu indique :",
        [("a", "une obligation"), ("b", "une interdiction"), ("c", "une fin d’obligation"), ("d", "une fin d’interdiction")],
        "Réponse a", 32))

    questions.append(q(154, "Forme ronde bord rouge", "Un panneau rond rouge est :",
        [("a", "une obligation"), ("b", "une interdiction"), ("c", "une fin d’interdiction"), ("d", "une indication")],
        "Réponse b", 32))

    questions.append(q(155, "Panneau de travaux AK5", "Ce panneau (AK5) :",
        [("a", "est permanent"),
         ("b", "est temporaire"),
         ("c", "impose un ralentissement"),
         ("d", "n’impose pas un ralentissement")],
        "Réponse b, c", 32, img="AK5", tags=["multi-reponses"]))

    questions.append(q(156, "Virages A1d", "Ce panneau (A1d) indique :",
        [("a", "deux ou trois virages maximum"),
         ("b", "plusieurs virages"),
         ("c", "un virage")],
        "Réponse b", 32, img="A1d"))

    questions.append(q(157, "Obligation tourner à gauche B21c2", "A la vue du panneau B21c2, que faire à la prochaine intersection ?",
        [("a", "je peux tourner à gauche"),
         ("b", "je dois tourner à gauche")],
        "Réponse b", 32, img="B21c2"))

    questions.append(q(158, "Début interdiction panneau rond", "Avec un panneau rond rouge, l’interdiction commence :",
        [("a", "à hauteur du panneau"),
         ("b", "à 150m du panneau")],
        "Réponse a", 32, exp="Les panneaux de prescription (interdiction et obligation) prennent effet immédiatement à hauteur du panneau."))

    questions.append(q(159, "Panneau AK5 travaux", "Ce panneau (AK5) annonce des travaux :",
        [("a", "oui"), ("b", "non"), ("c", "c’est un signal avancé"), ("d", "c’est un signal de position")],
        "Réponse a-c", 33, img="AK5", tags=["multi-reponses"]))

    questions.append(q(160, "Virages avec panonceau distance", "Ce panneau indique :",
        [("a", "que le premier virage est à 150m"),
         ("b", "plusieurs virages à 500m"),
         ("c", "plusieurs virages sur 500m"),
         ("d", "Un ralentissement")],
        "Réponse b, d", 33, img="A1d_500m", tags=["multi-reponses", "piege"]))

    questions.append(q(161, "Danger particulier A14", "Ce signal annonce :",
        [("a", "un danger particulier"),
         ("b", "la pluie"),
         ("c", "que je dois ralentir et passer")],
        "Réponse a, c", 33, img="A14", tags=["multi-reponses"]))

    questions.append(q(162, "Couleur panneaux itinéraire", "Les panneaux indiquant les itinéraires reliant des villes importantes par la route sont de couleur :",
        [("a", "Blanche"), ("b", "Verte"), ("c", "Bleue")],
        "Réponse c", 33))

    questions.append(q(163, "Itinéraires de délestage", "Les itinéraires de délestage permettent :",
        [("a", "D’éviter les bouchons"),
         ("b", "De faciliter la circulation"),
         ("c", "D’éviter les contrôles routiers")],
        "Réponse a, b", 33, tags=["multi-reponses"]))

    questions.append(q(164, "Caractère du délestage", "Les itinéraires de délestages sont :",
        [("a", "Obligatoires"), ("b", "Facultatifs"), ("c", "Rien de tout ce qui précède")],
        "Réponse b", 33))

    questions.append(q(165, "Balises de virage", "Les balises qui positionnent un virage sont :",
        [("a", "Balise entièrement blanche"),
         ("b", "Balise avec anneau bleu"),
         ("c", "Balise avec anneau rouge"),
         ("d", "Balise avec chapeau rouge (neige)")],
        "Réponse a-d", 33, img="Balises_virage", tags=["multi-reponses"]))

    questions.append(q(166, "Indices informels", "On appelle indices « informels », les informations données :",
        [("a", "par la signalisation"),
         ("b", "par l’environnement en général")],
        "Réponse b", 34, exp="Les indices formels proviennent des panneaux et signaux officiels ; les indices informels viennent du comportement des piétons, de la météo et de l'environnement."))

    questions.append(q(167, "Zone bleue stationnement", "Ce panneau B6a1-1 indique que le stationnement est :",
        [("a", "Limité à 1h30, payant"),
         ("b", "Gratuit, à durée limitée"),
         ("c", "Payant, à durée illimitée"),
         ("d", "Payant, à durée limitée")],
        "Réponse b", 34, img="B6a1_1"))

    questions.append(q(168, "Ligne brisée bus", "A cette image Im1 P64, sur la ligne brisée à bord de ce véhicule, je peux :",
        [("a", "m’arrêter"), ("b", "stationner"), ("c", "circuler")],
        "Réponse c", 34, img="Im1_P64", exp="Sur un emplacement d'arrêt de bus marqué d'une ligne jaune brisée, on peut rouler pour franchir, mais ni s'arrêter ni stationner."))

    questions.append(q(169, "Lignes brisées chaussée", "Les lignes brisées sur une chaussée servent à :",
        [("a", "La circulation des bus"),
         ("b", "L’arrêt des bus"),
         ("c", "Le stationnement des bus"),
         ("d", "L’arrêt des camions")],
        "Réponse b", 34))

    questions.append(q(170, "Ligne jaune discontinue trottoir", "Sur cette image Im2 P64, la ligne jaune discontinue en bordure du trottoir :",
        [("a", "Interdit l’arrêt"),
         ("b", "Autorise l’arrêt"),
         ("c", "Interdit le stationnement"),
         ("d", "Autorise le stationnement")],
        "Réponse b-c", 35, img="Im2_P64", tags=["multi-reponses"]))

    questions.append(q(171, "Comportement ligne jaune discontinue", "Sur cette image Im2 P64 à bord de ce véhicule, je peux :",
        [("a", "m’arrêter"), ("b", "stationner"), ("c", "circuler")],
        "Réponse a-c", 35, img="Im2_P64", tags=["multi-reponses"]))

    questions.append(q(172, "Ligne transversale STOP", "Sur cette image Im3 P64 à bord de ce véhicule je peux :",
        [("a", "avancer à la limite de la ligne transversale"),
         ("b", "avancer à la limite de la chaussée"),
         ("c", "Franchir la ligne transversale")],
        "Réponse a", 35, img="Im3_P64"))

    questions.append(q(173, "Ligne transversale Cédez le passage", "Sur cette image Im4 P64 à bord de ce véhicule je peux :",
        [("a", "m’arrêter à la limite de la ligne transversale"),
         ("b", "franchir la ligne transversale avant de céder le passage"),
         ("c", "franchir la ligne transversale en l’absence de tout véhicule")],
        "Réponse a-c", 36, img="Im4_P64", tags=["multi-reponses"]))

    questions.append(q(174, "Arrêt Cédez le passage", "Sur cette image Im4 P64 à bord de ce véhicule, je peux :",
        [("a", "m’arrêter immédiatement"),
         ("b", "avancer à la limite de la ligne transversale"),
         ("c", "avancer à la limite de la chaussée abordée"),
         ("d", "Franchir la ligne transversale")],
        "Réponse b-c", 36, img="Im4_P64", tags=["multi-reponses"]))

    questions.append(q(175, "Marquage jaune vs blanc", "En présence d’un marquage jaune et d’un marquage blanc, je respecte :",
        [("a", "Le marquage jaune"),
         ("b", "Le marquage blanc")],
        "Réponse a", 36, exp="Le marquage temporaire jaune l'emporte toujours sur le marquage permanent blanc."))

    questions.append(q(176, "Lignes de rive", "Les lignes de rive sur une route à double sens et sur autoroute sont identiques :",
        [("a", "A gauche"), ("b", "A droite"), ("c", "Rien de tout ce qui précède")],
        "Réponse c", 36))

    questions.append(q(177, "Zone stationnement entrée ville", "Un panneau de zone de stationnement placé sur le même support qu’un panneau d’entrée d’agglomération peut concerner :",
        [("a", "Plusieurs rues"),
         ("b", "Une seule rue"),
         ("c", "Toutes les rues de l’agglomération")],
        "Réponse a-c", 37, tags=["multi-reponses"]))

    questions.append(q(178, "Obligations devant STOP", "En présence d’un panneau stop, je dois :",
        [("a", "Marquer l’arrêt au niveau du panneau"),
         ("b", "Marquer l’arrêt au niveau de la ligne"),
         ("c", "Céder le passage à gauche"),
         ("d", "Céder le passage à droite")],
        "Réponse b-c-d", 37, tags=["multi-reponses"]))

    questions.append(q(179, "Piste ou bande cyclable B22a", "Ce panneau (B 22a) indique une voie réservée :",
        [("a", "aux cycles uniquement"),
         ("b", "aux cyclistes et cyclomotoristes"),
         ("c", "à tous les véhicules")],
        "Réponse a,b", 37, img="B22a", tags=["multi-reponses"]))

    questions.append(q(180, "Interdiction tourner camion plus de 6T", "L’interdiction de tourner à droite concerne :",
        [("a", "tous les véhicules"),
         ("b", "tous les véhicules affectés au transport de marchandises de plus de 6T"),
         ("c", "les véhicules affectés au transport de marchandises dont le PTAC est supérieur à 3,5T")],
        "Réponse b", 37, img="B2b_6t"))

    questions.append(q(181, "Limitation vitesse 50 portée", "La limitation de vitesse (panneau 50) :",
        [("a", "commence à la hauteur du panneau"),
         ("b", "commence à 150m du panneau"),
         ("c", "commence à 50m du panneau"),
         ("d", "concerne tous les véhicules")],
        "Réponse a-d", 37, img="B14_50", tags=["multi-reponses"]))

    questions.append(q(182, "Chaussée glissante AK4", "Ce panneau (AK4) indique une chaussée glissante :",
        [("a", "temporaire"),
         ("b", "permanente"),
         ("c", "concerne tous les véhicules"),
         ("d", "il faut ralentir")],
        "Réponse a, c, d", 37, img="AK4", tags=["multi-reponses"]))

    questions.append(q(183, "Limitation vitesse panonceau étendue", "La limitation de vitesse (50 avec panonceau 300m fléché) :",
        [("a", "commence au panneau"),
         ("b", "commence à 300 mètres"),
         ("c", "s’étend sur 300 mètres")],
        "Réponse a, c", 37, img="B14_300m", tags=["multi-reponses", "piege"]))

    questions.append(q(184, "Définition bande cyclable", "Une voie de la chaussée réservée aux cyclistes ou aux cyclomotoristes est :",
        [("a", "une piste cyclable"),
         ("b", "une bande cyclable")],
        "Réponse b", 38, exp="Une bande cyclable fait partie intégrante de la chaussée ; une piste cyclable en est séparée."))

    questions.append(q(185, "Franchissement ligne continue", "Le franchissement ou le chevauchement d’une ligne continue :",
        [("a", "est autorisé lors d’un changement de direction"),
         ("b", "est autorisé pour dépasser un deux – roues"),
         ("c", "est toujours interdit")],
        "Réponse c", 38, exp="Le franchissement ou le chevauchement d'une ligne continue est formellement interdit en toutes circonstances."))

    questions.append(q(186, "Panneaux accompagnant feux", "Lorsque des panneaux accompagnent des feux, je respecte les panneaux si le feu est :",
        [("a", "rouge"),
         ("b", "jaune clignotant"),
         ("c", "jaune fixe"),
         ("d", "éteint")],
        "Réponse b, d", 38, tags=["multi-reponses"]))

    questions.append(q(187, "Ordres de l'agent de profil", "L’agent vu de profil peut m’indiquer :",
        [("a", "de passer"),
         ("b", "de m’arrêter"),
         ("c", "d’accélérer")],
        "Réponse a-b- c", 38, tags=["ambiguite", "multi-reponses"]))

    questions.append(q(188, "Forme ronde signification", "Les panneaux qui ont la forme ronde peuvent être des panneaux :",
        [("a", "d’obligation"),
         ("b", "d’indication"),
         ("c", "d’interdiction"),
         ("d", "de danger")],
        "Réponse a, c", 38, tags=["multi-reponses"]))

    questions.append(q(189, "Panneaux direction fond jaune", "Lorsque les panneaux de direction ont un fond jaune, il s’agit :",
        [("a", "d’indication de direction provisoire"),
         ("b", "d’itinéraires prioritaires"),
         ("c", "d’indication urgente")],
        "Réponse a", 38))

    questions.append(q(190, "Double interdiction 50 et camions", "Cette signalisation (50 et interdiction camions) :",
        [("a", "impose une limitation de vitesse aux transports de marchandises"),
         ("b", "interdit accès à tous véhicules"),
         ("c", "interdit l’accès aux véhicules de transport de marchandises"),
         ("d", "impose la limitation de vitesse à tous véhicules")],
        "Réponse c, d", 38, img="B14_B8", tags=["multi-reponses"]))

    questions.append(q(191, "Panneau circulation double sens A18", "Ce panneau A18 :",
        [("a", "signale une circulation alternée"),
         ("b", "signale une circulation dans les deux sens"),
         ("c", "prend effet à 150 mètres environ"),
         ("d", "prend effet à partir du panneau")],
        "Réponse b, d", 39, img="A18", tags=["multi-reponses", "piege"]))

    questions.append(q(192, "Panneau enfants A13a", "Ce panneau A 13a indique :",
        [("a", "la proximité d’une école"),
         ("b", "un endroit fréquenté par les enfants"),
         ("c", "un terrain de jeu"),
         ("d", "un marché")],
        "Réponse a, b, c", 39, img="A13a", tags=["multi-reponses"]))

    questions.append(q(193, "Croisement piéton A13b", "A la vue du panneau A13b :",
        [("a", "Je passe derrière le piéton en laissant un intervalle d’au moins 1m"),
         ("b", "Je passe devant le piéton qui me voit bien, en laissant un intervalle d’au moins 1m"),
         ("c", "Je klaxonne pour obliger le piéton à vite traverser"),
         ("d", "Je m’arrête pour laisser passer le piéton")],
        "Réponse a", 39, img="A13b", diff=2, tags=["piege"]))

    questions.append(q(194, "Sens unique C12 et vis-à-vis", "A la vue du panneau C12 quel panneau l’usager venant en sens inverse doit voir à l’autre bout de la chaussée ?",
        [("a", "Le panneau \"priorité par rapport à la circulation venant en sens inverse\""),
         ("b", "Le panneau \"céder le passage à la circulation venant en sens inverse\""),
         ("c", "Le panneau \"sens interdit\"")],
        "Réponse c", 39, img="C12"))

    questions.append(q(195, "Panneau B7a accès autos motos", "Le panneau B7a :",
        [("a", "Interdit le stationnement à tout véhicule léger et aux motocyclettes"),
         ("b", "Interdit l’accès aux véhicules à moteur à l’exception des cyclomoteurs"),
         ("c", "Interdit le stationnement à tout véhicule sauf les motocycles et les véhicules légers")],
        "Réponse b", 39, img="B7a"))

    questions.append(q(196, "Bande jaune continue trottoir", "La bande jaune continue le long du trottoir interdit :",
        [("a", "L’arrêt"),
         ("b", "Le stationnement"),
         ("c", "L’arrêt pour les véhicules légers seulement")],
        "Réponses a-b", 39, tags=["multi-reponses"]))

    questions.append(q(197, "Bande jaune discontinue trottoir", "La bande jaune discontinue le long du trottoir interdit :",
        [("a", "L’arrêt"),
         ("b", "Le stationnement"),
         ("c", "L’arrêt pour les véhicules légers")],
        "Réponse b", 39))

    questions.append(q(198, "Fin arrêt et stationnement interdits", "A la rencontre du panneau \"arrêt et stationnement interdits\", l’interdiction finit :",
        [("a", "Avant le panneau"),
         ("b", "A partir du panneau"),
         ("c", "15 mètres après le panneau"),
         ("d", "A la prochaine intersection")],
        "Réponse d", 40, img="B6d", exp="L'interdiction prend fin à la prochaine intersection."))

    questions.append(q(199, "Fin arrêt et stationnement interdits bis", "A la rencontre du panneau \"arrêt et stationnement interdits\", l’interdiction finit :",
        [("a", "Avant la prochaine intersection"),
         ("b", "A la prochaine intersection"),
         ("c", "30 mètres après l’intersection")],
        "Réponse b", 40, img="B6d"))

    questions.append(q(200, "Interdiction tourner à droite B2b", "Le panneau B2b :",
        [("a", "Interdit de tourner à gauche à la prochaine intersection"),
         ("b", "Interdit de tourner à droite à la prochaine intersection"),
         ("c", "Oblige à tourner à droite à la prochaine intersection"),
         ("d", "Oblige à tourner à gauche à la prochaine intersection")],
        "Réponse b", 40, img="B2b"))

    questions.append(q(201, "Interdiction tourner à gauche B2a", "Le panneau B2a :",
        [("a", "Interdit de tourner à gauche à la prochaine intersection"),
         ("b", "Interdit de tourner à gauche dans cette rue"),
         ("c", "Oblige à tourner à gauche à la prochaine intersection")],
        "Réponse a", 40, img="B2a"))

    questions.append(q(202, "Flèche jaune clignotante à droite", "A un feu tricolore, l’apparition de la flèche jaune clignotante, orientée vers la droite autorise les véhicules à tourner malgré le feu rouge, dans la voie située immédiatement à droite ; pour cela il faut :",
        [("a", "se tourner de la file de droite"),
         ("b", "manœuvrer au ralentir"),
         ("c", "céder le passage aux piétons"),
         ("d", "céder le passage aux usagers venant de la gauche et ne pas gêner ceux venant de droite")],
        "Réponse a-b-c-d", 40, tags=["multi-reponses"]))

    questions.append(q(203, "Bande sonore", "Une bande sonore sur la chaussée est :",
        [("a", "une ligne longitudinale constituée de plots délimitant les voies de circulation"),
         ("b", "une ligne uniquement réflectorisée"),
         ("c", "une ligne continue")],
        "Réponse a", 40))

    questions.append(q(204, "Utilité des bandes sonores", "Les bandes sonores sur la chaussée servent :",
        [("a", "à alerter le conducteur qui s’écarte de sa trajectoire"),
         ("b", "à rompre la monotonie"),
         ("c", "à accélérer l’apparition des signes de fatigue"),
         ("d", "à sortir le conducteur de se tromper")],
        "Réponse a-b-d", 41, tags=["multi-reponses"]))

    questions.append(q(205, "Voie de détresse", "Ce panneau signale :",
        [("a", "une voie de détresse"),
         ("b", "une rue à sens unique"),
         ("c", "une voie sans issue"),
         ("d", "un parc de stationnement")],
        "Réponse a", 41, img="C27"))

    return questions

if __name__ == '__main__':
    qs = get_chapitre2_questions()
    print(f"Chapitre 2 loaded: {len(qs)} questions")
