import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

n = np.linspace(1, 100, 400)
k = 3

# Define time complexity functions
complexities = {
    "O(1)": lambda n: np.ones_like(n),
    "O(log n)": lambda n: np.log2(n),
    "O(n)": lambda n: n,
    "O(n log n)": lambda n: n * np.log2(n),
    "O(n^2)": lambda n: n**2,
    "O(n^k)": lambda n: n**k,
}

# Set up the plot
fig, ax = plt.subplots()
lines = {name: ax.plot([], [], label=name)[0] for name in complexities}
ax.set_xlim(0, 100)
ax.set_ylim(0, 10000)
ax.set_xlabel("n (Input Size)")
ax.set_ylabel("Operations")
ax.set_title("Time Complexity Curves")
ax.legend()

# Initialization function
def init():
    for line in lines.values():
        line.set_data([], [])
    return lines.values()

# Animation function
def animate(i):
    x = n[:i]
    for name, func in complexities.items():
        y = func(x)
        lines[name].set_data(x, y)
    return lines.values()

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(n),
                              interval=20, blit=True, repeat=False)

plt.show()