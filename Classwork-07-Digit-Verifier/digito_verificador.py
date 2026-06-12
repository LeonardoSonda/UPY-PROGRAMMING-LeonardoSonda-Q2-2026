# ============================================================
# Classwork 08 - Digito Verificador UTFSM
# Author: Leonardo D.
# Universidad Politecnica de Yucatan - Q2 2026
# ============================================================

# -------------------------------------------------------
# INPUT
# -------------------------------------------------------
rol_input = input("Ingresa el rol UTFSM (sin guion ni digito verificador): ")

# -------------------------------------------------------
# PROCESS
# -------------------------------------------------------

# Step 1: Clean the input (remove hyphens/spaces just in case)
rol = rol_input.replace("-", "").replace(" ", "")

# Step 2: Reverse the number string
rol_invertido = rol[::-1]

# Step 3: Multiply each digit by the repeating sequence 2,3,4,5,6,7
sequence = [2, 3, 4, 5, 6, 7]
total = 0

for i, digit_char in enumerate(rol_invertido):
    digit = int(digit_char)
    multiplier = sequence[i % len(sequence)]  # cycle through 2-7
    total += digit * multiplier

# Step 4: Apply modulo 11
resto = total % 11

# Step 5: Subtract from 11
diferencia = 11 - resto

# Step 6: Determine the verification digit
# Special cases: if result is 11 -> digit is 0; if 10 -> digit is K
if diferencia == 11:
    digito_verificador = "0"
elif diferencia == 10:
    digito_verificador = "K"
else:
    digito_verificador = str(diferencia)

# -------------------------------------------------------
# OUTPUT
# -------------------------------------------------------
print(f"\n--- Resultado ---")
print(f"Rol ingresado  : {rol}")
print(f"Rol invertido  : {rol_invertido}")
print(f"Suma total     : {total}")
print(f"Modulo 11      : {total} % 11 = {resto}")
print(f"11 - {resto}         = {diferencia}")
print(f"Digito verificador: {digito_verificador}")
print(f"\nRol completo   : {rol}-{digito_verificador}")