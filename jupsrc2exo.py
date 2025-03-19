import re
import nbformat
goal ="""This script take a notebook with the following format to generate the exercice :
myvar = myfunc(param1) # EXO__param1__<fill>__EXO
to generate
myvar = myfunc(<fill>)

This aims to provide functional notebook to build the exercice and introduce some hole to student for filling.
"""
def generate_notebooks(input_path, exercise_output_path):
    # Lire le notebook source
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Expression régulière pour trouver les balises EXO
    pattern = re.compile(r"(.*?)# EXO__(.*?)__(.*?)__EXO")

    # Générer l'exercice pour les étudiants
    exercise_nb = nbformat.v4.new_notebook()
    for cell in nb.cells:
        if cell.cell_type == 'code':
            exercise_code = cell.source
            matches = pattern.findall(exercise_code)
            for match in matches:
                # Remplacer le texte avant le commentaire par le motif
                exercise_code = exercise_code.replace(match[0], match[0].replace(match[1], match[2]))
                # Supprimer le commentaire
                exercise_code = re.sub('# EXO__.*__EXO', ' ',exercise_code)
            cell.source = exercise_code
        exercise_nb.cells.append(cell)
    
    # Sauvegarder les notebooks
    with open(exercise_output_path, 'w', encoding='utf-8') as f:
        nbformat.write(exercise_nb, f)

# Chemins des fichiers
input_path = 'source_notebook.ipynb'
exercise_output_path = 'exercice_etudiants.ipynb'

# Générer les notebooks
generate_notebooks(input_path, exercise_output_path)

