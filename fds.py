import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load UCI dataset (replace 'your_dataset.csv' with the actual file name)
df = pd.read_csv('your_dataset.csv')

# a) Normal values
sns.histplot(df['your_column'], kde=False)
plt.title('Histogram for Normal Values')
plt.show()

# b) Density and contour plots
sns.kdeplot(df['column_1'], df['column_2'], fill=True, cmap="Blues", levels=5)
plt.title('Density and Contour Plot')
plt.show()

# c) Three-dimensional plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x'], df['y'], df['z'], c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title('Three-Dimensional Plotting')
plt.show()
