# ============================================================
# Classwork 15 - Sorting Algorithms: Bubble Sort Visualized
# Author: Leonardo Sonda
# Universidad Politecnica de Yucatan - Q2 2026
# AI use declaration: Claude para poner el sonido de la animación y la visualización de las barras.
# ============================================================

import random
import stddraw
import pygame
import numpy as np
from color import Color

# ── PROCESS: Sound setup ─────────────────────────────────────
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

def beep(freq=440, duration=100):
    sample_rate = 44100
    frames = int(duration * sample_rate / 1000)
    t = np.linspace(0, duration / 1000, frames, False)
    wave = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)
    wave = np.column_stack([wave, wave])
    sound = pygame.sndarray.make_sound(wave)
    sound.play()

# ── PROCESS: Draw bars ────────────────────────────────────────
def draw_bars(numbers, selected=(), phase='compare'):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n

    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2

        # Color por fase:
        # compare  → naranja  (par siendo comparado)
        # swap     → rojo     (par siendo intercambiado)
        # sorted   → verde    (ya ordenado / estado final)
        # default  → azul
        if i in selected:
            if phase == 'swap':
                color = Color(220, 50, 50)    # rojo
            elif phase == 'compare':
                color = Color(255, 165, 0)    # naranja
            elif phase == 'sorted':
                color = Color(50, 180, 50)    # verde
            else:
                color = Color(70, 130, 220)   # azul
        else:
            color = Color(70, 130, 220)       # azul default

        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)

    stddraw.show(400)   # 400 ms entre frames → más lento y visible

# ── PROCESS: Bubble Sort with animation and sound ─────────────
def bubble_sort_animated(numbers):
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    # Estado inicial en azul
    draw_bars(numbers)

    for sweep in range(n):
        swapped = False
        for pair in range(0, n - 1 - sweep):

            # Comparación → naranja + sonido agudo
            beep(freq=600, duration=80)
            draw_bars(numbers, selected=(pair, pair + 1), phase='compare')

            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                swapped = True

                # Swap → rojo + sonido grave
                beep(freq=300, duration=150)
                draw_bars(numbers, selected=(pair, pair + 1), phase='swap')

        # Fin de pass → último elemento en verde
        draw_bars(numbers, selected=(n - 1 - sweep,), phase='sorted')

        if not swapped:
            break

    # Final → todo verde
    for i in range(n):
        draw_bars(numbers, selected=tuple(range(i + 1)), phase='sorted')
        beep(freq=500 + i * 50, duration=60)

    stddraw.show()

# ── INPUT ─────────────────────────────────────────────────────
numbers = [random.randint(1, 100) for _ in range(10)]

# ── OUTPUT ────────────────────────────────────────────────────
print(f"Before bubble sort: {numbers}")
bubble_sort_animated(numbers)
print(f"After bubble sort:  {numbers}")