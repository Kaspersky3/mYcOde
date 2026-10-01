# Chapter 6: Infraction, Incivisme, Secourisme (Questions 508 to 645)
# Extracted from DGTT 2011 pages 108 to 128

def get_chapitre6_questions():
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
            "chapitre": 6,
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

    questions.append(q(508, "Zébras", "Sur les lignes hachurées appelées zébras :",
        [("a", "Je peux stationner"),
         ("b", "Je peux circuler"),
         ("c", "Je ne peux ni circuler, ni stationner")],
        "Réponse c", 108))

    questions.append(q(509, "Aptitude à la conduite", "On doit s’abstenir de conduire :",
        [("a", "Si on est sous l’effet des boissons alcoolisées ou des médicaments"),
         ("b", "Si on vient de manger sans prendre de l’alcool"),
         ("c", "Si on est fatigué et somnolant"),
         ("d", "Si on se sent nerveux")],
        "Réponse a-c-d", 108, tags=["multi-reponses"]))

    questions.append(q(510, "Usage du klaxon", "Dans quel cas utiliser les avertisseurs sonores ?",
        [("a", "Pour avertir les autres usagers"),
         ("b", "Pour rechercher les passagers"),
         ("c", "Pour saluer les autres usagers")],
        "Réponse a", 108, exp="Le klaxon sert exclusivement d'avertisseur de sécurité, jamais pour interpeller des clients ou saluer."))

    questions.append(q(511, "Documents obligatoires du véhicule", "A toute réquisition des forces de sécurité concernant mon véhicule je dois présenter :",
        [("a", "La carte grise"),
         ("b", "Les papiers de dédouanement"),
         ("c", "Le papier d’achat"),
         ("d", "L’attestation d’assurance"),
         ("e", "La visite technique")],
        "Réponse a-d-e", 108, tags=["multi-reponses"], exp="Documents obligatoires de bord : carte grise, attestation d'assurance, attestation de visite technique en cours de validité (en plus du permis de conduire)."))

    questions.append(q(512, "Respect des règles", "Les règles de circulation doivent être respectées par :",
        [("a", "Les motocyclistes"),
         ("b", "Les piétons"),
         ("c", "Les automobilistes seulement"),
         ("d", "Les automobilistes")],
        "Réponse a-b-d", 108, tags=["multi-reponses"]))

    questions.append(q(513, "Conducteur dépassé", "Quand je suis sur le point d’être dépassé, je dois :",
        [("a", "Accélérer"),
         ("b", "Je serre ma droite sans accélérer"),
         ("c", "M’arrêter")],
        "Réponse b", 108))

    questions.append(q(514, "Surcharge passagers", "Dans un véhicule à cinq places il y a infraction avec :",
        [("a", "6 passagers adultes à bord"),
         ("b", "5 passagers adultes à bord"),
         ("c", "4 passagers adultes à bord")],
        "Réponse a-b", 108, tags=["multi-reponses", "piege"], exp="Un véhicule à 5 places comprend le conducteur et 4 passagers. Avoir 5 passagers adultes (donc 6 personnes au total) constitue une surcharge."))

    questions.append(q(515, "Attention au volant", "Une bonne conduite :",
        [("a", "Nécessite une attention soutenue de ma part"),
         ("b", "M’oblige à rouler tantôt à gauche tantôt à droite"),
         ("c", "Me permet de tout regarder sur la route"),
         ("d", "M’oblige à éviter tous les trous")],
        "Réponse a", 109))

    questions.append(q(516, "Intervalle de sécurité 50 km/h", "Quelle est l’intervalle minimum de sécurité entre deux véhicules qui se suivent et roulants à 50km/h :",
        [("a", "10m environ"),
         ("b", "15m environ"),
         ("c", "20m environ")],
        "Réponse b", 109, tags=["chiffre"], exp="A 50 km/h, l'intervalle de sécurité est d'environ 15 m (distance parcourue en une seconde de réaction)."))

    questions.append(q(517, "Facteurs d'accident", "Les principaux facteurs d’accident sont :",
        [("a", "une bonne tenue de route"),
         ("b", "la fatigue"),
         ("c", "le non respect des règles de circulation"),
         ("d", "la vitesse excessive ou non adapté"),
         ("e", "la conduite dans un état d’ivresse")],
        "Réponse b-c-d-e", 109, tags=["multi-reponses"]))

    questions.append(q(518, "Médicaments et conduite", "En cas de traitement médical en cours et pour faire un long trajet, il est préférable :",
        [("a", "de modifier le traitement médical"),
         ("b", "d’arrêter le traitement médical"),
         ("c", "de se renseigner auprès de son médecin")],
        "Réponse c", 109, tags=["ambiguite"], exp="Le manuel indique 'Réponse e' par coquille typographique alors qu'il n'y a que 3 options. La bonne réponse est bien l'option c (consulter son médecin)."))

    questions.append(q(519, "Flaque d'eau", "Que dois-je faire en présence d’une flaque d’eau sur la chaussée ?",
        [("a", "Accélérer"),
         ("b", "Ralentir"),
         ("c", "M’arrêter")],
        "Réponse b", 109))

    questions.append(q(520, "Arrêt brusque devant soi", "Quel serait votre comportement si le véhicule qui vous précède s’arrête subitement ?",
        [("a", "Je m’arrête et j’apprécie la situation"),
         ("b", "Je dépasse rapidement le véhicule"),
         ("c", "Je klaxonne")],
        "Réponse a", 109))

    questions.append(q(521, "Véhicule de tourisme chargement", "Dans un véhicule pour passagers, on peut transporter :",
        [("a", "des passagers et des marchandises"),
         ("b", "des passagers et des animaux"),
         ("c", "des passagers uniquement")],
        "Réponse c", 109))

    questions.append(q(522, "Comportement du conducteur", "Au volant de son véhicule, passagers à bord, le conducteur :",
        [("a", "peut fumer"),
         ("b", "peut discuter"),
         ("c", "doit se concentrer sur la conduite")],
        "Réponse c", 110))

    questions.append(q(523, "Crevaison sans cric", "En cas de crevaison, à défaut de cric et seul à bord de votre véhicule, vous pouvez :",
        [("a", "creuser la chaussée pour changer la roue crevée"),
         ("b", "Soulever le véhicule pour changer la roue crevée"),
         ("c", "Attendre d’autres usagers de la route pour solliciter leur aide")],
        "Réponse c", 110))

    questions.append(q(524, "Panne sans triangle", "En cas de panne sur la route et à défaut des triangles de pré signalisation, je peux utiliser :",
        [("a", "des touffes d’herbes"),
         ("b", "les feux de détresse"),
         ("c", "la roue-secours")],
        "Réponse b", 110, exp="Les feux de détresse (warning) sont la signalisation de secours officielle. Les branchages ou touffes d'herbes sont des pratiques informelles dangereuses."))

    questions.append(q(525, "Piétons sur passage clouté", "Lorsque les piétons sont engagés sur le passage clouté, je dois :",
        [("a", "leur céder le passage"),
         ("b", "klaxonner pour les empêcher de traverser"),
         ("c", "leur demander d’attendre mon passage")],
        "Réponse a", 110, exp="Priorité absolue aux piétons régulièrement engagés sur un passage pour piétons."))

    questions.append(q(526, "Véhicules prioritaires", "Parmi les véhicules suivants, lesquels sont prioritaires :",
        [("a", "Les corbillards"),
         ("b", "Les véhicules des sapeurs-pompiers en mission"),
         ("c", "Les ambulances"),
         ("d", "Les véhicules militaires")],
        "Réponse b", 110))

    questions.append(q(527, "Sens interdit exception", "Parmi les véhicules suivants ; lesquels peuvent emprunter un sens interdit :",
        [("a", "les véhicules de police en mission"),
         ("b", "les corbillards"),
         ("c", "les véhicules de SAMU en mission")],
        "Réponse a-c", 110, tags=["multi-reponses"]))

    questions.append(q(528, "Canne blanche levée", "Que dois-je faire à la vue d’une personne traversant ou s’apprêtant à s’engager sur la chaussée, canne blanche levée ?",
        [("a", "Je passe rapidement"),
         ("b", "Je m’arrête pour la laisser passer"),
         ("c", "Je klaxonne")],
        "Réponse b", 110, exp="La canne blanche signale une personne malvoyante ou non-voyante : arrêt obligatoire."))

    questions.append(q(529, "Enfants traversant", "Pour aider les enfants qui attendent pour traverser la rue :",
        [("a", "Je m’arrête et leur adresse un signe de main"),
         ("b", "Je ralentis et me tiens prêt à freiner si ces enfants se décident"),
         ("c", "Je m’arrête si aucun véhicule ne vient en sens inverse"),
         ("d", "Je descends de ma voiture pour les aider à traverser")],
        "Réponse c-d", 111, tags=["multi-reponses"]))

    questions.append(q(530, "Abstention de conduire", "Je dois m’abstenir de conduire :",
        [("a", "Sous l’effet de boissons alcoolisées"),
         ("b", "Sous l’effet de la fatigue"),
         ("c", "En cas de visibilité insuffisante grave"),
         ("d", "En cas de chaussée rétrécie"),
         ("e", "En cas de défaillance du câble compteur")],
        "Réponse a-b-c", 111, tags=["multi-reponses"]))

    questions.append(q(531, "Éblouissement par véhicule venant en face", "Comment réagir quand le conducteur venant d’en face m’éblouit, malgré mes appels de feux ?",
        [("a", "j’allume et je reste en feu de route"),
         ("b", "je me protège les yeux avec la main"),
         ("c", "je ralentis au maximum et je m’arrête au besoin"),
         ("d", "je ralentis et je fixe le bord droit de la chaussée")],
        "Réponses c-d", 111, tags=["multi-reponses"]))

    questions.append(q(532, "Protocole accident PAS", "Quel est le comportement d’un usager sur un lieu d’accident ?",
        [("a", "Alerter, secourir et protéger"),
         ("b", "Secourir, protéger et alerter"),
         ("c", "Protéger, alerter et secourir")],
        "Réponse c", 111, exp="Règle d'or universelle P-A-S : 1. Protéger les lieux (éviter le suraccident), 2. Alerter les secours, 3. Secourir les victimes."))

    questions.append(q(533, "Extincteur début d'incendie", "Pour éteindre un début d’incendie dans une voiture, j’utilise :",
        [("a", "le sable uniquement"),
         ("b", "l’eau"),
         ("c", "l’extincteur")],
        "Réponse c", 111))

    questions.append(q(534, "Balisage lieu accident", "Pour baliser un lieu d’accident, j’utilise :",
        [("a", "Des balises"),
         ("b", "Des branchages"),
         ("c", "Des triangles de pré signalisation")],
        "Réponse c", 111))

    questions.append(q(535, "Distance pré-signalisation accident", "A quelle distance place-t-on ordinairement les triangles de pré-signalisation sur un lieu d’accident ?",
        [("a", "à 30m au moins"),
         ("b", "à 100m au moins"),
         ("c", "à 200m au moins")],
        "Réponse a", 111, tags=["chiffre"], exp="30 mètres au moins en amont du lieu de l'accident ou de la panne."))

    questions.append(q(536, "Secours en rase campagne", "A quelle catégorie d’agents avez-vous recours en cas d’accident en rase campagne ?",
        [("a", "Les sapeurs pompiers"),
         ("b", "les gendarmes"),
         ("c", "les douaniers"),
         ("d", "les policiers")],
        "Réponses a-b", 112, tags=["multi-reponses"], exp="En rase campagne au Bénin : Gendarmerie et Sapeurs-pompiers. En ville : Police et Sapeurs-pompiers."))

    questions.append(q(537, "Blessé réclame à boire", "Quand le blessé d’un accident de circulation réclame à boire :",
        [("a", "je lui offre de l’eau"),
         ("b", "je lui offre de l’alcool"),
         ("c", "je lui offre du jus de fruit"),
         ("d", "je ne lui donne rien")],
        "Réponse : d", 112, diff=2, tags=["piege"], exp="NE JAMAIS DONNER A BOIRE A UN BLESSÉ : risque vital d'étouffement, d'aggravation d'hémorragie interne ou de complication anesthésique."))

    questions.append(q(538, "Causes de mort avant secours", "Quelles sont les causes qui peuvent être à l’origine de la mort d’un blessé avant l’arrivée des secours ?",
        [("a", "L’hémorragie"),
         ("b", "La peur"),
         ("c", "L’asphyxie")],
        "Réponses a-c", 112, tags=["multi-reponses"]))

    questions.append(q(539, "Arrêt hémorragie externe", "Comment arrêter l’hémorragie externe ?",
        [("a", "en faisant un pansement alcoolisé"),
         ("b", "en plaçant un garrot à longue durée"),
         ("c", "en faisant un pansement compressif"),
         ("d", "en faisant une pression directe sur la plaie avec un linge propre plié"),
         ("e", "en appuyant sur les points de compression")],
        "Réponses c-d-e", 112, tags=["multi-reponses"]))

    questions.append(q(540, "Reconnaître l'asphyxie", "Comment reconnaitre une personne asphyxiée ?",
        [("a", "Par l’arrêt du mouvement du ventre et de la poitrine"),
         ("b", "Par l’arrêt du pouls"),
         ("c", "Par le mouvement du ventre et de la poitrine")],
        "Réponse : a", 112))

    questions.append(q(541, "Réanimation personne asphyxiée", "Comment réanimer une personne asphyxiée ?",
        [("a", "en desserrant les vêtements de la victime"),
         ("b", "en pratiquant la respiration bouche à bouche après désobstruction des voies aériennes supérieures"),
         ("c", "en pratiquant la respiration bouche à nez sans désobstruction des voies aériennes supérieures"),
         ("d", "en mettant le blessé dans la Position Latérale de Sécurité (P.L.S.)"),
         ("e", "en lui donnant à boire")],
        "Réponses : a-b-d", 112, tags=["multi-reponses"]))

    questions.append(q(542, "Signes de l'entorse", "Quels sont les signes qui apparaissent en cas d’entorse ?",
        [("a", "douleur, gonflement, mouvements impossibles"),
         ("b", "Douleur, saignement, mouvements possibles"),
         ("c", "Douleur, gonflement, mouvements possibles")],
        "Réponse : c", 113, exp="Entorse = mouvements possibles (douloureux). Luxation/fracture = mouvements impossibles."))

    questions.append(q(543, "Définition hémorragie", "L’hémorragie est :",
        [("a", "La sortie du sang hors des vaisseaux sanguins"),
         ("b", "Une mauvaise circulation du sang"),
         ("c", "Le passage du sang dans le cœur")],
        "Réponse : a", 113))

    questions.append(q(544, "Hémorragie externe", "Il y a hémorragie externe lorsque le sang s’écoule :",
        [("a", "D’un orifice naturel"),
         ("b", "A l’extérieur du corps par une plaie"),
         ("c", "D’un orifice naturel ou à l’extérieur du corps par une plaie"),
         ("d", "A l’intérieur du corps")],
        "Réponse a-b-c", 113, tags=["multi-reponses"]))

    questions.append(q(545, "Hémorragie interne", "Il y a hémorragie interne lorsque le sang s’écoule :",
        [("a", "A l’extérieur du corps"),
         ("b", "A l’intérieur du corps hors des vaisseaux"),
         ("c", "A l’intérieur des vaisseaux")],
        "Réponse : b", 113))

    questions.append(q(546, "Brûlure vêtements en flammes", "En cas de brûlure grave par le feu, vêtements enflammés :",
        [("a", "Je déshabille la victime avant de l’évacuer à l’hôpital"),
         ("b", "J’empêche la victime de courir, je l’enroule dans une couverture et je l’évacue à l’hôpital"),
         ("c", "Je l’arrose de l’extincteur")],
        "Réponse b", 113, exp="Empêcher de courir (l'air attise les flammes), étouffer le feu avec une couverture/manteau."))

    questions.append(q(547, "Brûlure liquide bouillant", "En cas de brûlure par liquide bouillant ou par vapeur :",
        [("a", "Je déshabille la victime, je la douche le plus vite possible et je le fais évacuer vers un centre médical"),
         ("b", "Je l’enroule de couverture"),
         ("c", "Je l’évacue sans rien faire")],
        "Réponse a", 113))

    questions.append(q(548, "Projection acide de batterie dans l'œil", "En cas de projection de l’acide de la batterie dans l’œil d’un individu :",
        [("a", "je rince l’œil pendant au moins 10 minutes avec de l’eau courante et je mets une compresse, puis je l’évacue chez l’ophtalmologiste"),
         ("b", "j’instille de l’huile à frein sur l’œil"),
         ("c", "je bande l’œil")],
        "Réponse a", 113, tags=["chiffre"], exp="Rinçage immédiat à grande eau tiède pendant au moins 10 minutes sans frotter."))

    questions.append(q(549, "Dégagement d'urgence blessé", "Pour effectuer le dégagement d’urgence d’un blessé de quelques mètres :",
        [("a", "je le roule par terre"),
         ("b", "je le mets au dos"),
         ("c", "je soulève légèrement sa tête, un aide le tire par les pieds en le glissant sur le sol dans l’axe du corps")],
        "Réponse c", 114))

    questions.append(q(550, "Utilité de la PLS", "Quel est l’utilité de la position latérale de sécurité (PLS) ?",
        [("a", "Elle permet d’être couché sur le dos afin de bien respirer"),
         ("b", "Elle permet de rester assis pour empêcher le choc"),
         ("c", "Elle permet d’être couché à plat ventre"),
         ("d", "Elle permet à la victime d’être couché sur le côté, d’éviter la chute de la langue en arrière, l’encombrement des voies respiratoires par le sang, le vomissement et la mucosité")],
        "Réponse d", 114, exp="La PLS maintient les voies aériennes libres et évite l'étouffement par la langue ou les vomissements chez la victime inconsciente qui respire."))

    questions.append(q(551, "But du massage cardiaque", "Quel est le but du massage cardiaque ?",
        [("a", "Il permet au malade d’éviter le vertige"),
         ("b", "Il permet au malade de bien respirer"),
         ("c", "Il permet de réanimer une victime qui présente un arrêt circulatoire"),
         ("d", "il permet d’arrêter une hémorragie interne")],
        "Réponse : c", 114))

    questions.append(q(552, "Définition de la luxation", "Quand dit-on qu’il y a luxation ?",
        [("a", "Lorsqu’il y a étirement ou déchirure des ligaments"),
         ("b", "Lorsqu’il y a cassure d’un os et qu’il est en contact avec l’extérieur"),
         ("c", "Lorsque les ligaments sont déchirés, l’articulation déboitée")],
        "Réponse c", 114))

    questions.append(q(553, "Luxation vs entorse", "Quand dit-on qu’il y a luxation ?",
        [("a", "Lorsqu’il y a cassure d’un os sans saignement"),
         ("b", "Lorsque les ligaments sont déchirés, l’articulation déboitée"),
         ("c", "Lorsqu’il y a étirement ou déchirure des ligaments, les surfaces articulaires restent en contact")],
        "Réponse c", 114, tags=["ambiguite"]))

    questions.append(q(554, "Ramassage d'un blessé", "Pour le ramassage d’un blessé :",
        [("a", "Je dois remuer le blessé et le mettre débout"),
         ("b", "Je dois mettre le blessé au dos"),
         ("c", "Je dois le remuer le moins possible et respecter le bloc tête-cou-tronc")],
        "Réponse c", 114, exp="Maintenir impérativement l'axe tête-cou-tronc pour prévenir les lésions irréversibles de la moelle épinière."))

    questions.append(q(555, "Définition fracture", "On appelle fracture :",
        [("a", "La rupture brutale d’un os"),
         ("b", "La douleur d’un os"),
         ("c", "La sortie de l’os dans l’organisme")],
        "Réponse a", 114))

    questions.append(q(556, "Fracture fermée", "Il y a fracture fermée lorsque :",
        [("a", "Un os a un abcès"),
         ("b", "Un os est cassé et prend contact avec l’extérieur"),
         ("c", "Un os est cassé et ne prend pas contact avec l’extérieur")],
        "Réponse c", 115))

    questions.append(q(557, "Fracture ouverte", "Il y a fracture ouverte lorsque :",
        [("a", "Un os est courbé"),
         ("b", "Un os est cassé et ne prend pas contact avec l’extérieur"),
         ("c", "Un os est cassé et prend contact avec l’extérieur")],
        "Réponse c", 115))

    questions.append(q(558, "Signes de fatigue au volant", "Quels peuvent être les signes révélateurs de fatigue au volant ?",
        [("a", "Maux de dents – picotements gastrique –lourdeurs des pieds et des bras"),
         ("b", "lourdeur de tête – picotement des yeux – lourdeurs des paupières"),
         ("c", "Maux d’estomac – picotements de la peau – campes aux jambes"),
         ("d", "Faim – soif – vertige")],
        "Réponse b", 115))

    questions.append(q(559, "Obligation de secours", "Secourir un accident de la route est-il obligatoire ?",
        [("a", "Oui"), ("b", "Non"), ("c", "Facultatif")],
        "Réponse a", 115, exp="Le refus d'assistance à personne en danger est un délit lourdement sanctionné."))

    questions.append(q(560, "Effet de l'alcool sur le conducteur", "Quel effet l’alcool produit-il sur un conducteur ?",
        [("a", "Permet au conducteur de mieux voir"),
         ("b", "Permet au conducteur de respecter le code de la route"),
         ("c", "Réduit les facultés mentales et physiques du conducteur")],
        "Réponse c", 115))

    questions.append(q(561, "Bon comportement lieu d'accident", "Quel est le bon comportement d’un usager sur un lieu d’accident :",
        [("a", "alerter – secourir – et protéger"),
         ("b", "secourir – protéger – et alerter"),
         ("c", "secourir – alerter – et protéger"),
         ("d", "rien de tout ce qui précède")],
        "Réponse d", 115, tags=["piege"], exp="Piège classique : la bonne séquence est PROTÉGER d'abord, ALERTER ensuite, SECOURIR enfin (P.A.S.)."))

    questions.append(q(562, "Infraction insertion autoroute", "Sur autoroute, je commets une infraction en m’insérant sur l’axe principal :",
        [("a", "si je fais ralentir un véhicule"),
         ("b", "si j’oblige un usager à changer de voie"),
         ("c", "si je cède le passage à un usager circulant sur l’axe principal")],
        "Réponse: a, b", 115, tags=["multi-reponses"]))

    questions.append(q(563, "Appel secours autoroute", "En cas d’accident sur autoroute je peux prévenir les secours :",
        [("a", "à l’aide des bornes d’appel d’urgence placées tous les 2km"),
         ("b", "à l’aide de mon téléphone portable en composant le numéro d’un service secours"),
         ("c", "avec l’aide d’un autre usager")],
        "Réponse : a, b", 116, tags=["multi-reponses"]))

    questions.append(q(564, "Ordre installation poste de conduite", "Pour m’installer à mon poste de conduite, dans l’ordre :",
        [("a", "je mets la ceinture, je règle les rétroviseurs puis le siège"),
         ("b", "je règle le siège puis les rétroviseurs et je mets la ceinture"),
         ("c", "je règle les rétroviseurs puis le siège et je mets la ceinture")],
        "Réponse: b", 116, exp="Ordre d'installation : 1. Réglage du siège et du dossier, 2. Réglage des rétroviseurs, 3. Bouclage de la ceinture."))

    questions.append(q(565, "Vitesse permis 18 mois", "Titulaire du permis de conduire depuis 18mois, je peux rouler à :",
        [("a", "80km/h"), ("b", "70km/h"), ("c", "60km/h"), ("d", "100km/h")],
        "Réponse: a, b, c", 116, tags=["multi-reponses", "chiffre"]))

    questions.append(q(566, "Définition taux d'alcoolémie", "Le taux d’alcoolémie est :",
        [("a", "le degré de l’état d’ivresse"),
         ("b", "la quantité de bière dans le sang"),
         ("c", "la quantité d’alcool contenue dans un litre de sang"),
         ("d", "la quantité de vin contenu dans le sang")],
        "Réponse c", 116, exp="L'alcoolémie s'exprime en grammes d'alcool pur par litre de sang (g/l)."))

    questions.append(q(567, "Dépistage de l'alcoolémie", "Le dépistage de l’alcoolémie se fait par :",
        [("a", "l’air expiré par la bouche"),
         ("b", "l’alcotest"),
         ("c", "la prise de sang"),
         ("d", "l’éthylotest")],
        "Réponse b, d", 116, tags=["multi-reponses"], exp="Le dépistage préventif se fait par alcootest / éthylotest. La mesure exacte (dosage) par éthylomètre ou prise de sang."))

    questions.append(q(568, "Dosage de l'alcoolémie", "Le dosage de l’alcoolémie se fait par :",
        [("a", "l’alcooltest"),
         ("b", "analyse de sang"),
         ("c", "éthylomètre"),
         ("d", "éthylotest")],
        "Réponse b, c", 116, tags=["multi-reponses"]))

    questions.append(q(569, "Position des mains au volant", "Quelle est la bonne position des mains au volant d’un conducteur en marche normale, en considérant le volant comme le cadran d’une montre :",
        [("a", "11h 05mn"),
         ("b", "9h 15mn"),
         ("c", "7h 25mn")],
        "Réponse b", 116, exp="La position recommandée est 9h15 (ou 10h10), assurant un contrôle optimal de la direction et de l'airbag."))

    questions.append(q(570, "Téléphone au volant", "Au volant de mon véhicule je peux :",
        [("a", "recevoir un appel"),
         ("b", "appeler un ami"),
         ("c", "communiquer si mon portable est équipé d’un écouteur"),
         ("d", "rien de tout ce qui précède")],
        "Réponse d", 117, exp="Il est strictement interdit de téléphoner en conduisant."))

    questions.append(q(571, "Distractions au volant", "Au volant de mon véhicule je peux :",
        [("a", "manger"),
         ("b", "boire"),
         ("c", "fumer"),
         ("d", "écouter la radio")],
        "Réponse d", 117, exp="Seul l'usage raisonné de la radio est admis. Manger, boire ou fumer détournent l'attention et occupent les mains."))

    questions.append(q(572, "Feux en agglomération éclairée", "Dans une agglomération éclairée je peux circuler :",
        [("a", "sans feux"),
         ("b", "en feux de position"),
         ("c", "en feux de croisement"),
         ("d", "en feux de route")],
        "Réponse b, c", 117, tags=["multi-reponses"]))

    questions.append(q(573, "Condamnation délit de fuite", "Je peux être condamné pour délit de fuite si je ne m’arrête pas après avoir :",
        [("a", "occasionné un accident matériel"),
         ("b", "occasionné un accident corporel"),
         ("c", "ignoré l’injonction d’un agent de force réglementant la circulation")],
        "Réponse: a, b", 117, tags=["multi-reponses"], exp="Ne pas s'arrêter après un accident corporel OU matériel dans lequel on est impliqué constitue le délit de fuite."))

    questions.append(q(574, "Dégradation de la vigilance", "La vigilance au volant est dégradé si :",
        [("a", "Je téléphone"),
         ("b", "Je mange un sandwich"),
         ("c", "Je bavarde avec les passagers"),
         ("d", "Je me concentre à la conduite")],
        "Réponse a, b, c", 117, tags=["multi-reponses"]))

    questions.append(q(575, "Consommation de drogue", "La consommation de la drogue peut provoquer :",
        [("a", "des effets d’ivresse"),
         ("b", "une diminution du champ visuel"),
         ("c", "l’euphorie")],
        "Réponse a, b, c", 117, tags=["multi-reponses"]))

    questions.append(q(576, "Obligations conducteur accident", "Que doit faire un conducteur impliqué dans un accident de circulation ?",
        [("a", "dégager la chaussée après marquage pour ne pas gêner la circulation"),
         ("b", "avertir son assureur (compagnie d’assurance)"),
         ("c", "communiquer son identité (adresse) à toute personne impliquée dans l’accident"),
         ("d", "rester calme et courtois")],
        "Réponse: a, b, c, d", 117, tags=["multi-reponses"]))

    questions.append(q(577, "Comportement véhicule prioritaire", "Quel doit être le comportement d’un conducteur vis-à-vis d’un véhicule prioritaire en mission ?",
        [("a", "céder le passage aux intersections"),
         ("b", "céder le passage aux intersections munies de feux tricolores"),
         ("c", "faciliter leurs manœuvres, de croisement"),
         ("d", "attendre l’ordre d’un agent règlementant la circulation")],
        "Réponse a, b, c", 118, tags=["multi-reponses"]))

    questions.append(q(578, "Signes évidents de fatigue", "Quels sont les signes évidents de la fatigue ?",
        [("a", "bâillement"),
         ("b", "picotement des yeux"),
         ("c", "somnolence")],
        "Réponse : a-b-c", 118, tags=["multi-reponses"]))

    questions.append(q(579, "Effets de la fatigue", "Quels sont les effets de la fatigue ?",
        [("a", "réaction tardive"),
         ("b", "mauvaise analyse"),
         ("c", "mauvaise appréciation des vitesses"),
         ("d", "l’impatience ou anxiété grandissante")],
        "Réponse a, b, c", 118, tags=["multi-reponses"]))

    questions.append(q(580, "Limiter la fatigue", "Comment limiter la fatigue ?",
        [("a", "conduire sur une longue durée sans repos"),
         ("b", "pendant le trajet se reposer régulièrement"),
         ("c", "pratiquer l’alternance au volant")],
        "Réponse b, c", 118, tags=["multi-reponses"]))

    questions.append(q(581, "Déplacement sûr", "Quels sont les conditions nécessaires pour un déplacement sûr ?",
        [("a", "être en forme pour conduire"),
         ("b", "avoir un véhicule en bon état de fonctionnement"),
         ("c", "anticiper les situations critiques"),
         ("d", "être courtois avec les autres usagers")],
        "Réponse : a-b-c-d", 118, tags=["multi-reponses"]))

    questions.append(q(582, "Conduite économique", "Quel comportement adopter pour une conduite économique ?",
        [("a", "choisir un bon style de conduite"),
         ("b", "bien régler son moteur"),
         ("c", "bon gonflage des pneus"),
         ("d", "aérodynamisme bien adapté")],
        "Réponse : a-b-c-d", 118, tags=["multi-reponses"]))

    questions.append(q(583, "Conducteur impliqué accident", "Quel doit être le comportement d’un conducteur impliqué dans un accident de circulation ?",
        [("a", "s’arrêter après marquage"),
         ("b", "dégager la chaussée pour ne pas gêner la circulation"),
         ("c", "avertir sa compagnie d’assurance"),
         ("d", "communiquer son identité et son adresse à toute personne impliquée dans l’accident"),
         ("e", "conduire le véhicule au poste de police le plus proche")],
        "Réponse a, b, c, d", 119, tags=["multi-reponses"]))

    questions.append(q(584, "Effets de l'alcool sur la vision", "L’alcool :",
        [("a", "diminue le champ de vision"),
         ("b", "réduit la vigilance"),
         ("c", "allonge le temps de réaction"),
         ("d", "Augmente le champ de vision")],
        "Réponse a, b", 119, tags=["multi-reponses"]))

    questions.append(q(585, "Risque de verglas", "J’ai plus de risque de rencontrer du verglas si je circule :",
        [("a", "en lisière d’une forêt"),
         ("b", "le long d’un cours d’eau"),
         ("c", "à allure soutenue")],
        "Réponse a, b", 119, tags=["multi-reponses"]))

    questions.append(q(586, "Allumage des feux", "Je dois allumer mes feux :",
        [("a", "Dès que le jour tombe"),
         ("b", "Dès qu’il fait nuit"),
         ("c", "Dès qu’il commence par pleuvoir")],
        "Réponse: a, b", 119, tags=["multi-reponses"]))

    questions.append(q(587, "Stationnement de nuit rue sombre", "Pour stationner de nuit dans une rue non éclairée en agglomération, j’allume :",
        [("a", "Mes feux de croisement"),
         ("b", "Mes feux de position"),
         ("c", "Aucun feu pour ne pas décharger ma batterie")],
        "Réponse : b", 119, exp="En stationnement de nuit sur chaussée non éclairée, laisser allumés les feux de position pour être visible."))

    questions.append(q(588, "Alcool altérations", "L’absorption d’alcool entraine une réduction :",
        [("a", "Du champ visuel"),
         ("b", "Des capacités d’analyse"),
         ("c", "Du temps de réaction"),
         ("d", "Des habiletés motrices")],
        "Réponse: a, b, c, d", 119, tags=["multi-reponses"]))

    questions.append(q(589, "Seuil d'effets de l'alcool", "Les effets de l’alcool apparaissent à partir de :",
        [("a", "0,3g/l de sang"),
         ("b", "0,5g/l de sang"),
         ("c", "1,2g/l de sang")],
        "Réponse : b", 119, tags=["chiffre"], exp="Le taux limite légal d'alcoolémie est fixé à 0,5 g d'alcool par litre de sang."))

    questions.append(q(590, "Risque accident mortel alcoolémie 0,5g/l", "Conduire avec une alcoolémie de 0,5g/l de sang multiplie le risque d’avoir un accident mortel :",
        [("a", "par dix"),
         ("b", "par cinq"),
         ("c", "par deux")],
        "Réponse : c", 120, tags=["chiffre"], exp="Dès 0,5 g/l, le risque d'accident mortel est multiplié par 2."))

    questions.append(q(591, "Élimination de l'alcoolémie", "Pour faire redescendre à 0,5g/l, un taux d’alcoolémie de 0,8g/l de sang, il faut en moyenne :",
        [("a", "1 heure"),
         ("b", "2 heures"),
         ("c", "3 heures")],
        "Réponse : b", 120, tags=["chiffre"], exp="Le corps élimine en moyenne 0,10 à 0,15 g/l par heure ; il faut environ 2 heures pour perdre 0,3 g/l."))

    questions.append(q(592, "Alcool et médicaments interaction", "L’association alcool et médicaments peut augmenter :",
        [("a", "Le taux d’alcoolémie"),
         ("b", "Les effets de l’alcool"),
         ("c", "Le temps de réaction")],
        "Réponse : b, c", 120, tags=["multi-reponses"]))

    questions.append(q(593, "Fréquence des pauses sur long trajet", "Lors d’un long trajet, il est conseillé de faire une pause d’au moins 10minutes :",
        [("a", "Toutes les heures"),
         ("b", "Toutes les deux heures"),
         ("c", "Toutes les 4 heures")],
        "Réponse : b", 120, tags=["chiffre"], exp="Règle d'or de la sécurité routière : arrêt obligatoire toutes les 2 heures au moins 10 à 15 minutes."))

    questions.append(q(594, "Pic d'alcoolémie", "L’alcoolémie atteint son maximum :",
        [("a", "Immédiatement après absorption"),
         ("b", "Entre demi-heure et une heure après absorption"),
         ("c", "Après deux heures")],
        "Réponse : b", 120, tags=["chiffre"]))

    questions.append(q(595, "Mesure exacte du taux d'alcoolémie", "La mesure exacte du taux d’alcoolémie est effectuée si :",
        [("a", "Le dépistage est positif"),
         ("b", "Le conducteur refuse le dépistage"),
         ("c", "Le dépistage est négatif")],
        "Réponse : a, b", 120, tags=["multi-reponses"]))

    questions.append(q(596, "Contrôle d'alcoolémie systématique", "Le contrôle d’alcoolémie est systématique :",
        [("a", "Si l’on est impliqué dans un accident corporel"),
         ("b", "Lors des contrôles routiers"),
         ("c", "Lors d’un accident")],
        "Réponse : a", 120))

    questions.append(q(597, "Conditions augmentant la fatigue", "Les conditions qui augmentent la fatigue sont :",
        [("a", "Le manque de sommeil"),
         ("b", "La visibilité réduite"),
         ("c", "Une circulation fluide"),
         ("d", "La conduite de nuit")],
        "Réponse : a-b", 121, tags=["multi-reponses"]))

    questions.append(q(598, "Retarder l'apparition de la fatigue", "Pour retarder l’apparition de la fatigue, il faut :",
        [("a", "Boire beaucoup de café"),
         ("b", "Etre bien installé au volant"),
         ("c", "Prendre la route après un bon repos")],
        "Réponse : b-c", 121, tags=["multi-reponses"]))

    questions.append(q(599, "Conduite en cas de fatigue", "En cas de fatigue, il faut :",
        [("a", "Marquer une pause"),
         ("b", "Rouler plus lentement"),
         ("c", "Rouler plus vite pour maintenir la vigilance"),
         ("d", "Passer le volant à un passager")],
        "Réponse : a", 121))

    questions.append(q(600, "Risque d'incendie après accident", "Lors d’un accident, s’il y a risque d’incendie :",
        [("a", "Je débranche la batterie des véhicules"),
         ("b", "Je maintien le contact des véhicules"),
         ("c", "Je coupe le contact des véhicules")],
        "Réponse : a-c", 121, tags=["multi-reponses"], exp="Couper le contact et débrancher la borne de batterie supprime tout risque d'étincelle avec les fuites d'essence."))

    questions.append(q(601, "Signaler un accident la nuit", "De nuit pour signaler un accident :",
        [("a", "J’utilise les feux de mon véhicule"),
         ("b", "Je fais des signes avec une lampe de poche"),
         ("c", "Je place mes triangles de pré signalisation")],
        "Réponse : a-b-c", 121, tags=["multi-reponses"]))

    questions.append(q(602, "Règlement à l'amiable", "Lors d’un accident le règlement à l’amiable est :",
        [("a", "Obligatoire"),
         ("b", "Facultatif"),
         ("c", "Recommandé")],
        "Réponse : b-c", 121, tags=["multi-reponses"]))

    questions.append(q(603, "Assurance minimum obligatoire", "L’assurance minimum obligatoire :",
        [("a", "couvre les dommages occasionnés aux autres"),
         ("b", "couvre les dégâts occasionnés aux véhicules seulement"),
         ("c", "est aussi appelée assurance au tiers")],
        "Réponse : a-c", 121, tags=["multi-reponses"], exp="L'assurance au tiers couvre la responsabilité civile : tous les dommages causés aux tiers (autres personnes et biens)."))

    questions.append(q(604, "Témoin d'accident devoirs", "Si je suis témoin d’un accident, je dois :",
        [("a", "exposer ce que j’ai vu aux forces de l’ordre"),
         ("b", "remplir le contrat amiable"),
         ("c", "déterminer les responsabilités"),
         ("d", "laisser mes coordonnées pour un témoignage ultérieur")],
        "Réponse : a-d", 122, tags=["multi-reponses"]))

    questions.append(q(605, "Premiers gestes aux blessés", "En présence de blessés après un accident il faut :",
        [("a", "les couvrir"),
         ("b", "pratiquer les gestes qui sauvent"),
         ("c", "les faire boire pour éviter qu’ils ne se déshydratent"),
         ("d", "les transporter sur l’accotement")],
        "Réponse : a-b", 122, tags=["multi-reponses"]))

    questions.append(q(606, "Message d'alerte des secours", "Lors de l’alerte des secours, j’indique :",
        [("a", "le lieu précis de l’accident"),
         ("b", "le numéro d’immatriculation des véhicules impliqués"),
         ("c", "le nombre et le type de véhicules impliqués"),
         ("d", "le nombre et l’état des blessés")],
        "Réponse : a-c-d", 122, tags=["multi-reponses"]))

    questions.append(q(607, "Protéger les lieux de l'accident", "Protéger les lieux d’un accident, c’est :",
        [("a", "baliser les lieux pour éviter un autre accident"),
         ("b", "dégager complètement la chaussée"),
         ("c", "barrer complètement la voie aux autres véhicules")],
        "Réponse : a", 122))

    questions.append(q(608, "Position d'attente blessé déplacé", "Après avoir déplacé un blessé, je le mets allongé sur :",
        [("a", "le coté"),
         ("b", "le dos"),
         ("c", "le ventre")],
        "Réponse : a", 122, exp="Allongé sur le côté (PLS) pour préserver sa respiration."))

    questions.append(q(609, "Déplacement véhicule immobilisé", "Si mon véhicule est immobilisé dangereusement sur la chaussée, je le déplace de préférence :",
        [("a", "en le poussant"),
         ("b", "en enclenchant la 1ère ou la marche en arrière et en actionnant le démarreur"),
         ("c", "en faisant appel à des secours")],
        "Réponse : b", 122))

    questions.append(q(610, "Boîte d'ampoules de rechange", "La présence à bord d’une boîte d’ampoule et de fusible de recharge est :",
        [("a", "obligatoire"),
         ("b", "recommandée"),
         ("c", "inutile")],
        "Réponse : b", 122))

    questions.append(q(611, "Réglage des faisceaux lumineux", "Le réglage de la hauteur des faisceaux lumineux du véhicule :",
        [("a", "dépend de la charge du véhicule"),
         ("b", "nécessite toujours l’intervention d’un spécialiste"),
         ("c", "est effectué une fois pour toutes lors de la mise en circulation")],
        "Réponse : a", 123))

    questions.append(q(612, "Liquide de lave-glace", "Pour remplir le réservoir de mon lave glace, j’utilise de préférence :",
        [("a", "de l’eau uniquement"),
         ("b", "un produit détergent spécial"),
         ("c", "un détergent ménager")],
        "Réponse : b", 123))

    questions.append(q(613, "Vérification équilibrage des roues", "Je dois faire vérifier l’équilibrage des roues de mon véhicule :",
        [("a", "après un choc violent contre un trottoir"),
         ("b", "en cas d’usure anormale de mes pneus"),
         ("c", "je ressens des vibrations au niveau du volant"),
         ("d", "si mon véhicule se déporte au freinage")],
        "Réponse : a-c", 123, tags=["multi-reponses"]))

    questions.append(q(614, "Équipements et batterie", "Parmi ces équipements, ceux qui déchargent le plus la batterie sont :",
        [("a", "l’autoradio"),
         ("b", "les feux"),
         ("c", "le système dégivrage de la lunette arrière")],
        "Réponse : b-c", 123, tags=["multi-reponses"]))

    questions.append(q(615, "Économiser le carburant", "Pour économiser du carburant, il faut :",
        [("a", "faire entretenir régulièrement son véhicule"),
         ("b", "éviter de rouler avec une galerie vide sur le toit"),
         ("c", "rouler le plus souvent possible en sous régime"),
         ("d", "avoir les pneus bien gonflés")],
        "Réponse : a-b-d", 123, tags=["multi-reponses"]))

    questions.append(q(616, "Vérification du parallélisme", "Je dois faire vérifier le parallélisme des roues de mon véhicule :",
        [("a", "après un choc violent"),
         ("b", "en cas d’usure de mes pneus"),
         ("c", "si je ressens des vibrations au niveau du volant"),
         ("d", "si mon véhicule se déporte")],
        "Réponse : a-b-d", 123, tags=["multi-reponses"]))

    questions.append(q(617, "Position de conduite conséquences", "L’installation au poste de conduite influence :",
        [("a", "la vision"),
         ("b", "le confort"),
         ("c", "la tenue de route"),
         ("d", "la manipulation des commandes")],
        "Réponse a, b, d", 123, tags=["multi-reponses"]))

    questions.append(q(618, "Regard dans les rétroviseurs", "Il est indispensable de regarder dans ses rétroviseurs avant de :",
        [("a", "modifier sa trajectoire"),
         ("b", "activer ses clignotants"),
         ("c", "modifier son allure")],
        "Réponse : a-b- c", 124, tags=["multi-reponses"]))

    questions.append(q(619, "Utilité des appels lumineux", "Les appels lumineux servent à signaler :",
        [("a", "une intention de dépasser"),
         ("b", "la présence de gendarmes"),
         ("c", "l’approche à une intersection la nuit")],
        "Réponse a, c", 124, tags=["multi-reponses"]))

    questions.append(q(620, "Usage du klaxon", "Je peux utiliser l’avertisseur sonore pour :",
        [("a", "avertir de ma présence un usager qui ne me regarde pas"),
         ("b", "signaler à un usager qu’il vient de commettre une faute"),
         ("c", "Passer lorsque j’ai la priorité")],
        "Réponse a", 124))

    questions.append(q(621, "Interdiction du klaxon", "L’usage de l’avertisseur sonore est interdit :",
        [("a", "la nuit, uniquement en agglomération"),
         ("b", "la nuit, en agglomération et hors agglomération"),
         ("c", "le jour en agglomération sauf danger immédiat")],
        "Réponse b, c", 124, tags=["multi-reponses"], exp="Klaxon interdit la nuit partout, et le jour en ville sauf danger immédiat."))

    questions.append(q(622, "Monter ou descendre du véhicule", "Avant de monter abord ou de descendre de mon véhicule je dois :",
        [("a", "m’assurer qu’il n’y aucun risque"),
         ("b", "contrôler que ma position ne gêne d’autres usagers"),
         ("c", "tenir compte les mouvements des autres usagers")],
        "Réponse b, c", 124, tags=["multi-reponses"]))

    questions.append(q(623, "Visibilité réduite", "Lorsque la visibilité est réduite :",
        [("a", "je ralentis pour pouvoir m’arrêter le cas échéant"),
         ("b", "je ne ralentis pas car cela n’améliore pas la visibilité")],
        "Réponse a", 124))

    questions.append(q(624, "Démarrage en côte frein à main", "Lors d’un départ en cote, il faut desserrer le frein à main :",
        [("a", "avant de commencer à embrayer"),
         ("b", "dès que l’on a trouvé le point de patinage"),
         ("c", "dès que l’on a fini d’embrayer")],
        "Réponse b", 124, exp="On relâche le frein à main pile au point de patinage quand la voiture tire vers l'avant, pour ne pas reculer."))

    questions.append(q(625, "Arrêt sans caler", "Lors d’un arrêt en circulation, pour éviter de caler le moteur il faut :",
        [("a", "débrayer dès le début du freinage"),
         ("b", "débrayer en fin de freinage seulement"),
         ("c", "débrayer avant de freiner")],
        "Réponse b", 124))

    questions.append(q(626, "Position des mains volant schéma", "Les mains sur le volant sont placées correctement sur le dessin :",
        [("a", "Dessin a"), ("b", "Dessin b (9h15)"), ("c", "Dessin c"), ("d", "Dessin d (10h10)")],
        "Réponse b, d", 125, img="Mains_volant", tags=["multi-reponses"]))

    questions.append(q(627, "Rôle de la rétrogradation bis", "La rétrogradation permet :",
        [("a", "de ralentir le véhicule dans une descente"),
         ("b", "de répartir après un ralentissement"),
         ("c", "d’arrêter le véhicule en circulation")],
        "Réponse b", 125))

    questions.append(q(628, "Intervention frein moteur", "Le frein moteur intervient dès qu’on :",
        [("a", "lâche l’accélérateur"),
         ("b", "appuie sur la pédale de frein")],
        "Réponse a", 125, exp="Dès qu'on lève le pied de l'accélérateur, la compression du moteur ralentit naturellement le véhicule."))

    questions.append(q(629, "Visibilité en marche arrière", "A bord d’un véhicule de tourisme, pour effectuer une marche arrière, j’aurai une meilleure vision :",
        [("a", "si je me retourne bien"),
         ("b", "si je me retourne peu"),
         ("c", "si j’utilise mes 3 rétroviseurs")],
        "Réponse a", 125))

    questions.append(q(630, "Lieux de demi-tour dangereux", "Il est dangereux d’effectuer un demi-tour :",
        [("a", "dans un virage"),
         ("b", "lorsque la circulation est dense et rapide"),
         ("c", "dans une rue sans issue")],
        "Réponse : a, b", 125, tags=["multi-reponses"]))

    questions.append(q(631, "Facteurs de fatigue accrue", "La fatigue et la perte de vigilance sont accrues par :",
        [("a", "une vitesse modérée"),
         ("b", "la conduite de nuit"),
         ("c", "une dette de sommeil"),
         ("d", "la prise de caféine")],
        "Réponse : b-c", 125, tags=["multi-reponses"]))

    questions.append(q(632, "Téléphone au feu rouge", "Pendant l’arrêt au feu rouge :",
        [("a", "je peux rapidement prendre un appel téléphonique"),
         ("b", "je peux rapidement passer un appel téléphonique avant le feu vert"),
         ("c", "je ne dois toucher au téléphone")],
        "Réponse : c", 126, exp="Même à l'arrêt temporaire dans la circulation (au feu ou dans un bouchon), l'usage du téléphone reste strictement interdit."))

    questions.append(q(633, "Kit oreillette et urgence", "Au volant de mon véhicule, je peux utiliser mon téléphone portable :",
        [("a", "lorsque je me retrouve seul sur la chaussée"),
         ("b", "lorsque je ne suis pas sur une route à grande circulation"),
         ("c", "lorsque je suis équipé d’un kit oreillette en cas d’urgence"),
         ("d", "lorsqu’il y a urgence")],
        "Réponse : c", 126))

    questions.append(q(634, "Téléphone qui sonne au volant", "Au volant de mon véhicule, mon téléphone portable sonne :",
        [("a", "j’arrête mon véhicule convenablement avant de toucher au téléphone"),
         ("b", "je ne dois pas toucher au téléphone"),
         ("c", "je prends le téléphone pour vérifier mon correspondant")],
        "Réponse : b-c", 126, tags=["ambiguite", "multi-reponses"]))

    questions.append(q(635, "Délit de fuite", "Je commets un délit de fuite si je ne m’arrête pas :",
        [("a", "Lorsque je suis témoin d’un accident"),
         ("b", "Lorsqu’un agent de sécurité me fait signe de m’arrêter"),
         ("c", "Lorsque je suis impliqué dans un accident")],
        "Réponse c", 126))

    questions.append(q(636, "Causes d'abstention de conduire", "Je dois m’abstenir de conduire :",
        [("a", "Si je prends un verre de jus de raisin"),
         ("b", "Si je suis sous l’effet de boissons alcoolisées ou de certains médicaments"),
         ("c", "Si je suis fatigué"),
         ("d", "Si je me sens nerveux ou surexcité"),
         ("e", "Après un bon sommeil")],
        "Réponse b-c-d", 126, tags=["multi-reponses"]))

    questions.append(q(637, "Alcool et temps de réaction", "L’absorption d’alcool :",
        [("a", "Permet de bien conduire"),
         ("b", "Augmente le temps de réaction"),
         ("c", "Permet de bien apprécier les distances"),
         ("d", "Augmente le champ visuel")],
        "Réponse b", 126, exp="L'alcool rallonge le temps de réaction (le cerveau met plus de temps à réagir) et rétrécit le champ visuel."))

    questions.append(q(638, "Passer au feu rouge", "On peut passer le feu rouge allumé à une intersection munie de feux tricolores :",
        [("a", "Quand on s’y retrouve seul"),
         ("b", "Quand on s’y retrouve seul tard dans la nuit"),
         ("c", "A aucun moment"),
         ("d", "Si je veux tourner à droite")],
        "Réponse c", 126))

    questions.append(q(639, "Alcool avant de conduire", "Avant de me mettre au volant :",
        [("a", "Je peux prendre de l’alcool"),
         ("b", "Je peux prendre de l’alcool sans me soûler"),
         ("c", "Je dois m’abstenir de prendre de l’alcool")],
        "Réponse c", 127))

    questions.append(q(640, "Possession du permis en circulation", "Je suis titulaire du permis de conduire :",
        [("a", "Je peux conduire sans l’avoir sur moi"),
         ("b", "Je conduis toujours avec mon permis de conduire"),
         ("c", "Je peux conduire avec une photocopie légalisée de mon permis de conduire")],
        "Réponse b", 127, exp="Il faut toujours avoir sur soi le titre original physique du permis de conduire."))

    questions.append(q(641, "Retrait de permis et CNSR", "En cas de retrait de votre permis de conduire suite à une infraction ou à un accident, je dois :",
        [("a", "Me présenter à la gendarmerie pour reprendre le permis de conduire"),
         ("b", "Me présenter au Centre National de Sécurité Routière pour les dispositions de reprise de mon permis de conduire"),
         ("c", "Me présenter au maire de la commune où l’accident a eu lieu pour le retrait de mon permis de conduire")],
        "Réponse b", 127, exp="Au Bénin, la gestion des dossiers de retrait et de restitution du permis relève du CNSR."))

    questions.append(q(642, "Rôle Commission Nationale Retrait", "La Commission Nationale de Retrait de Permis de Conduire est chargée :",
        [("a", "D’auditionner le(s) mis(es) en cause, de décider du retrait partiel ou définitif du Permis de conduire et de sensibiliser"),
         ("b", "D’écouter simplement les conducteurs de véhicules impliqués dans les accidents"),
         ("c", "De décider du payement des dommages causés par l’accident survenu"),
         ("d", "De l’emprisonnement du conducteur impliqué dans un accident mortel")],
        "Réponse a", 127))

    questions.append(q(643, "Interdiction de conduire après retrait", "Après le retrait de mon permis de conduire suite à un accident, je peux :",
        [("a", "Procéder au remplacement de mon permis de conduire"),
         ("b", "Demander le duplicata du permis de conduire"),
         ("c", "Continuer à conduire mon véhicule avec un certificat de perte"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 127, exp="Pendant la période de retrait ou suspension, toute conduite d'un véhicule à moteur est formellement interdite."))

    questions.append(q(644, "Organisation commission spéciale retrait", "Les travaux de la Commission Spéciale de Retrait de permis de conduire sont organisés par :",
        [("a", "La Direction Générale des Transports Terrestres"),
         ("b", "La Direction Générale des Travaux Publics"),
         ("c", "La Gendarmerie"),
         ("d", "Le Centre National de Sécurité Routière")],
        "Réponse d", 127))

    questions.append(q(645, "Transmission du permis retiré", "L’original du permis de conduire retiré par les Forces de Sécurité Publique suite à un accident est transmis :",
        [("a", "Au parquet"),
         ("b", "Au Centre National de Sécurité Routière"),
         ("c", "La Direction Générale des Transports Terrestres")],
        "Réponse b", 128))

    return questions

if __name__ == '__main__':
    qs = get_chapitre6_questions()
    print(f"Chapitre 6 loaded: {len(qs)} questions")
