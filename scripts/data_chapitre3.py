# Chapter 3: Règles de priorité, dépassement, croisement (Questions 206 to 359)
# Extracted from DGTT 2011 pages 43 to 83

def get_chapitre3_questions():
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
            "chapitre": 3,
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

    questions.append(q(206, "Véhicules prioritaires", "Les véhicules prioritaires sont :",
        [("a", "Police – Gendarmerie – corbillards en mission"),
         ("b", "SAMU – SMUR-Sapeur-pompier – Gendarmerie en mission"),
         ("c", "SAMU – corbillard – Police")],
        "Réponse b", 43, exp="Les 4 catégories prioritaires : Police, Gendarmerie, Sapeurs-Pompiers, SAMU/SMUR en mission d'urgence."))

    questions.append(q(207, "Feux vs Agent", "Les feux tricolores fonctionnent, cependant l’agent de sécurité règlemente la circulation :",
        [("a", "Je passe au feu vert"),
         ("b", "Je ne passe que si je suis autorisé par l’agent de sécurité"),
         ("c", "Je passe sans tenir compte ni du feu ni de l’agent de sécurité")],
        "Réponse b", 43, exp="Les injonctions de l'agent de police ou de gendarmerie annulent toutes les autres signalisations."))

    questions.append(q(208, "Panneau vs Feux", "A une intersection munie à la fois de panneau et de feu tricolore fonctionnant normalement :",
        [("a", "Je me conforme à la fois au panneau et aux feux"),
         ("b", "Je ne me conforme ni à l’un ni à l’autre"),
         ("c", "Je me conforme uniquement aux feux")],
        "Réponse c", 43))

    questions.append(q(209, "Grandes règles de priorité", "Quelles sont les grandes règles de priorité ?",
        [("a", "La règle de courtoisie et le respect des agents de sécurité"),
         ("b", "Le respect des feux et la règle de priorité à droite"),
         ("c", "La priorité à droite, la priorité de passage et la perte de priorité")],
        "Réponse c", 43, exp="Le code béninois classe la priorité selon 3 régimes : la priorité à droite, la priorité de passage et la perte de priorité."))

    questions.append(q(210, "Priorité à droite définition", "La priorité à droite consiste à :",
        [("a", "Passer quand ma droite est libre"),
         ("b", "Passer quand ma gauche est libre"),
         ("c", "Serrer ma droite et tourner à droite")],
        "Réponse a", 43))

    questions.append(q(211, "Intersection sans signalisation", "Que faire à une intersection sans signalisation ?",
        [("a", "Céder le passage à droite"),
         ("b", "Céder le passage à gauche"),
         ("c", "Aller tout droit")],
        "Réponse a", 43, exp="En l'absence de toute signalisation, la règle par défaut est la priorité à droite."))

    questions.append(q(212, "Routes de même nature", "Que faire à une intersection de routes de même nature ?",
        [("a", "Céder le passage à droite"),
         ("b", "Aller tout droit"),
         ("c", "Céder le passage à droite et à gauche")],
        "Réponse a", 43))

    questions.append(q(213, "Primauté des agents", "Les indications des agents de sécurité prévalent sur :",
        [("a", "Uniquement les feux tricolores"),
         ("b", "Toutes signalisations"),
         ("c", "Les règles de circulation"),
         ("d", "Les feux de signalisation")],
        "Réponse b, c et d", 44, tags=["multi-reponses"]))

    questions.append(q(214, "Principe de priorité à droite", "La priorité à droite consiste à :",
        [("a", "Céder le passage à tout véhicule venant de gauche comme de droite"),
         ("b", "Céder le passage uniquement aux véhicules venant de la droite"),
         ("c", "Ne céder le passage à aucun véhicule")],
        "Réponse b", 44))

    questions.append(q(215, "Feu rouge comportement", "A l’intersection munie de feux tricolores dont le rouge est allumé, que dois-je faire ?",
        [("a", "Je m’arrête"),
         ("b", "Je passe si je veux tourner à droite"),
         ("c", "Je ralentis et je passe si la voie est libre")],
        "Réponse a", 44))

    questions.append(q(216, "Feu jaune fixe", "A une distance raisonnable du feu jaune fixe, je me prépare à :",
        [("a", "Appliquer la règle de priorité à droite"),
         ("b", "Passer"),
         ("c", "M’arrêter"),
         ("d", "Céder le passage")],
        "Réponse c", 44))

    questions.append(q(217, "Agent vu de face", "Lorsque je vois de face l’agent de sécurité réglementant la circulation :",
        [("a", "Je passe"),
         ("b", "Je ralentis et je passe"),
         ("c", "J’applique la priorité à droite"),
         ("d", "Je ralentis et je m’arrête")],
        "Réponse d", 44))

    questions.append(q(218, "Ordre de passage I17", "A cette intersection I17, quel doit être l’ordre de passage des véhicules ?",
        [("a", "Jaune – vert – bleu"),
         ("b", "Bleu – vert – jaune"),
         ("c", "Rien de tout ce qui précède")],
        "Réponse c", 44, img="I17"))

    questions.append(q(219, "Sens giratoire agglomération", "Au carrefour à sens giratoire en agglomération :",
        [("a", "La priorité est toujours à droite"),
         ("b", "La priorité peut être donnée à droite et à gauche"),
         ("c", "Rien de tout ce qui précède")],
        "Réponse c", 45, exp="Voir question 239 : la priorité est donnée aux usagers engagés sur l'anneau lorsque la signalisation l'indique."))

    questions.append(q(220, "Ordre de passage I14", "A cette intersection I14, quel doit être l’ordre de passage des véhicules ?",
        [("a", "1. le véhicule bleu démarre, fait 1/4 de tour et s’arrête, 2. le véhicule rouge passe ensuite, 3. le véhicule jaune passe, 4. le véhicule bleu après"),
         ("b", "1. le véhicule bleu démarre, fait 1/4 de tour et s’arrête, 2. le véhicule jaune passe, 3. le véhicule rouge passe ensuite, 4. le véhicule bleu passe après")],
        "Réponse b", 45, img="I14", diff=2, tags=["piege"]))

    questions.append(q(221, "Agent vs Feux tricolores", "A une intersection munie de feux tricolores où un agent de sécurité réglemente la circulation, que dois-je faire ?",
        [("a", "Je respecte les feux"),
         ("b", "Je passe si le feu est au vert"),
         ("c", "Je suis les indications de l’agent")],
        "Réponse c", 45))

    questions.append(q(222, "Route revêtue vs terre en agglo", "A l’intersection d’une route revêtue et d’une route en terre, quelle est la règle de priorité à observer en agglomération ?",
        [("a", "La priorité de passage"),
         ("b", "La perte de priorité"),
         ("c", "La priorité à droite")],
        "Réponse c", 45, exp="En agglomération, la priorité à droite s'applique même entre route revêtue et terre."))

    questions.append(q(223, "Route revêtue vs terre hors agglo", "A l’intersection d’une route revêtue et d’une route en terre, quelle est la règle de priorité à observer hors agglomération par l’usager circulant sur la route en terre ?",
        [("a", "La priorité de passage"),
         ("b", "La perte de priorité"),
         ("c", "La priorité à droite")],
        "Réponse b", 46, exp="Hors agglomération, l'usager débouchant d'une route en terre perd toujours sa priorité face à la route bitumée."))

    questions.append(q(224, "Céder passage aux deux côtés", "Dans quels cas dois-je céder le passage aux usagers venant de gauche comme de droite ?",
        [("a", "Devant le feu rouge"),
         ("b", "Devant le triangle pointe en bas"),
         ("c", "Devant le feu vert"),
         ("d", "Quand je roule sur une route prioritaire")],
        "Réponse a-b", 46, tags=["multi-reponses"]))

    questions.append(q(225, "Ordre de passage I3", "Quel doit être l’ordre de passage des véhicules à cette intersection I3 ?",
        [("a", "Le véhicule rouge, le véhicule jaune et le véhicule bleu"),
         ("b", "Le véhicule bleu, le véhicule jaune et le véhicule rouge"),
         ("c", "Les véhicules jaune, rouge et bleu")],
        "Réponse b", 46, img="I3"))

    questions.append(q(226, "Intersection I7 règle", "A cette intersection I7 :",
        [("a", "Il faut appliquer la règle de la priorité à droite"),
         ("b", "Il faut appliquer la règle de courtoisie"),
         ("c", "La voiture jaune doit céder le passage à la rouge"),
         ("d", "La voiture rouge doit céder le passage à la jaune")],
        "Réponse a-d", 46, img="I7", tags=["multi-reponses"]))

    questions.append(q(227, "Intersection I9 manœuvre", "A l’intersection I9 :",
        [("a", "Le véhicule jaune peut tourner immédiatement à droite"),
         ("b", "Le véhicule jaune peut tourner immédiatement à gauche"),
         ("c", "Le véhicule jaune peut aller immédiatement tout droit")],
        "Réponse a", 47, img="I9"))

    questions.append(q(228, "Intersection I7 en ville", "A cette intersection I7, en agglomération, le véhicule rouge est sur la chaussée revêtue et le véhicule jaune est sur la chaussée en terre, quelle est la règle de priorité à observer ?",
        [("a", "La règle de courtoisie"),
         ("b", "La règle de la priorité à droite"),
         ("c", "La règle de la perte de priorité"),
         ("d", "La règle de la priorité de passage")],
        "Réponse b", 47, img="I7", exp="En agglomération, c'est la règle de priorité à droite qui s'applique."))

    questions.append(q(229, "Intersection I7 hors ville", "A cette intersection I7, hors agglomération, le véhicule rouge est sur la chaussée revêtue et le véhicule jaune est sur la chaussée en terre, quelle est la règle de priorité à appliquer ?",
        [("a", "La priorité de passage par le véhicule rouge"),
         ("b", "La perte de priorité par le véhicule jaune"),
         ("c", "La priorité à droite par les deux véhicules"),
         ("d", "La règle de courtoisie par les deux véhicules")],
        "Réponse a et b", 48, img="I7", tags=["multi-reponses"]))

    questions.append(q(230, "Intersection I8 ordre", "A cette intersection I8, quel doit être l’ordre de passage des véhicules ?",
        [("a", "1. les véhicules, jaune, bleu et la moto passent simultanément, 2. le véhicule rouge passe après"),
         ("b", "1. les véhicules jaune et bleu passent, 2. le véhicule rouge passe, 3. la moto passe après")],
        "Réponse b", 48, img="I8"))

    questions.append(q(231, "Intersection I9 premier véhicule", "A cette intersection I9, qui passera définitivement le premier ?",
        [("a", "la moto"),
         ("b", "le véhicule rouge"),
         ("c", "le véhicule vert"),
         ("d", "le véhicule jaune")],
        "Réponse c", 48, img="I9"))

    questions.append(q(232, "Blocage 4 voies sans droite libre", "A une intersection de route de même valeur où aucun usager n’a sa droite libre, s’applique :",
        [("a", "la priorité de passage pour les usagers venant de droite et de gauche"),
         ("b", "le jeu de courtoisie et ensuite la règle de la priorité à droite"),
         ("c", "la perte de priorité de passage pour les usagers venant de face")],
        "Réponse b", 48, exp="Quand tous les véhicules se bloquent mutuellement à droite, l'un cède par courtoisie pour débloquer la priorité à droite."))

    questions.append(q(233, "Intersection I10 ordre", "A cette intersection I10, quel doit être l’ordre de passage des véhicules ?",
        [("a", "1. la moto, 2. le véhicule jaune ensuite, 3. le véhicule bleu après"),
         ("b", "1. le véhicule jaune, 2. le véhicule bleu ensuite, 3. la moto après")],
        "Réponse b", 49, img="I10"))

    questions.append(q(234, "Intersection I12 virage à gauche", "A cette intersection I12, quel doit être l’ordre de passage des véhicules ?",
        [("a", "le véhicule bleu, le véhicule rouge et le véhicule vert"),
         ("b", "le véhicule vert démarre, fait 1/4 de tour et s’arrête, le véhicule bleu tourne, le véhicule rouge passe et le vert continue"),
         ("c", "le véhicule rouge avance en suivant le véhicule bleu qui tourne puis le véhicule vert tourne après")],
        "Réponse b", 49, img="I12", diff=2, tags=["piege"]))

    questions.append(q(235, "Intersection I18 feux et flèche", "A cette intersection I18, quel doit être l’ordre de passage des véhicules ?",
        [("a", "- le véhicule orange marque un arrêt, - les véhicules jaune, rouge et vert passent simultanément, - le véhicule orange laisse passer les piétons et passera au feu vert"),
         ("b", "– les véhicules jaune, rouge et vert passent simultanément, - le véhicule orange qui a vu la flèche verte tourne à droite"),
         ("c", "- véhicule orange tourne immédiatement, - les véhicules jaune, rouge et vert passent simultanément")],
        "Réponse a", 50, img="I18"))

    questions.append(q(236, "Panneau rencontré intersection I6", "Avant cette intersection I6, quel panneau ont rencontré les véhicules jaune et rouge ?",
        [("a", "panneau indiquant l’intersection d’une route à grande circulation"),
         ("b", "panneau indiquant le caractère prioritaire de la route")],
        "Réponse b", 50, img="I6"))

    questions.append(q(237, "Intersection I17 ordre bis", "A cette intersection I17, quel sera l’ordre de passage ?",
        [("a", "le véhicule jaune, le véhicule vert et le véhicule bleu"),
         ("b", "le véhicule bleu, le véhicule vert et le véhicule jaune"),
         ("c", "le véhicule bleu passe derrière le véhicule jaune et le véhicule vert après")],
        "Réponse c", 51, img="I17"))

    questions.append(q(238, "Intersection I22 piétons", "A cette intersection I22, quel sera l’ordre de passage ?",
        [("a", "Les véhicules jaune et bleu passent simultanément le véhicule rouge laisse passer les piétons et tourne à droite"),
         ("b", "Le véhicule rouge tourne immédiatement à droite et les véhicules jaune et bleu passent après"),
         ("c", "Pendant que les véhicules jaune et bleu passent simultanément, le véhicule rouge tourne à droite")],
        "Réponse a", 51, img="I22"))

    questions.append(q(239, "Sens giratoire agglomération bis", "Au carrefour à sens giratoire en agglomération :",
        [("a", "La priorité est toujours à droite"),
         ("b", "La priorité est donnée aux véhicules engagés dans le sens giratoire"),
         ("c", "La priorité peut être donnée à gauche et à droite")],
        "Réponse b", 51, exp="Sur un rond-point giratoire moderne, priorité absolue aux véhicules engagés sur l'anneau."))

    questions.append(q(240, "Passage niveau PN1", "Sur cette image PN1, le véhicule bleu doit :",
        [("a", "S’arrêter devant la demi-barrière et attendre le passage du train"),
         ("b", "Attendre que la demi-barrière s’élève et que le feu rouge s’éteigne avant de démarrer"),
         ("c", "Pouvoir se faufiler entre les demi-barrières pour partir après le passage du train")],
        "Réponse b", 51, img="PN1"))

    questions.append(q(241, "Passage voie aérienne PN3", "Sur cette image PN3, les véhicules rouge et bleu doivent :",
        [("a", "Passer"),
         ("b", "Attendre devant le premier panneau de signalisation et passer après l’avion"),
         ("c", "Attendre devant le deuxième panneau de signalisation et ne passer qu’après l’extinction du feu")],
        "Réponse c", 52, img="PN3"))

    questions.append(q(242, "Distance balise PN1", "Sur cette image PN1, le véhicule jaune se situe à :",
        [("a", "150m environ du passage à niveau"),
         ("b", "100m environ du passage à niveau"),
         ("c", "50m environ du passage à niveau")],
        "Réponse b", 52, img="PN1", tags=["chiffre"], exp="Balise à deux bandes obliques rouges = 100 m (1 bande = 50 m, 3 bandes = 150 m)."))

    questions.append(q(243, "Arrêt panneau STOP", "Sur une route où il y a un panneau STOP, l’arrêt se fait :",
        [("a", "Exactement devant le panneau"),
         ("b", "A la limite de la visibilité en l’absence de ligne blanche au sol"),
         ("c", "Si à la ligne blanche, la visibilité est insuffisante, on marque un second arrêt à la limite de la chaussée abordée")],
        "Réponse b-c", 52, tags=["multi-reponses"]))

    questions.append(q(244, "Intersection I11 ordre", "A cette intersection I11, quel sera l’ordre de passage ?",
        [("a", "1- la moto, 2- le véhicule jaune ensuite, 3- le véhicule rouge après"),
         ("b", "1- le véhicule jaune, 2- le véhicule rouge ensuite, 3- la moto après")],
        "Réponse b", 53, img="I11"))

    questions.append(q(245, "Intersection I12 premier", "A cette intersection I12, quel est le véhicule qui passera définitivement le premier ?",
        [("a", "le véhicule rouge"),
         ("b", "le véhicule bleu"),
         ("c", "le véhicule vert")],
        "Réponse b", 53, img="I12"))

    questions.append(q(246, "Intersection I24 ordre", "A cette intersection I24, quel sera l’ordre de passage ?",
        [("a", "1- le véhicule bleu, 2- le véhicule rouge ensuite, 3- le véhicule vert après"),
         ("b", "1- le véhicule vert, 2- le véhicule bleu ensuite, 3- le véhicule rouge après")],
        "Réponse b", 54, img="I24"))

    questions.append(q(247, "Intersection I26 véhicule prioritaire", "A cette intersection I26, quel est le véhicule qui passera le premier ?",
        [("a", "Le véhicule vert"),
         ("b", "Le véhicule Jaune"),
         ("c", "Le véhicule Rouge"),
         ("d", "Le véhicule bleu")],
        "Réponse c", 54, img="I26", exp="Le véhicule rouge est un camion de pompiers en mission avec gyrophares allumés."))

    questions.append(q(248, "Intersection I3 panneau jaune", "Quel panneau verra le véhicule jaune à cette intersection I3 ?",
        [("a", "Panneau d’intersection de deux routes de même nature"),
         ("b", "Panneau indiquant le caractère prioritaire d’une route"),
         ("c", "Aucun panneau")],
        "Réponse a", 55, img="I3"))

    questions.append(q(249, "Intersection I14 premier", "A cette intersection I14, quel est le véhicule qui passera définitivement le premier ?",
        [("a", "Le véhicule bleu"),
         ("b", "Le véhicule Rouge"),
         ("c", "Le véhicule jaune")],
        "Réponse c", 55, img="I14"))

    questions.append(q(250, "Intersection I1 ordre", "A cette intersection I1, quel est l’ordre de passage ?",
        [("a", "1- Le véhicule jaune, 2- Le véhicule rouge, 3- Le véhicule vert"),
         ("b", "1- Le véhicule rouge, 2- Les véhicules jaune et vert ensuite")],
        "Réponse b", 55, img="I1"))

    questions.append(q(251, "Intersection I5 ordre", "A cette intersection I5, quel sera l’ordre de passage ?",
        [("a", "1-le véhicule vert marque un arrêt, 2- les véhicules rouge et jaune passent ensuite, 3- enfin le véhicule vert passe"),
         ("b", "1- le véhicule rouge passe, 2- le véhicule vert passe, 3- le véhicule jaune passe après")],
        "Réponse b", 56, img="I5"))

    questions.append(q(252, "Intersection I14 étapes", "A cette intersection I14, quel sera l’ordre de passage ?",
        [("a", "1- le véhicule bleu passe, 2- le véhicule jaune passe ensuite, 3- Enfin le véhicule rouge passe"),
         ("b", "1-le véhicule bleu démarre, fait un quart de tour et s’arrête, 2- le véhicule rouge passe, 3- le véhicule bleu passe ensuite, 4- enfin le véhicule jaune passe"),
         ("c", "1- le véhicule bleu démarre fait un quart de tour et s’arrête, 2- le véhicule jaune passe, 3- le véhicule rouge passe ensuite, 4 – enfin le véhicule bleu passe")],
        "Réponse c", 56, img="I14"))

    questions.append(q(253, "Intersection I23 ordre", "A cette intersection I23, quel sera l’ordre de passage ?",
        [("a", "1- les véhicules vert et rouge passent, 2- les véhicules jaune et bleu passent après"),
         ("b", "1- les véhicules jaune et bleu s’arrêtent, 2-les véhicules vert et rouge passent, 3- le véhicule bleu tourne"),
         ("c", "1- le véhicule bleu tourne, 2- les véhicules vert et rouge passent, 3- le véhicule jaune passe au feu vert")],
        "Réponse b", 57, img="I23"))

    questions.append(q(254, "Intersection I26 feux", "A cette intersection I 26, quel sera l’ordre de passage ?",
        [("a", "1- les véhicules jaune et vert passent, 2- le véhicule bleu et le véhicule rouge marque un arrêt"),
         ("b", "1- les véhicules jaune, bleu et vert marquent un arrêt, 2- le véhicule rouge passe, 3- les véhicules qui auront le feu vert passeront après le véhicule rouge")],
        "Réponse b", 57, img="I26"))

    questions.append(q(255, "Intersection I15 panneau vert", "Quel panneau le conducteur du véhicule vert peut rencontrer à cette intersection I15 ?",
        [("a", "Panneau d’intersection de deux routes de même nature"),
         ("b", "Panneau d’intersection d’une route à grande circulation et d’une route secondaire"),
         ("c", "Panneau indiquant le caractère prioritaire d’une route"),
         ("d", "Panneau indiquant la fin du caractère prioritaire d’une route")],
        "Réponse b-c", 58, img="I15", tags=["multi-reponses"]))

    questions.append(q(256, "Intersection I23 dernier", "A cette intersection I23, quel est le véhicule qui passera le dernier ?",
        [("a", "Le véhicule jaune"),
         ("b", "Le véhicule Bleu"),
         ("c", "Les véhicules Jaune et bleu")],
        "Réponse a", 58, img="I23"))

    questions.append(q(257, "Intersection I20 passage immédiat", "A cette intersection I20, quel est le véhicule qui peut passer immédiatement ?",
        [("a", "Le véhicule jaune"),
         ("b", "Le véhicule vert qui a sa droite libre"),
         ("c", "Aucun véhicule"),
         ("d", "Les véhicules vert et jaune")],
        "Réponse c", 59, img="I20"))

    questions.append(q(258, "Comportement si dépassé", "Que doit faire un conducteur qui est sur le point d’être dépassé ?",
        [("a", "Il serre sa gauche sans accélérer"),
         ("b", "Il serre sa droite en accélérant"),
         ("c", "Il serre sa droite sans accélérer"),
         ("d", "Il reste au milieu de la chaussée en accélérant"),
         ("e", "Il serre sa droite en ralentissant")],
        "Réponse c", 59, exp="Règle d'or : serrer à droite et maintenir son allure (ne pas accélérer)."))

    questions.append(q(259, "Interdiction de dépasser", "Dans quels cas est-il interdit de dépasser ?",
        [("a", "Lorsque je gène un usager venant de derrière"),
         ("b", "Lorsque je suis au sommet d’une côte où dans un virage"),
         ("c", "Lorsque je suis en présence d’un panneau d’interdiction de dépasser"),
         ("d", "Lorsque je suis sur le point d’être dépassé")],
        "Réponses b-d-e", 59, tags=["ambiguite", "multi-reponses"]))

    questions.append(q(260, "Dépassement la nuit", "La nuit, pour dépasser :",
        [("a", "J’utilise mes avertisseurs sonores"),
         ("b", "J’utilise mes avertisseurs lumineux"),
         ("c", "Je ne fais rien de tout cela")],
        "Réponse b", 59, exp="La nuit, le klaxon est prohibé hors danger imminent : on utilise des appels de feux."))

    questions.append(q(261, "Ligne mixte franchissement", "Lorsque la ligne discontinue de la ligne mixte est plus proche du conducteur, on peut franchir cette ligne :",
        [("a", "Pour tourner à droite"),
         ("b", "Pour tourner à gauche"),
         ("c", "Pour dépasser puis se rabattre")],
        "Réponse b-c", 59, tags=["multi-reponses"]))

    questions.append(q(262, "Première précaution dépasser", "Quelle est la toute première précaution à observer pour effectuer un dépassement ?",
        [("a", "S’assurer que l’on n’est pas dans un cas d’interdiction"),
         ("b", "Accélérer pour dépasser"),
         ("c", "Bien serrer sa droite")],
        "Réponse a", 59))

    questions.append(q(263, "Côté normal de dépassement", "En général, de quel côté s’effectue le dépassement ?",
        [("a", "Par la droite"),
         ("b", "Par la gauche"),
         ("c", "Du côté de votre choix"),
         ("d", "Du côté où c’est possible")],
        "Réponse b", 60))

    questions.append(q(264, "Dépassement par la droite exception", "Dans quel cas peut-on être autorisé, à dépasser par la droite ?",
        [("a", "Quand on a une file ininterrompue de véhicules devant soi"),
         ("b", "Quand le véhicule à dépasser a déjà pris position pour tourner à gauche"),
         ("c", "En abordant une intersection"),
         ("d", "Sur une chaussée à sens unique")],
        "Réponse b", 60, exp="Seule exception formelle : quand l'usager qui précède a signalé et engagé son virage à gauche."))

    questions.append(q(265, "Fin de dépassement effectif", "Quand est-ce que le dépassement est effectif ?",
        [("a", "Quand l’usager dépassé apparaît dans le rétroviseur intérieur"),
         ("b", "Après avoir mis le clignotant à droite pour se rabattre"),
         ("c", "Quand on peut estimer soi-même que le dépassement est fait")],
        "Réponse a", 60, exp="On ne se rabat en sécurité que lorsqu'on aperçoit entièrement le véhicule dépassé dans le rétroviseur central."))

    questions.append(q(266, "Nombre d'étapes dépassement", "En combien d’étape s’effectue le dépassement ?",
        [("a", "En une étape"),
         ("b", "En deux étapes"),
         ("c", "En trois étapes")],
        "Réponse c", 60, exp="Les 3 étapes : 1. Préparation (contrôle + avertissement), 2. Manœuvre (déboîtement + dépassement), 3. Rabattement."))

    questions.append(q(267, "Cas d'interdiction dépasser", "Citez deux cas d’interdiction de dépasser :",
        [("a", "Devant un panneau interdisant de dépasser et sur une ligne continue"),
         ("b", "Devant un panneau interdisant de dépasser et sur une ligne discontinue"),
         ("c", "Sur des lignes mixtes dont la ligne discontinue se trouve du côté du conducteur")],
        "Réponse a", 60))

    questions.append(q(268, "Chaussée 3 voies double sens", "Sur une chaussée à 3 voies et à double sens, on utilise, pour dépasser :",
        [("a", "La voie centrale"),
         ("b", "La voie la plus à gauche"),
         ("c", "La voie la plus à droite")],
        "Réponse a", 60))

    questions.append(q(269, "Écart latéral entre autos", "Donner l’écart latéral minimal entre deux véhicules automobiles lors d’un dépassement :",
        [("a", "1m environ"),
         ("b", "0,50m environ"),
         ("c", "0,3m environ")],
        "Réponse b", 60, tags=["chiffre"], exp="Entre deux voitures : 0,50 m minimum."))

    questions.append(q(270, "Écart piéton ou cycliste agglo", "Donner l’écart minimal à observer par un automobiliste qui dépasse un piéton ou un cycliste en agglomération :",
        [("a", "1m environ"),
         ("b", "0,5m environ"),
         ("c", "2,0m environ")],
        "Réponse a", 60, tags=["chiffre"], exp="En agglomération : 1 m minimum. Hors agglomération : 1,50 m."))

    questions.append(q(271, "Être dépassé comportement", "Quel serait votre comportement quand un usager s’apprête à vous dépasser ?",
        [("a", "Je serre ma gauche"),
         ("b", "J’occupe l’axe médian de la chaussée"),
         ("c", "Je serre ma droite"),
         ("d", "Je ralentis")],
        "Réponse c", 61))

    questions.append(q(272, "Dépassements autorisés avec B3", "A la vue de ce panneau B3 je peux dépasser :",
        [("a", "Tous véhicules à moteur qui me précèdent"),
         ("b", "Un motocycliste sans side-car"),
         ("c", "Un véhicule à traction animale"),
         ("d", "Un cyclomotoriste sans side-car")],
        "Réponse b-c-d", 61, img="B3", tags=["multi-reponses", "piege"]))

    questions.append(q(273, "Comportement B3", "A la vue du panneau B3 :",
        [("a", "J’accélère et je passe"),
         ("b", "Je ne dois pas dépasser"),
         ("c", "Je dois dépasser par la droite")],
        "Réponse b", 61, img="B3"))

    questions.append(q(274, "Usage clignotants", "Dans quels cas doit-on utiliser les clignotants ?",
        [("a", "Lorsqu’on veut s’insérer dans la circulation"),
         ("b", "Lorsqu’on veut augmenter ou réduire sa vitesse"),
         ("c", "Lorsqu’on veut dépasser ou se rabattre"),
         ("d", "Lorsqu’on veut changer de direction"),
         ("e", "Lorsqu’on veut croiser")],
        "Réponse a-c-d", 61, tags=["multi-reponses"]))

    questions.append(q(275, "Usage feux de route", "Dans quels cas utilise t- on ses feux de route ?",
        [("a", "En agglomération dans une rue non éclairée"),
         ("b", "Lorsqu’on va croiser un autre usager"),
         ("c", "Lorsqu’on ne risque d’éblouir personne"),
         ("d", "Lorsqu’on quitte une zone éclairée pour une zone sombre")],
        "Réponse a-c-d", 61, tags=["multi-reponses"]))

    questions.append(q(276, "Dépassement interdit rase campagne", "En rase campagne le dépassement est autorisé :",
        [("a", "A proximité des intersections"),
         ("b", "Au sommet de côte"),
         ("c", "Dans les virages"),
         ("d", "Rien de tout ce qui précède")],
        "Réponse d", 61, exp="Il est strictement interdit de dépasser aux virages, sommets de côte et intersections sans visibilité."))

    questions.append(q(277, "Chronologie dépassement", "Pour effectuer un dépassement :",
        [("a", "J’avertis, je contrôle, puis je déboîte"),
         ("b", "Je contrôle, j’avertis et je déboîte"),
         ("c", "Je déboîte, j’avertis, je contrôle")],
        "Réponse b", 62, exp="Règle mnémotechnique : 1. Contrôle (rétroviseurs + angle mort), 2. Avertissement (clignotant), 3. Action (déboîtement)."))

    questions.append(q(278, "Feux de route pendant dépassement de nuit", "Lors du dépassement d’un véhicule la nuit, je mets les feux de route :",
        [("a", "Immédiatement après avoir déboîter"),
         ("b", "En arrivant à la hauteur du conducteur du véhicule à dépasser"),
         ("c", "Tout de suite après m’être rabattu")],
        "Réponse b", 62, diff=2, tags=["piege"]))

    questions.append(q(279, "Avertir usager le jour", "Comment prévenir l’usager à dépasser le jour ?",
        [("a", "Par des appels sonores"),
         ("b", "Par des appels lumineux"),
         ("c", "Par le clignotant")],
        "Réponse a", 62))

    questions.append(q(280, "Avertir usager la nuit", "Comment prévenir l’usager à dépasser la nuit ?",
        [("a", "Par des appels sonores"),
         ("b", "Par des appels lumineux"),
         ("c", "Par le clignotant")],
        "Réponse b", 62))

    questions.append(q(281, "Intersection deux routes même nature dépassement", "A une intersection de deux routes de même nature peut-on dépasser par la gauche ?",
        [("a", "On peut effectuer rapidement le dépassement"),
         ("b", "On ne peut pas effectuer le dépassement"),
         ("c", "On le peut si le véhicule qui me précède signal son intention de tourner à droite")],
        "Réponse b-c", 62, tags=["multi-reponses"]))

    questions.append(q(282, "Sommet de côte dépassement", "Aux sommets d’une côte :",
        [("a", "Je peux dépasser si ma voiture a une réserve d’accélération suffisante"),
         ("b", "Je peux dépasser à la hauteur d’une ligne continue"),
         ("c", "Je ne peux pas dépasser")],
        "Réponse c", 62))

    questions.append(q(283, "Chaussée 3 voies double sens 3ème position", "Sur une chaussée à double sens comportant trois voies :",
        [("a", "Je suis autorisé à dépasser en 3ème position lorsqu’aucun usager ne vient en face"),
         ("b", "Je suis autorisé à dépasser en 3ème position lorsque je juge suffisante la largeur de la chaussée"),
         ("c", "Je ne suis pas autorisé à dépasser en 3ème position")],
        "Réponse c", 62))

    questions.append(q(284, "Flèches de rabattement dépassement", "Au niveau des flèches de rabattement :",
        [("a", "Je suis autorisé à dépasser lorsqu’aucun usager ne vient en face"),
         ("b", "Je suis autorisé à dépasser lorsque je juge la largeur de la chaussée suffisante"),
         ("c", "Je ne suis pas autorisé à dépasser"),
         ("d", "Je suis autorisé si l’usager devant moi est trop lent")],
        "Réponse c", 63))

    questions.append(q(285, "Ligne mixte discontinue proche", "Au niveau d’une ligne continue accolée à une ligne discontinue plus proche du conducteur, peut-on effectuer le dépassement ?",
        [("a", "On ne peut pas effectuer le dépassement"),
         ("b", "On peut effectuer le dépassement"),
         ("c", "On ne peut pas effectuer le dépassement la nuit")],
        "Réponse b", 63))

    questions.append(q(286, "Dépassement passage à niveau", "A quel passage à niveau le dépassement est-il autorisé ?",
        [("a", "A un passage à niveau sans barrière"),
         ("b", "A un passage à niveau avec barrière à fonctionnement manuel"),
         ("c", "A un passage à niveau avec barrière à fonctionnement automatique"),
         ("d", "A aucun passage à niveau")],
        "Réponse d", 63))

    questions.append(q(287, "Situation virage D9", "Sur cette image D9 :",
        [("a", "Le véhicule bleu est en infraction"),
         ("b", "Le véhicule bleu effectue une bonne manœuvre"),
         ("c", "Le véhicule bleu n’est pas en infraction"),
         ("d", "Le véhicule bleu effectue une mauvaise manœuvre")],
        "Réponse a-d", 63, img="D9", tags=["multi-reponses"]))

    questions.append(q(288, "Chaussée D10 trois voies", "Sur cette chaussée D10 à trois voies et à double sens de circulation :",
        [("a", "Le véhicule jaune est en infraction"),
         ("b", "Le véhicule jaune n’est pas en infraction"),
         ("c", "Le véhicule jaune effectue une bonne manœuvre"),
         ("d", "Le véhicule jaune effectue une mauvaise manœuvre")],
        "Réponse a-d", 64, img="D10", tags=["multi-reponses"]))

    questions.append(q(289, "Situation D11 manœuvre", "Sur cette image D11 :",
        [("a", "Le véhicule jaune effectue une bonne manœuvre"),
         ("b", "Le véhicule jaune n’est pas en infraction"),
         ("c", "Le véhicule jaune effectue une mauvaise manœuvre"),
         ("d", "Le véhicule jaune est en infraction")],
        "Réponse a-b", 64, img="D11", tags=["multi-reponses"]))

    questions.append(q(290, "Situation D12 manœuvre", "Sur cette image D12 :",
        [("a", "Le véhicule vert est en infraction"),
         ("b", "Le véhicule vert effectue une bonne manœuvre"),
         ("c", "Le véhicule vert n’est pas en infraction"),
         ("d", "Le véhicule vert effectue une mauvaise manœuvre")],
        "Réponses b-c", 64, img="D12", tags=["multi-reponses"]))

    questions.append(q(291, "Chaussée 4 voies double sens D13", "Sur cette chaussée D13 à quatre voies et à double sens de circulation :",
        [("a", "Le véhicule vert n’est pas en infraction"),
         ("b", "Le véhicule vert effectue une bonne manœuvre"),
         ("c", "Le véhicule vert effectue une mauvaise manœuvre"),
         ("d", "Le véhicule vert est en infraction")],
        "Réponses c-d", 65, img="D13", tags=["multi-reponses"]))

    questions.append(q(292, "Chaussée 4 voies sens unique D13", "Sur cette chaussée D13 à quatre voies et à sens unique :",
        [("a", "Le véhicule vert n’est pas en infraction"),
         ("b", "Le véhicule vert effectue une bonne manœuvre"),
         ("c", "Le véhicule vert effectue une mauvaise manœuvre"),
         ("d", "Le véhicule vert est en infraction")],
        "Réponse a-b", 65, img="D13", tags=["multi-reponses"]))

    questions.append(q(293, "Situation D9 manœuvre", "Sur cette image D9 :",
        [("a", "Le véhicule bleu est en infraction"),
         ("b", "Le véhicule bleu n’est pas en infraction"),
         ("c", "Le véhicule bleu effectue une mauvaise manœuvre"),
         ("d", "Le véhicule bleu effectue une bonne manœuvre")],
        "Réponse a-c", 66, img="D9", tags=["multi-reponses"]))

    questions.append(q(294, "Chaussée 3 voies sens unique D10", "Sur cette chaussée D10 à trois voies et à sens unique de circulation :",
        [("a", "Le véhicule jaune est en infraction"),
         ("b", "Le véhicule jaune effectue une bonne manœuvre"),
         ("c", "Le véhicule jaune effectue une mauvaise manœuvre"),
         ("d", "Le véhicule jaune n’est pas en infraction")],
        "Réponses b-d", 66, img="D10", tags=["multi-reponses"]))

    questions.append(q(295, "Situation D4 manœuvre", "Sur cette image D4 :",
        [("a", "Le véhicule bleu est en infraction"),
         ("b", "Le véhicule bleu n’est pas en infraction"),
         ("c", "Le véhicule bleu effectue une bonne manœuvre"),
         ("d", "Le véhicule bleu effectue une mauvaise manœuvre")],
        "Réponses b-c", 66, img="D4", tags=["multi-reponses"]))

    questions.append(q(296, "Dépassement interdit voie gauche", "Sur une chaussée à plus de deux voies et à double sens de circulation, le dépassement est interdit :",
        [("a", "Sur la voie se trouvant la plus à gauche"),
         ("b", "Sur la voie du milieu"),
         ("c", "Sur toutes les voies")],
        "Réponse a", 66))

    questions.append(q(297, "Circulation chaussée 2 voies", "Sur une chaussée à deux voies et à double sens, je peux circuler :",
        [("a", "Sur la voie de gauche pour effectuer un dépassement"),
         ("b", "Sur la voie de gauche de façon continue"),
         ("c", "Sur la voie de droite seulement")],
        "Réponse a", 67))

    questions.append(q(298, "Ligne continue franchissement", "Le franchissement ou le chevauchement de la ligne continue est autorisé :",
        [("a", "A tout moment"),
         ("b", "A aucun moment"),
         ("c", "Pour effectuer un dépassement"),
         ("d", "Lorsque la chaussée est libre")],
        "Réponse b", 67))

    questions.append(q(299, "Temps de grand vent écart", "Vous circulez par temps de grand vent ; pour dépasser un autre usager :",
        [("a", "Vous diminuez l’écart latéral"),
         ("b", "Vous maintenez l’écart latéral"),
         ("c", "Vous augmentez l’écart latéral")],
        "Réponse c", 67, exp="Le vent peut dévier brusquement les deux-roues ou véhicules hauts : il faut augmenter l'intervalle de sécurité."))

    questions.append(q(300, "Effectuer un croisement", "Pour effectuer un croisement, je dois :",
        [("a", "Accélérer"),
         ("b", "Ralentir"),
         ("c", "Serrer ma droite")],
        "Réponse b-c", 67, tags=["multi-reponses"]))

    questions.append(q(301, "Croisement de nuit feux", "Pour effectuer un croisement la nuit, je dois :",
        [("a", "Klaxonner"),
         ("b", "Circuler en phare"),
         ("c", "Circuler en code"),
         ("d", "Circuler en feux de détresse")],
        "Réponse c", 67, exp="On passe obligatoirement en feux de croisement (code) pour éviter d'éblouir l'usager en face."))

    questions.append(q(302, "Croisement difficile terrain plat", "Quel est le véhicule qui doit s’arrêter à temps à cause d’un croisement difficile sur un terrain plat ?",
        [("a", "Le véhicule léger"),
         ("b", "Le véhicule encombrant"),
         ("c", "Le véhicule qui veut")],
        "Réponse b", 67, exp="Sur le plat, c'est le véhicule le plus encombrant (largeur > 2 m ou longueur > 7 m) qui doit s'arrêter ou faciliter le passage."))

    questions.append(q(303, "Croisement difficile pente", "Sur une pente, quel est le véhicule qui doit s’arrêter à temps à cause d’un croisement difficile ?",
        [("a", "Le véhicule montant"),
         ("b", "Le véhicule descendant"),
         ("c", "Le véhicule qui le désire")],
        "Réponse b", 67, exp="Règle en pente : le véhicule descendant s'arrête en premier car le véhicule qui monte a besoin d'élan et est plus difficile à redémarrer."))

    questions.append(q(304, "Croisement difficile agglomération", "En agglomération, quel est le véhicule qui doit s’arrêter à temps à cause d’un croisement difficile ?",
        [("a", "L’autobus"),
         ("b", "Le véhicule qui le désire"),
         ("c", "Le camion")],
        "Réponse c", 68))

    questions.append(q(305, "Marche arrière en pente même catégorie", "Lorsque deux véhicules de même catégorie se retrouvent sur une pente, lequel doit faire la marche arrière à cause d’un croisement difficile ?",
        [("a", "Le véhicule montant"),
         ("b", "Le véhicule descendant"),
         ("c", "Le véhicule qui veut")],
        "Réponse b", 68, exp="A catégorie égale, c'est le véhicule descendant qui recule."))

    questions.append(q(306, "Arrêt pour usager en sens inverse", "Dans quels cas dois-je m’arrêter pour laisser passer l’usager venant en sens inverse ?",
        [("a", "Devant le panneau \"chaussée rétrécie\" et un obstacle devant moi"),
         ("b", "Devant le panneau \"céder le passage\" aux usagers venant en sens inverse et devant un panneau \"chaussée rétrécie\""),
         ("c", "Devant le panneau sens interdit et un obstacle devant moi")],
        "Réponse a-b", 68, tags=["multi-reponses"]))

    questions.append(q(307, "Pente faciliter le passage", "Sur une pente, quel est le véhicule qui doit faciliter le passage lors d’un croisement difficile ?",
        [("a", "L’autobus chargé"),
         ("b", "Le camion"),
         ("c", "Le véhicule qui le désire")],
        "Réponse b", 68))

    questions.append(q(308, "Pente marche arrière isolé vs articulé", "Sur une pente, quel est le véhicule qui doit faire la marche arrière à cause d’un croisement difficile ?",
        [("a", "Le véhicule isolé"),
         ("b", "Le véhicule articulé"),
         ("c", "Le véhicule qui veut")],
        "Réponse a", 68, exp="Un véhicule articulé (avec remorque/semi-remorque) est bien plus difficile à manœuvrer en marche arrière qu'un véhicule isolé."))

    questions.append(q(309, "Éviter éblouissement de nuit", "La nuit, pour éviter d’être ébloui :",
        [("a", "Je regarde le bord droit de la chaussée"),
         ("b", "Je ferme les yeux pendant un court instant"),
         ("c", "Je porte des verres teintés"),
         ("d", "J’allume mes feux de route")],
        "Réponse a", 68, exp="Porter son regard sur la ligne blanche ou le bas-côté droit permet de ne pas fixer les phares éblouissants."))

    questions.append(q(310, "Différentiel de vitesse dépassement", "L’écart minimal de vitesse recommandé pour un véhicule qui veut effectuer le dépassement est de :",
        [("a", "30km/h"), ("b", "25 km/h"), ("c", "40 km/h"), ("d", "20 km/h"), ("e", "10 km/h")],
        "Réponse d", 68, tags=["chiffre"], exp="Il faut rouler au moins 20 km/h plus vite que le véhicule à dépasser pour effectuer la manœuvre rapidement et en sécurité."))

    questions.append(q(311, "Forte déclivité véhicule qui s'arrête", "Sur une chaussée à forte déclivité, quel est le véhicule qui doit s’arrêter à temps lorsque le croisement se révèle difficile ?",
        [("a", "Le véhicule descendant"),
         ("b", "Le véhicule qui le désire"),
         ("c", "Le véhicule montant")],
        "Réponse a", 69))

    questions.append(q(312, "Arrêt face à obstacle", "Je laisse passer l’usager d’en face en m’arrêtant :",
        [("a", "Quand se dresse un obstacle devant moi"),
         ("b", "Devant un panneau de circulation à sens unique"),
         ("c", "Quand je suis au volant d’un véhicule encombrant")],
        "Réponse a-c", 69, tags=["multi-reponses"]))

    questions.append(q(313, "Comportement usager qui dépasse", "Quel doit être mon comportement lorsqu’un usager manifeste son intention de me dépasser ?",
        [("a", "Je ne l’empêche pas si la manœuvre est régulière"),
         ("b", "Je serre ma droite le plus possible"),
         ("c", "J’accélère"),
         ("d", "Je maintiens mon allure et, au besoin je ralentis"),
         ("e", "La nuit, je passe en feu de croisement quand il arrive à ma hauteur")],
        "Réponse a-b-d-e", 69, tags=["multi-reponses"]))

    questions.append(q(314, "Céder passage aux deux côtés", "Dans quels cas devez vous céder le passage de gauche comme de droite ?",
        [("a", "devant le feu vert ou jaune clignotant"),
         ("b", "devant le feu rouge"),
         ("c", "devant le panneau « STOP »"),
         ("d", "devant le panneau « Triangle pointe en bas »"),
         ("e", "en sortant d’un chemin de terre, d’un garage ou d’un parking")],
        "Réponse b-c-d-e", 69, tags=["multi-reponses"]))

    questions.append(q(315, "Répétition panneau prioritaire hors agglo", "Hors agglomération, le panneau à caractère prioritaire est répété :",
        [("a", "tous les 5km"),
         ("b", "après chaque intersection"),
         ("c", "tous les 2km"),
         ("d", "après chaque virage"),
         ("e", "tous les kilomètres")],
        "Réponse a, b", 69, tags=["multi-reponses", "chiffre"]))

    questions.append(q(316, "Répétition panneau prioritaire en agglo", "En agglomération, le panneau à caractère prioritaire est répété :",
        [("a", "tous les 5 kilomètres"),
         ("b", "après chaque intersection"),
         ("c", "Tous les 2 kilomètres"),
         ("d", "Après chaque virage"),
         ("e", "Tous les kilomètres")],
        "Réponse e", 69, tags=["chiffre"]))

    questions.append(q(317, "But des ronds-points", "Quel est le but des ronds-points ?",
        [("a", "faciliter l’écoulement des trafics"),
         ("b", "briser les vitesses"),
         ("c", "permettre le stationnement des véhicules")],
        "Réponse a", 70))

    questions.append(q(318, "Dangers deux-roues", "A quoi peut-on s’attendre lors d’un croisement ou dépassement d’un véhicule à deux roues ?",
        [("a", "non respect des signaux"),
         ("b", "non respect des règles de priorité"),
         ("c", "des écarts sans avertir, sans contrôler")],
        "Réponse a-b-c", 70, tags=["multi-reponses"]))

    questions.append(q(319, "Voie du milieu choix de direction", "A cette intersection Im4 ; P55, l’usager se trouvant dans la voie du milieu peut :",
        [("a", "tourner à droite"),
         ("b", "tourner à gauche"),
         ("c", "continuer tout droit")],
        "Réponse c", 70, img="Im4_P55"))

    questions.append(q(320, "Intersection Im5 P55 véhicule bleu", "A cette intersection (Im5 ; P55) le véhicule bleu passe :",
        [("a", "avant le véhicule blanc"),
         ("b", "après le véhicule blanc"),
         ("c", "le dernier")],
        "Réponse b", 70, img="Im5_P55"))

    questions.append(q(321, "Intersection Im6 P65 premier", "A cette intersection (Im6 ; P65) quel est le véhicule qui passe le premier ?",
        [("a", "le rouge"),
         ("b", "le jaune"),
         ("c", "le bleu")],
        "Réponse b", 71, img="Im6_P65"))

    questions.append(q(322, "Intersection Im7 P65 immédiat", "A cette intersection Im7 ; P65, quel est le véhicule qui peut passer immédiatement ?",
        [("a", "le bleu"),
         ("b", "le jaune"),
         ("c", "le vert")],
        "Réponse a", 71, img="Im7_P65"))

    questions.append(q(323, "Intersection Im8 P55 tourner droite", "A cette intersection Im8 P55 le véhicule vert peut :",
        [("a", "tourner immédiatement à droit"),
         ("b", "continuer tout droit"),
         ("c", "ne peut tourner immédiatement à droite")],
        "Réponse c", 71, img="Im8_P55"))

    questions.append(q(324, "Repère visuel pour se rabattre", "Pour me rabattre à droite après un dépassement, j’attends :",
        [("a", "De ne plus voir le véhicule par la vitre latérale droite"),
         ("b", "De voir le véhicule dans mon rétroviseur droit"),
         ("c", "De voir le véhicule dans mon rétroviseur intérieur")],
        "Réponse c", 72, exp="Le rétroviseur intérieur donne l'angle de vision qui confirme une distance de sécurité suffisante."))

    questions.append(q(325, "Force centrifuge paramètres", "La force centrifuge augmente proportionnellement :",
        [("a", "Avec la vitesse"),
         ("b", "Avec le rayon de la courbe"),
         ("c", "Avec la charge du véhicule")],
        "Réponse a-c", 72, tags=["multi-reponses"]))

    questions.append(q(326, "Route prioritaire et dépassement", "A l’approche d’une intersection, sur une route à caractère prioritaire :",
        [("a", "je peux dépasser un véhicule"),
         ("b", "je ne peux pas dépasser un véhicule"),
         ("c", "je ne peux pas dépasser lorsqu’il y a un marquage au sol l’interdisant")],
        "Réponse a-c", 72, tags=["multi-reponses"]))

    questions.append(q(327, "Route prioritaire intersections", "Je suis sur une route à caractère prioritaire, si je n’ai pas à céder le passage :",
        [("a", "à droite aux intersections"),
         ("b", "à gauche aux intersections"),
         ("c", "à la prochaine intersection seulement")],
        "Réponse a-b", 72, tags=["multi-reponses"]))

    questions.append(q(328, "Position dans la voie", "Pour ma sécurité et celle des autres, je dois circuler :",
        [("a", "à droite dans ma voie"),
         ("b", "au centre de ma voie"),
         ("c", "à gauche dans ma voie")],
        "Réponse a", 72))

    questions.append(q(329, "Croisement à l'indonésienne", "Dans un croisement à l’indonésienne, les véhicules se croisent :",
        [("a", "par la droite"),
         ("b", "par la gauche")],
        "Réponse b", 72, exp="Au croisement à l'indonésienne, les véhicules tournant à gauche passent l'un devant l'autre (se croisent par la gauche)."))

    questions.append(q(330, "Intersection sans signalisation céder", "A une intersection sans signalisation, je dois céder le passage :",
        [("a", "à gauche seulement"),
         ("b", "à droite seulement"),
         ("c", "à droite et à gauche"),
         ("d", "à aucun usager")],
        "Réponse b", 72))

    questions.append(q(331, "Croisement montagne route étroite", "En montagne, sur une route étroite, celui qui doit s’arrêter est :",
        [("a", "Le véhicule qui monte"),
         ("b", "Le véhicule qui descend"),
         ("c", "Le véhicule le plus chargé"),
         ("d", "Le véhicule le moins chargé")],
        "Réponse b", 72))

    questions.append(q(332, "Freinage longue descente", "Dans une longue et forte descente :",
        [("a", "Je Freine en permanence pour ne pas prendre de vitesse"),
         ("b", "Je freine au début pour rétrograder et utiliser le frein moteur"),
         ("c", "Dans des lignes droites, je mets le levier de vitesse au point mort pour consommer moins de carburant")],
        "Réponse b", 73, exp="Rétrograder permet d'utiliser le frein moteur et évite l'échauffement ou la perte d'efficacité des freins."))

    questions.append(q(333, "Intersection Im3 ordre", "Sur cette image Im 3 quel est l’ordre de passage des voitures :",
        [("a", "rouge d’abord, bleue ensuite et enfin vert"),
         ("b", "bleue d’abord puis vert et rouge simultanément, vert d’abord, bleue ensuite et rouge en fin")],
        "Réponse a", 73, img="Im3_P73"))

    questions.append(q(334, "Règle et ordre Im1", "Donnez la règle à appliquer et l’ordre de passage des véhicules :",
        [("a", "perte de priorité"),
         ("b", "priorité de passage"),
         ("c", "priorité à droite"),
         ("d", "rouge, bleu, jaune"),
         ("e", "bleu, jaune, rouge")],
        "Réponse c, d", 73, img="Im1_P73", tags=["multi-reponses"]))

    questions.append(q(335, "Règles et ordre Im2 P47", "Sur cette image Im2 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "priorité à droite"),
         ("b", "perte de priorité"),
         ("c", "priorité de passage"),
         ("d", "jaune et bleu simultanément puis rouge"),
         ("e", "rouge, jaune, bleu")],
        "Réponse b, c, d", 74, img="Im2_P47", tags=["multi-reponses"]))

    questions.append(q(336, "Règles et ordre Im3 P47", "Sur cette image Im3 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "priorité à droite"),
         ("b", "priorité de passage"),
         ("c", "perte de priorité"),
         ("d", "jaune, bleu, rouge"),
         ("e", "bleu, rouge, jaune")],
        "Réponse a, d", 74, img="Im3_P47", tags=["multi-reponses"]))

    questions.append(q(337, "Règles et ordre Im4 P47", "Sur cette image Im4 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "perte de priorité"),
         ("b", "priorité de passage"),
         ("c", "courtoisie"),
         ("d", "jaune et rouge simultanément puis bleu et blanc après"),
         ("e", "Bleu et blanc simultanément puis rouge et jaune après")],
        "Réponse a, b, d", 74, img="Im4_P47", tags=["multi-reponses"]))

    questions.append(q(338, "Règles et ordre Im5 P47", "Sur cette image Im5 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "perte de priorité"),
         ("b", "priorité à droite"),
         ("c", "priorité de passage"),
         ("d", "bleue, rouge, jaune"),
         ("e", "bleu et jaune simultanément puis rouge après")],
        "Réponse a, c, e", 75, img="Im5_P47", tags=["multi-reponses"]))

    questions.append(q(339, "Règles et ordre Im6 P47", "Sur cette image Im6 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "priorité à droite"),
         ("b", "priorité de passage"),
         ("c", "perte de priorité"),
         ("d", "rouge d’abord, puis bleu et jaune après"),
         ("e", "bleu, rouge et jaune")],
        "Réponse b, c, d", 75, img="Im6_P47", tags=["multi-reponses"]))

    questions.append(q(340, "Règles et ordre Im7 P47", "Sur cette image Im7 P47, donnez les règles à appliquer et l’ordre de passage des véhicules :",
        [("a", "perte de priorité"),
         ("b", "priorité de passage"),
         ("c", "la priorité à droite"),
         ("d", "bleu, jaune, rouge"),
         ("e", "bleu et rouge simultanément, puis jaune après")],
        "Réponse a, b, e", 76, img="Im7_P47", tags=["multi-reponses"]))

    questions.append(q(341, "Panneau manquant Im1 P49", "Sur cette image Im1 P49, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau AB1 (Croix rouge)"),
         ("b", "Panneau AB2 (Flèche barrée)"),
         ("c", "Panneau AB3a (Cédez le passage)"),
         ("d", "Panneau AB4 (STOP)"),
         ("e", "Panneau AB6 (Losange jaune)")],
        "Réponse a", 76, img="Im1_P49"))

    questions.append(q(342, "Panneau manquant Im2 P49", "Sur cette image Im2 P49, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau AB2"),
         ("b", "Panneau AB3a (Cédez le passage)"),
         ("c", "Panneau STOP"),
         ("d", "Panneau AB6"),
         ("e", "Panneau AB7")],
        "Réponse b", 77, img="Im2_P49"))

    questions.append(q(343, "Panneau manquant Im3 P49", "Sur cette image Im3 P49, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau AB1"),
         ("b", "Panneau AB2"),
         ("c", "Panneau AB3a"),
         ("d", "Panneau STOP"),
         ("e", "Panneau AB6")],
        "Réponse b, e", 77, img="Im3_P49", tags=["multi-reponses"]))

    questions.append(q(344, "Panneau manquant Im4 P49", "Sur cette image, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau a"), ("b", "Panneau b"), ("c", "Panneau c"), ("d", "Panneau d"), ("e", "Panneau e")],
        "Réponse e", 78, img="Im4_P49"))

    questions.append(q(345, "Panneau manquant Im5 P49", "Sur cette image Im5 P49, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau a"), ("b", "Panneau b"), ("c", "Panneau c"), ("d", "Panneau d"), ("e", "Panneau e")],
        "Réponse e", 78, img="Im5_P49"))

    questions.append(q(346, "Panneau manquant Im6 P49", "Sur cette image Im6 P49, choisi le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau a"), ("b", "Panneau b"), ("c", "Panneau c"), ("d", "Panneau d"), ("e", "Panneau e")],
        "Réponse c", 78, img="Im6_P49"))

    questions.append(q(347, "Panneau manquant Im7 P49", "Sur cette image Im7 P49, choisissez le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau a"), ("b", "Panneau b"), ("c", "Panneau c"), ("d", "Panneau d"), ("e", "Panneau e")],
        "Réponse b", 79, img="Im7_P49"))

    questions.append(q(348, "Panneau manquant Im8 P49", "Sur cette image Im8 P49, choisi le panneau manquant parmi les panneaux proposés :",
        [("a", "Panneau a"), ("b", "Panneau b"), ("c", "Panneau c"), ("d", "Panneau d"), ("e", "Panneau e")],
        "Réponse a, c", 79, img="Im8_P49", tags=["multi-reponses"]))

    questions.append(q(349, "Ligne d'avertissement Im1 P60", "Sur cette image Im N°1 P60 :",
        [("a", "nous sommes en présence d’une ligne d’avertissement"),
         ("b", "le véhicule bleu peut dépasser"),
         ("c", "le véhicule rouge peut s’arrêter sur la chaussée"),
         ("d", "la ligne de rive peut être franchie")],
        "Réponse a, b, d", 79, img="Im1_P60", tags=["multi-reponses"]))

    questions.append(q(350, "Geste agent passage autorisé", "Sur cette image (Im 1 p57), quelle est la position de l’agent qui vous autorise le passage ?",
        [("a", "Position a (de profil)"),
         ("b", "Position b (de face avec bras levé)"),
         ("c", "Position c (bras en croix de face)")],
        "Réponse a", 80, img="Agent_P57", exp="Position de profil = passage autorisé."))

    questions.append(q(351, "Carrefour avec agent Im2", "Quel est l’ordre de passage des véhicules à cette intersection (Im 2) :",
        [("a", "rouge- jaune – bleu – blanc"),
         ("b", "rouge et bleu simultanément puis blanc et jaune sur ordre de l’agent"),
         ("c", "jaune et blanc simultanément puis bleu et rouge sur ordre de l’agent")],
        "Réponse b", 80, img="Agent_Im2"))

    questions.append(q(352, "Carrefour avec agent In 3", "A cette intersection In 3, quel sera l’ordre de passage des véhicules ?",
        [("a", "rouge – blanc- jaune –vert"),
         ("b", "bleu et rouge simultanément puis bleu et vert au feu vert"),
         ("c", "bleu et vert simultanément puis rouge et jaune sur l’ordre de l’agent")],
        "Réponse c", 81, img="Agent_In3"))

    questions.append(q(353, "Geste agent N°1", "Sur cette image (Im5) que signifie le geste de l’agent N°1 ?",
        [("a", "passer rapidement"),
         ("b", "ralentir"),
         ("c", "s’arrêter")],
        "Réponse b", 81, img="Agent_Im5_1", exp="Mouvement de haut en bas avec la main = ralentir."))

    questions.append(q(354, "Geste agent N°2", "Sur cette image Im 5 que signifie le geste de l’agent N°2 ?",
        [("a", "passer rapidement"),
         ("b", "ralentir"),
         ("c", "s’arrêter")],
        "Réponse b", 81, img="Agent_Im5_2"))

    questions.append(q(355, "Geste agent N°3", "Sur cette image Im 5 que signifie la position de l’agent N°3 ?",
        [("a", "passer rapidement"),
         ("b", "ralentir"),
         ("c", "s’arrêter")],
        "Réponse c", 82, img="Agent_Im5_3", exp="Bras levé verticalement = arrêt pour tous les usagers."))

    questions.append(q(356, "Intersection Im6 avec agent", "A cette intersection Im 6 quel sera l’ordre de passage des véhicules ?",
        [("a", "jaune-rouge-bleu"),
         ("b", "bleu et jaune simultanément puis rouge dès que la chaussée abordée par lui sera libre"),
         ("c", "vert, jaune et rouge, bleu sur l’ordre de l’agent")],
        "Réponse c", 82, img="Agent_Im6"))

    questions.append(q(357, "Intersection Im 7 avec agent", "A cette image Im 7 quel sera l’ordre de passage des véhicules ?",
        [("a", "vert et jaune, puis rouge et bleu"),
         ("b", "rouge et bleu puis le jaune et vert"),
         ("c", "vert et jaune, puis rouge et bleu sur ordre de l’agent")],
        "Réponse c", 83, img="Agent_Im7"))

    questions.append(q(358, "Intersection Im1 feux", "Sur cette image Im 1 quel est l’ordre de passage des voitures :",
        [("a", "rouge et jaune simultanément puis bleue au feu vert"),
         ("b", "bleue puis rouge et jaune simultanément"),
         ("c", "jaune d’abord, bleue ensuite et enfin rouge")],
        "Réponse a", 83, img="Im1_P83"))

    questions.append(q(359, "Croisement véhicules en codes", "Lorsque les véhicules que je croise roulent en feux de croisement, je prévois que je peux rencontrer :",
        [("a", "une zone d’intempéries"),
         ("b", "un contrôle de vitesse"),
         ("c", "un contrôle routier")],
        "Réponse a", 83, exp="Si les véhicules en face allument leurs codes en plein jour, c'est signe d'une averse ou nappe de brouillard en avant."))

    return questions

if __name__ == '__main__':
    qs = get_chapitre3_questions()
    print(f"Chapitre 3 loaded: {len(qs)} questions")
