#!/usr/bin/python
# -*- coding: latin-1 -*-

import re
import nbformat
import argparse

goal = """This script takes a notebook with the following format to generate the exercise:
myvar = myfunc(param1) # EXO__param1__<fill>__EXO
to generate
myvar = myfunc(<fill>)

This aims to provide functional notebook to build the exercise and introduce some holes for students to fill.
"""

def generate_notebooks(input_path, exercise_output_path):
    # Lire le notebook source
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Expression régulière pour trouver les balises EXO
    pattern_exo = re.compile(r"(.*?)# EXO__(.*?)__(.*?)__EXO")
    # Expression régulière pour trouver les blocs DEBEXO/FINEXO
    pattern_block = re.compile(r"##DEBEXO##(.*?)##FINEXO##", re.DOTALL)

    # Générer l'exercice pour les étudiants
    exercise_nb = nbformat.v4.new_notebook()
    for cell in nb.cells:
        if cell.cell_type == 'code':
            exercise_code = cell.source

            # Traiter les balises EXO
            matches = pattern_exo.findall(exercise_code)
            for match in matches:
                exercise_code = exercise_code.replace(match[0], match[0].replace(match[1], match[2]))
            exercise_code = re.sub('# EXO__.*__EXO', ' ', exercise_code)

            # Traiter les blocs DEBEXO/FINEXO
            blocks = pattern_block.findall(exercise_code)
            for block in blocks:
                # Remplacer le contenu du bloc par un commentaire ou autre traitement
                exercise_code = exercise_code.replace('##DEBEXO##'+block+'##FINEXO##', "# Code à compléter par l'étudiant")

            cell.source = exercise_code
            exercise_nb.cells.append(cell)
        else:
            exercise_nb.cells.append(cell)

    # Sauvegarder les notebooks
    with open(exercise_output_path, 'w', encoding='utf-8') as f:
        nbformat.write(exercise_nb, f)

# Chemins des fichiers
input_path = 'source_notebook.ipynb'
exercise_output_path = 'exercice_etudiants.ipynb'
def main():
    parser = argparse.ArgumentParser(description=goal)
    parser.add_argument('input_path', type=str, help='Chemin du fichier notebook source')
    parser.add_argument('exercise_output_path', type=str, help='Chemin du fichier notebook de sortie pour les étudiants')

    args = parser.parse_args()

    # Générer les notebooks
    generate_notebooks(args.input_path, args.exercise_output_path)

if __name__ == "__main__":
    main()

