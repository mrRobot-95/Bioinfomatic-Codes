from scipy import stats as st
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.gofplots import qqplot

#read to pd dataframe
df=pd.read_csv("HornedLizards.csv").dropna(axis=0)
survived = df.loc[(df['Survive'] == 'survived')]["Squamosal horn length"]
dead = df.loc[(df['Survive'] == 'dead')]["Squamosal horn length"]

#test statistics
groupby_Survive = df.describe()
print(groupby_Survive)


#histograms
plt.hist(survived, color='green')
plt.hist(dead, color='red')
plt.legend(['survived lizards', 'dead lizards'])
plt.title('Histograms of living and dead lizard horn lengths')
plt.show()

#qqplots
qqplot(survived)
plt.title('QQplot for horn length of horned of living horned lizards')
plt.show()


qqplot(dead)
plt.title('QQplot for horn length of horned of dead horned lizards')
plt.show()

#normality test for living lizrads
print("For survived lizrds")
p =st.shapiro(survived)
alpha = 0.05
if p[1] > alpha:
	print("p value of "+str(p[1]) +"is greater than alpha value therefore fail to reject H0")
else:
	print("p value of "+str(p[1]) +"is less than or equal to alpha value therefore reject H0")

# normality test for living lizrads
print("For dead lizrds")
p =st.shapiro(dead)
alpha = 0.05
if p[1] > alpha:
	print("p value of "+str(p[1]) +"is greater than alpha value therefore fail to reject H0")
else:
	print("p value of "+str(p[1]) +"is less than or equal to alpha value therefore reject H0")

#plotting box plots
f,(box1,box2)=plt.subplots(1,2,sharey=True)
box1.boxplot(survived)
box1.set_title("Boxplot of survived lizards horn length")
box2.boxplot(dead)
box2.set_title("Boxplot of dead lizards horn length")
plt.show()

#plotting Violin plots
f,(Violin1,Violin2)=plt.subplots(1,2,sharey=True)
Violin1.violinplot(survived)
Violin1.set_title("violin plot of survived lizards horn length")
Violin2.violinplot(dead)
Violin2.set_title("violin plot of dead lizards horn length")
plt.show()

# Carrying out non-parametric tests
print("Kruskal-Wallis H test")
result=st.kruskal(survived, dead)
alpha=0.05
print(result)
if result.pvalue > alpha:
	print("p-value of" +str(result[1])+" is greater than 0.05 therefore null hyphothesis is not rejected")
else:
	print("p-value of" + str(result[1]) + " is less than or equal to 0.05 therefore null hyphothesis is  rejected")

