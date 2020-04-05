import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

iris_data = pd.read_csv("c:/Users/iriscsv/Desktop/TechieNest/iris.csv")

iris_data = np.array(iris_data)
x = iris_data[:,0:4]
y = iris_data[:,4]

print(np.shape(x),np.shape(y))
neigh = KNeighborsClassifier(n_neighbors=5)

trained = neigh.fit(x,y)
y_pred1 = trained.predict(x)
y_pred2 = trained,predict([[2.3,4.5,5.5,1.0]])

print("y:",y)
print("y_pred1:",y_pred1)
