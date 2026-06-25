# ============================================================
# Classwork 09 - Spanish Verb Conjugator
# Author: Leonardo Sonda
# Universidad Politecnica de Yucatan - Q2 2026
# ============================================================

# # INPUT
verbo = input("Ingrese verbo: ")

# # PROCESS

# List of pronouns (required structure)
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

# Dictionary of endings by verb type (required structure)
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Get stem (verb minus last 2 letters) and ending (last 2 letters)
stem    = verbo[:-2]
ending  = verbo[-2:]

# Look up the matching endings list in the dictionary
endings_list = terminaciones[ending]

# # OUTPUT

# Loop over pronouns and print conjugation using same index
for i in range(len(pronombres)):
    print(pronombres[i], stem + endings_list[i])