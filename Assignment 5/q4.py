import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y1 = x**2
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="sin(x)")
plt.plot(x, y3, label="exp(x)")
plt.plot(x, y4, label="log(|x|+1)")

plt.title("Function Plots")
plt.xlabel("x values")
plt.ylabel("y values")
plt.legend()
plt.grid(True)
plt.show()
