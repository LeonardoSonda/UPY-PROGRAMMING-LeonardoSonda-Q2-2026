# ============================================================
# Classwork 08 - Numerical Integration
# Author: Leonardo Sonda
# Universidad Politecnica de Yucatan - Q2 2026

# ============================================================

import math

# ── INPUT ────────────────────────────────────────────────────
a     = input("Write the left endpoint of the interval: ")
b     = input("Write the right endpoint of the interval: ")
f_x   = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")

# ── PROCESS ──────────────────────────────────────────────────

# Convert endpoints (support "pi" input)
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)

n        = 1000
h        = (b - a) / n
area     = 0.0
constant = 0      # midpoint offset
shift    = 0      # index start for RRM

if method == "RRM":
    shift = 1

if method == "MRM":
    constant = h / 2

if method == "TRAP":
    # Trapezoidal rule
    f_0   = f_x.replace("x", str(a))
    area += (h / 2) * eval(f_0)

    for i in range(1, n):
        xi   = a + i * h
        f_xi = f_x.replace("x", str(xi))
        area += (h / 2) * 2 * eval(f_xi)

    f_xn  = f_x.replace("x", str(b))
    area += (h / 2) * eval(f_xn)

else:
    # Left / Right / Midpoint Riemann sum
    for i in range(shift, n + shift):
        xi     = a + i * h
        height = f_x.replace("x", str(xi + constant))
        area  += h * eval(height)

# ── OUTPUT ───────────────────────────────────────────────────
print(f"The integration of {f_x} is {area}")