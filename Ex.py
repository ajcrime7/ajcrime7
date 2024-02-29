import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris  # Example UCI dataset

# Load example UCI dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# a) Normal values
sns.histplot(df['sepal length (cm)'], kde=False)
plt.title('Histogram for Normal Values')
plt.show()

# b) Density and contour plots
sns.kdeplot(df['sepal length (cm)'], df['sepal width (cm)'], fill=True, cmap="Blues", levels=5)
plt.title('Density and Contour Plot')
plt.show()

# c) Three-dimensional plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['sepal length (cm)'], df['sepal width (cm)'], df['petal length (cm)'], c='r', marker='o')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.set_zlabel('Petal Length (cm)')
plt.title('Three-Dimensional Plotting')
plt.show()
