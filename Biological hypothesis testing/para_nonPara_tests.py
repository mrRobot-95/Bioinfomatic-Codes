from scipy import stats as st
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.gofplots import qqplot

df=pd.read_csv("BlackbirdTestosterone.csv")
birds=pd.DataFrame(df,columns=['log before', 'log after', 'dif in logs'])
before= df['log before']
after= df['log after']
difference= df['dif in logs']

groupby_Survive = birds.describe()
print(groupby_Survive)

#plotting histograms
f,(hist1,hist2,hist3)=plt.subplots(1,3,sharey=True)
hist1.hist(before)
hist2.hist(after)
hist3.hist(difference)
plt.show()

#qq_plots
qqplot(before)
plt.title('QQplot for log before antibody production')
plt.show()


qqplot(after)
plt.title('QQplot for log after antibody production')
plt.show()

qqplot(difference)
plt.title('QQplot for log differnce antibody production')
plt.show()

#normality test
print("for log before value")
test=st.shapiro(before)
alpha=0.05
if test[1] < alpha:
    print("p value of "+str(test[1]) +"is greater than alpha value therefore fail to reject H0")
else:
    print("p value of " + str(test[1]) + "is less than or equal to alpha value therefore  reject H0")

print("for log after value")
test=st.shapiro(after)
alpha=0.05
if test[1] < alpha:
    print("p value of "+str(test[1]) +"is greater than alpha value therefore fail to reject H0")
else:
    print("p value of " + str(test[1]) + "is less than or equal to alpha value therefore  reject H0")

print("for log difference value")
test=st.shapiro(difference)
alpha=0.05
if test[1] < alpha:
    print("p value of "+str(test[1]) +"is greater than alpha value therefore fail to reject H0")
else:
    print("p value of " + str(test[1]) + "is less than or equal to alpha value therefore  reject H0")

#plotting box plots
f,(box1,box2,box3)=plt.subplots(1,3,sharey=True)
box1.boxplot(before)
box1.set_title("Boxplot of log after")
box2.boxplot(after)
box2.set_title("Boxplot of log before")
box3.boxplot(difference)
box3.set_title("Boxplot of log difference")
plt.show()


#plotting Violin plots
f,(Violin1,Violin2,Violin3)=plt.subplots(1,3,sharey=True)
Violin1.violinplot(before)
Violin1.set_title("violin plot of log before")
Violin2.violinplot(after)
Violin2.set_title("violin plot of log after")
Violin3.violinplot(difference)
Violin3.set_title("violin plot of log difference")
plt.show()

# Carrying out non-parametric tests
print("Kruskal-Wallis H test")
result=st.kruskal(before, after)
print(result)
alpha=0.05
if result.pvalue > alpha:
	print("p-value of" +str(result[1])+" is greater than 0.05 therefore null hyphothesis is not rejected")
else:
	print("p-value of" + str(result[1]) + " is less than or equal to 0.05 therefore null hyphothesis is  rejected")
