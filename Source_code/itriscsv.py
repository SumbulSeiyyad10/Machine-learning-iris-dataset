import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv("c:/Users/user/Desktop/itris.csv")
b= np.array(a["sepal length"])
c= np.array(a["petal length"])
d= np.array(a["sepal width"])
e= np.array(a["petal width"])

plt.scatter(b,c,color="blue")
plt.scatter(d,e,color="red",marker="*")
plt.title("graph between sepal and petal length")
plt.xlabel("sepal")
plt.ylabel("petal")
plt.legend(["length","width"])
plt.show()

