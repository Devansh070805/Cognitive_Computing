import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

print(gfg.sum())
print(gfg.sum(axis=1))
print(gfg.sum(axis=0))
