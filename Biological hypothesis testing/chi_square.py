from scipy import stats as st
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.graphics.mosaicplot as mplot

#creating dataframe
fish = pd.DataFrame([[1,10,37],[49,35,9]],index=['eaten','not_eaten'],columns=['uninfected','lightly infected',
                                                                               'highly infected'])

print(fish)

#mosaic plot
mplot.mosaic(fish.stack())
plt.show()

#chi_Squre test
print("chi-squre test")
chi=st.chi2_contingency(fish)
print("Chi-square statistic:"+str(chi[0]))
print("p-value:"+str(chi[1]))
print("degree of freedom:"+str(chi[2]))

expected = pd.DataFrame(chi[3])
print(expected)
