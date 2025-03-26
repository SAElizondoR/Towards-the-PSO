import numpy as np
import matplotlib.pyplot as plt
import pyswarms as ps
import matplotlib.animation as animation

# Definición de la función Rastrigin
def rastrigin(X):
    A = 10
    return A * X.shape[1] + np.sum(X**2 - A * np.cos(2 * np.pi * X), axis=1)

# Parámetros de configuración
n_particles, dimensions, iters = 30, 2, 300
bounds = np.array([[-5.12, -5.12], [5.12, 5.12]])

# Configuración de PSO
phi, c1, c2 = 4.1, 2.05, 2.05
chi = 2.0 / (phi - 2 + np.sqrt(phi**2 - 4 * phi))
options = {'c1': 1.5, 'c2': 1.5, 'w': 0.9}
options_constr = {'c1': c1, 'c2': c2, 'w': chi}

# Optimización
optimizer_no_constr = ps.single.GlobalBestPSO(n_particles, dimensions, options, bounds)
cost_no_constr, pos_no_constr = optimizer_no_constr.optimize(rastrigin, iters, verbose=False)
optimizer_constr = ps.single.GlobalBestPSO(n_particles, dimensions, options_constr, bounds)
cost_constr, pos_constr = optimizer_constr.optimize(rastrigin, iters, verbose=False)

# Contorno de la función Rastrigin
x, y = np.linspace(bounds[0][0], bounds[1][0], 400), np.linspace(bounds[0][1], bounds[1][1], 400)
X, Y = np.meshgrid(x, y)
Z = rastrigin(np.column_stack((X.ravel(), Y.ravel()))).reshape(X.shape)

# Creación de gráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, title in zip(axes, ["Sin Constricción", "Con Constricción"]):
    ax.contourf(X, Y, Z, levels=50, cmap='viridis', alpha=0.7)
    ax.set(xlim=(bounds[0][0], bounds[1][0]), ylim=(bounds[0][1], bounds[1][1]), xlabel="Eje X", ylabel="Eje Y", title=title)
scat1, scat2 = axes[0].scatter([], [], c='white', edgecolors='k', s=80), axes[1].scatter([], [], c='white', edgecolors='k', s=80)

# Animación
def update(frame):
    scat1.set_offsets(optimizer_no_constr.pos_history[frame])
    scat2.set_offsets(optimizer_constr.pos_history[frame])
    fig.suptitle(f"Iteración {frame}", fontsize=16, fontweight='bold')
    return scat1, scat2

ani = animation.FuncAnimation(fig, update, frames=iters, interval=200, blit=True)
ani.save("comparacion_pso.gif", writer='pillow', dpi=100)
plt.show()

# Gráfico de convergencia
plt.figure(figsize=(10, 6))
plt.plot(optimizer_no_constr.cost_history, label='Sin Constricción', linewidth=2)
plt.plot(optimizer_constr.cost_history, label='Con Constricción', linewidth=2)
plt.xlabel('Iteraciones', fontsize=14)
plt.ylabel('Fitness (Valor de Rastrigin)', fontsize=14)
plt.title('Convergencia del PSO con y sin Factor de Constricción', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("comparacion_convergencia.png", dpi=300)
plt.show()
