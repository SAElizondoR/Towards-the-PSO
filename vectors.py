import matplotlib.pyplot as plt
import numpy as np

# Definir el origen y los vectores
origin = np.array([0, 0])
v_inercia = np.array([2.0, 0.0])
v_cognitivo = np.array([1.0, 2.0])
v_social = np.array([2.0, -1.0])
v_total = v_inercia + v_cognitivo + v_social  # Suma de los vectores

# Configuración de la figura
plt.figure(figsize=(8, 6))

# Graficar cada vector con plt.quiver
plt.quiver(*origin, *v_inercia, angles='xy', scale_units='xy', scale=1, color='blue', width=0.005, label=r'$w \cdot \vec{v}_i^n$')
plt.quiver(*origin, *v_cognitivo, angles='xy', scale_units='xy', scale=1, color='red', width=0.005, label=r'$c_1 r_1 (\vec{p}_i-\vec{x}_i^n)$')
plt.quiver(*origin, *v_social, angles='xy', scale_units='xy', scale=1, color='green', width=0.005, label=r'$c_2 r_2 (\vec{g}-\vec{x}_i^n)$')
plt.quiver(*origin, *v_total, angles='xy', scale_units='xy', scale=1, color='purple', width=0.005, label=r'$\vec{v}_i^{n+1}$')

# Establecer límites de los ejes
plt.xlim(-1, 6)
plt.ylim(-4, 4)

# Dibujar ejes y cuadrícula
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)

# Anotaciones para cada vector (se colocan en la mitad de cada vector)
plt.text(v_inercia[0] / 2, v_inercia[1] / 2 - 0.3, r'$w \cdot \vec{v}_i^n$', color='blue', fontsize=12)
plt.text(v_cognitivo[0] / 2, v_cognitivo[1] / 2 + 0.3, r'$c_1 r_1 (\vec{p}_i-\vec{x}_i^n)$', color='red', fontsize=12)
plt.text(v_social[0] / 2, v_social[1] / 2 - 0.5, r'$c_2 r_2 (\vec{g}-\vec{x}_i^n)$', color='green', fontsize=12)
plt.text(v_total[0] / 2, v_total[1] / 2 + 0.3, r'$\vec{v}_i^{n+1}$', color='purple', fontsize=12)

# Título, etiquetas y leyenda
plt.title("Combinación de Vectores en PSO", fontsize=16)
plt.xlabel("Eje X", fontsize=14)
plt.ylabel("Eje Y", fontsize=14)
plt.legend(loc='upper left')

plt.show()
