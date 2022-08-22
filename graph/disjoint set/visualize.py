import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt


grid1 = [[1,1,0,1,0,1,1,1],[0,1,1,1,1,0,1,1],[1,1,1,1,0,1,0,1],[1,1,1,0,1,1,1,1],[1,1,1,1,0,1,1,0],[1,1,1,1,0,1,0,0],[1,0,1,1,1,1,0,0],[1,0,0,1,1,1,1,1]]
grid2 = [[1,1,1,1,0,0,0,0],[0,1,1,1,0,0,1,1],[1,1,1,1,0,1,1,1],[1,1,0,1,1,1,1,0],[1,0,0,1,0,1,1,1],[1,1,0,1,1,1,1,0],[1,0,1,0,1,1,1,1],[1,1,1,1,1,0,1,1]]


# t = np.arange(len(grid1))


# plt.figure(1)
# plt.subplot(211)
# plt.imshow(grid1)
# plt.subplot(212)
# plt.imshow(grid2)
# plt.show()

fig, axes = plt.subplots(1, 2)

m,n = len(grid1), len(grid1[0])
df_cm1 = pd.DataFrame(grid1, range(m), range(n))
df_cm2 = pd.DataFrame(grid2, range(m), range(n))
# plt.figure(figsize=(10,7))
sn.set(font_scale=1.4) # for label size
sn.heatmap(df_cm1, annot=True, annot_kws={"size": 16},ax=axes[0],center=0) # font size
sn.heatmap(df_cm2, annot=True, annot_kws={"size": 16},ax=axes[1],center=0) # font size

plt.show()