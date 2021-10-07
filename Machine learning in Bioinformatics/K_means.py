import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

#reading data from pandas
iris=pd.read_csv('iris.csv')
#define label column
df2=iris['v_short']
print(df2)
#add sepal data frame to columns
df=pd.DataFrame(iris,columns=['sepal.length','sepal.width'])
df3=pd.DataFrame(iris,columns=['v_short'])
print(df)
#Kmeans test
kmeans= KMeans(n_clusters=3).fit(df)
#getting cetroids
centrodis=kmeans.cluster_centers_

#specise unknown data sample
plant=np.array([[4.6, 3.0, 1.5, 0.2],[6.2, 3.0,4.1,1.2]])
X = plant[:, [0, 1]]


predicted=kmeans.predict(X)
print(predicted)
#define labels
labels=kmeans.labels_

#scatter plot of sepal length ,sepal width ,unknown saple data with cetroids
plt.scatter(df['sepal.length'],df['sepal.width'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(X[:,0],X[:,1],c='green',s=50)
plt.scatter(centrodis[:,0],centrodis[:,1],c='red',s=50)

#annotation
for df2, x, y,z in zip(df2, df.iloc[:, 0], df.iloc[:, 1],df3.iloc[:,0]):
    if z=='s':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(-50, 50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3',fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle = '->', connectionstyle="arc,rad=40",alpha=0.2))
    if z == 've':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(50, -50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3', fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle='->', connectionstyle="arc,rad=40", alpha=0.2))
    if z == 'vi':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(50, 50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3', fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle='->', connectionstyle="arc,rad=40", alpha=0.2))
#label annotation
for label, x, y in zip(labels, df.iloc[:, 0], df.iloc[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        textcoords='offset points'

       )
plt.show()

print("for the petals data")
#define label collumns
df2=iris['v_short']

##add petal data frame to columns
df3=pd.DataFrame(iris,columns=['petal.length','petal.width'])
df4=pd.DataFrame(iris,columns=['v_short'])

#kmeans test fo petal
kmeans = KMeans(n_clusters=3, random_state=0).fit(df3)

#getting cetroids
centrodis=kmeans.cluster_centers_
predicted=kmeans.predict(X)
print(predicted)

#define labels
labels=kmeans.labels_

#unknown sample petal data
X = plant[:, [2, 3]]

#scatter plot of petal length ,petal width ,unknown saple data with cetroids
plt.scatter(df3['petal.length'],df3['petal.width'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(X[:,0],X[:,1],c='green',s=50)
plt.scatter(centrodis[:,0],centrodis[:,1],c='red',s=50)

#annotation
for df2, x, y,z in zip(df2, df3.iloc[:, 0], df3.iloc[:,1],df4.iloc[:,0]):
    if z=='s':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(-50, 50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3',fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle = '->', connectionstyle="arc,rad=40",alpha=0.2))
    if z == 've':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(50, -50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3', fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle='->', connectionstyle="arc,rad=40", alpha=0.2))
    if z == 'vi':
        plt.annotate(
            df2,
            xy=(x, y), xytext=(50, 50),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='circle,pad=0.3', fc="white", alpha=0.2),
            arrowprops=dict(arrowstyle='->', connectionstyle="arc,rad=40", alpha=0.2))
#annotation
for label, x, y in zip(labels, df3.iloc[:, 0], df3.iloc[:, 1]):
    plt.annotate(
        label,
        xy=(x, y),
        textcoords='offset points')

plt.show()
