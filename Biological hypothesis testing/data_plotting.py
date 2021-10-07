from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.graphics.gofplots import qqplot

df1= pd.read_csv("Temperature.csv")
print(df1.describe())

fig,ax=plt.subplots(figsize=(12,4))
sns.histplot(df1,ax=ax)
print(plt.show())

qqplot(df1['temperature'],line='s')
plt.title('QQplot')
print(plt.show())

stat, p=stats.shapiro(df1)
print(p)

chekvalue = 98.6
t,p=stats.ttest_1samp(df1,chekvalue)
print(p)
