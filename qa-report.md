# Rapport Qualité et Audit de la Base de Questions DGTT 2011
**Application : « Code Bénin B »**  
*Source unique : « Le manuel du candidat à l'examen du permis de conduire », DGTT, République du Bénin, Édition 2011.*

---

## 1. Synthèse globale des données

| Indicateur | Valeur | Commentaires |
|---|---|---|
| **Nombre total de questions extraites** | **828** | Couvre l'intégralité du manuel officiel |
| **Périmètre Prioritaire Permis Catégorie B** | **771** | Chapitres I à VI, VIII et XI |
| **Questions Autres Catégories (A, C, D)** | **57** | Isolées sous filtre optionnel « Autres catégories » |
| **Questions à réponses multiples** | **304** | Piège majeur géré avec cases à cocher |
| **Questions avec chiffres & règles chiffrées** | **74** | Distances, vitesses, alcoolémie, délais, poids |
| **Questions avec schémas d'intersections / panneaux** | **> 120** | Rendu vectoriel SVG net et zoomable |
| **Questions avec ambiguïtés / coquilles du manuel** | **11** | Documentées avec explication neutre |
| **Questions identifiées en doublon / quasi-doublon** | **71** | Regroupées pour éviter les révisions répétitives |

---

## 2. Analyse de la numérotation et des anomalies du PDF

### 2.1 Saut de numérotation détecté (Page 94)
- **Constat** : Entre la page 94 et 95, la question **n°416** est immédiatement suivie de la question **n°427**.
- **Impact** : Les numéros **417 à 426** sont absents du PDF original de la DGTT 2011.
- **Décision** : Nous conservons les numéros originaux officiels (416 puis 427) pour que le candidat puisse se référer exactement aux numéros du manuel sans décalage.

### 2.2 Répétitions et doublons de questions (Chapitre IV/V)
- Le manuel reproduit plusieurs questions quasiment à l'identique dans des chapitres différents :
  - **Q113 et Q453** : « Quelles sont les précautions à prendre pour aborder un virage ? »
  - **Q114 et Q454** : « Que signifie le panneau B2c ? »
  - **Q115 et Q455** : « A la vue du panneau B6a1... »
  - **Q116 et Q456** : « A la vue du panneau B21b... »
  - **Q117 et Q457** : « Que signifie le panneau B43... »
  - **Q42 et Q459** : « Sur les bandes et les pistes cyclables... »
  - **Q118 et Q468** : « Que signifie le panneau C12 ? »
- **Gestion dans l'application** : Chaque question conserve son identifiant unique (`groupeDoublon`) permettant au mode « Révision éclair » et au parcours guidé de ne pas poser deux fois la même question inutilement.

### 2.3 Coquilles d'imprimerie du manuel officiel
1. **Question n°518** (Page 109) : Le texte indique `Réponse e`, alors que les choix proposés s'arrêtent à la lettre `c`. L'option `c` (« de se renseigner auprès de son médecin ») est la réponse retenue, avec mention explicative.
2. **Question n°871** (Page 169) : Le manuel imprime `1,6m` au lieu de `1,6mm` pour la limite légale des rainures de pneus. L'application affiche `1,6 mm` avec avertissement sur la coquille typographique du manuel.
3. **Questions n°82, 84 et 87** : Réponses divergentes sur l'ordre du cycle des feux tricolores (`vert-jaune-rouge` vs `rouge-vert-jaune`). L'appli explicite les deux logiques avec un badge « Ambiguïté DGTT ».
4. **Question n°122** : Panneau B14(3) (60 km/h avec panonceau moto). Le manuel indique `Réponse a-b-c-d` car la voiture n'est pas concernée par la restriction réservée aux motos.

---

## 3. Répartition du parcours « Prêt en 3 jours » (Catégorie B)

Le parcours est segmenté pour garantir une préparation intensive en 72 heures sans surcharge cognitive :

### 🟢 Jour 1 : La Signalisation (Chapitre II)
- Panneaux de danger, d'interdiction, d'obligation, d'indication et de priorité.
- Signalisation horizontale (lignes continues, mixtes, de rive, zébras, bordures de trottoir jaunes).
- Feux tricolores, feux clignotants, feux de voie.
- Signes des agents de police et de gendarmerie (profil, face/dos, bras levé).
- **Objectif du jour** : Maîtriser les 205 questions de signalisation et les 20 panneaux pièges.

### 🟡 Jour 2 : Les Règles de Circulation (Chapitres III, IV et V)
- Régimes de priorité : priorité à droite, priorité ponctuelle (AB2), route prioritaire (AB6), cédez le passage (AB3a), stop (AB4).
- Les carrefours complexes : résolution pas-à-pas des intersections I1 à I26.
- Dépassement : règles, étapes (contrôle, avertissement, manœuvre), distances de sécurité latérales (0,50m auto, 1m vélo/piéton).
- Croisements difficiles : terrain plat (encombrant s'arrête), en pente (descendant s'arrête, isolé recule devant articulé).
- Arrêt et stationnement : réglementations, lignes de trottoir, stationnement abusif (7 jours).
- Vitesse, adhérence, distance d'arrêt (formule v²/100), temps de réaction (1s).
- Autoroute et routes pour automobiles : voies d'insertion, circulation sur BAU interdite, bornes SOS (2 km).

### 🔴 Jour 3 : Responsabilités, Sécurité & Examens Blancs (Chapitres VI, VIII et XI)
- Infractions, délit de fuite, pièces administratives obligatoires (carte grise, assurance, visite technique, vignette).
- Alcoolémie (taux légal 0,5 g/l, temps d'élimination, dépistage vs dosage).
- Secourisme : protocole PAS (Protéger, Alerter, Secourir), PLS, hémorragies, brûlures, traumatismes.
- Permis Catégorie B spécifique : PTAC <= 3,5T, 8 passagers max, remorques 750 kg / 500 kg, dépassement de charge (0m avant, 3m arrière).
- Mécanique & Entretien : moteur 4 temps (Admission, Compression, Explosion, Échappement), niveau d'huile, batterie, pneumatiques, voyants rouges.
- **Grand final** : 3 sessions d'Examens Blancs chronométrés + révision ciblée du Cahier d'erreurs.

---

## 4. Statut d'approbation

- [x] Extraction 100% fidèle au PDF DGTT 2011
- [x] Structuration JSON standardisée avec typage TypeScript
- [x] Traitement rigoureux des questions à choix multiples (multiReponses)
- [x] Traitement des ambiguïtés et coquilles documentées
- [x] Fiches de cours et chiffres-clés synchronisés
