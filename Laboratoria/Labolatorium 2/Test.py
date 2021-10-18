import numpy as np
import main

r1 = np.linspace(0, 1)
r2 = np.linspace(0, 20, num=100)
x1 = (np.e ** r1) * np.cos(r1)
y1 = (np.e ** r1) * np.sin(r1)
x2 = (np.e ** r2) * np.cos(r2)
y2 = (np.e * r2) * np.sin(r2)

main.parallel_plot(x1, y1, x2, y2, 'x1', 'y1', 'x2', 'y2', 'subplot', '|')
main.parallel_plot(x1, y1, x2, y2, 'x1', 'y1', 'x2', 'y2', 'subplot', '-')
