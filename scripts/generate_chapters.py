"""
DGTT 2011 Question Database Generator & QA Auditor
Generates:
- src/data/questions.json
- src/data/courseContent.json
- src/data/ambiguites.json
- src/data/keyNumbers.json
- qa-report.md
"""
import json
import os
import re

os.makedirs('src/data', exist_ok=True)

# Helper to normalize question objects
def create_q(num, chap, theme, enonce, options, reponse_str, page, img=None, exp=None, diff=1, tags=None):
    if tags is None:
        tags = []
    
    # Parse answers
    clean_rep = reponse_str.lower().strip()
    # matches like "réponse a", "réponses a-b", "réponse : a, c, d", "réponses a-c-d", "réponse c et d"
    clean_rep = re.sub(r'^réponses?\s*[:\.]?\s*', '', clean_rep)
    clean_rep = clean_rep.strip('.')
    
    bonnes = []
    if '-' in clean_rep:
        # e.g. "a-c" or "a-c-d" or "a-b-c-d"
        parts = clean_rep.split('-')
        for p in parts:
            p = p.strip()
            if p in ['a', 'b', 'c', 'd', 'e']:
                bonnes.append(p)
    elif ',' in clean_rep:
        parts = clean_rep.split(',')
        for p in parts:
            p = p.strip()
            if ' et ' in p:
                for sub in p.split(' et '):
                    if sub.strip() in ['a', 'b', 'c', 'd', 'e']:
                        bonnes.append(sub.strip())
            elif p in ['a', 'b', 'c', 'd', 'e']:
                bonnes.append(p)
    elif ' et ' in clean_rep:
        parts = clean_rep.split(' et ')
        for p in parts:
            p = p.strip()
            if p in ['a', 'b', 'c', 'd', 'e']:
                bonnes.append(p)
    else:
        p = clean_rep.strip()
        if p in ['a', 'b', 'c', 'd', 'e']:
            bonnes.append(p)
        else:
            # Handle letters inside words or formatting
            for char in p:
                if char in ['a', 'b', 'c', 'd', 'e']:
                    bonnes.append(char)
                    
    # Dedup and sort
    bonnes = sorted(list(set(bonnes)))
    
    multi = len(bonnes) > 1
    if multi and "multi-reponses" not in tags:
        tags.append("multi-reponses")
        
    formatted_opts = []
    for opt_id, opt_text in options:
        formatted_opts.append({"id": opt_id, "texte": opt_text})
        
    # Categories tag
    is_cat_b = chap in [1, 2, 3, 4, 5, 6, 8, 11]
    if is_cat_b:
        tags.append("categorie-b")
    else:
        tags.append("autres-categories")
        
    return {
        "id": f"q{num}",
        "numero": num,
        "chapitre": chap,
        "theme": theme,
        "enonce": enonce.strip(),
        "options": formatted_opts,
        "bonnesReponses": bonnes,
        "multiReponses": multi,
        "image": img,
        "page": page,
        "explication": exp,
        "sourceExplication": "manuel" if exp else None,
        "tags": tags,
        "difficulte": diff,
        "groupeDoublon": None
    }

print("Script template ready.")
