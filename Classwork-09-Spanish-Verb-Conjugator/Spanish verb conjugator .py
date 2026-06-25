# ============================================================
# Classwork 09 - Spanish Verb Conjugator
# Author: Leonardo Sonda
# Universidad Politecnica de Yucatan - Q2 2026
# ============================================================

# # INPUT
verb = input("Enter verb: ")

# # PROCESS

# List of pronouns (required structure)
pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

# Dictionary of endings by verb type (required structure)
endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Get stem (verb minus last 2 letters) and ending (last 2 letters)
stem   = verb[:-2]
ending = verb[-2:]

# Look up the matching endings list in the dictionary
endings_list = endings[ending]

# # OUTPUT

# Loop over pronouns and print conjugation using enumerate
for index, pronombre in enumerate(pronouns):
    terminacion = endings_list[index]
    print(f"{pronombre} {stem}{terminacion}")