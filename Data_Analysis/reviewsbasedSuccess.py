import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/bestBooksdetails.csv")
cat_1=df.loc[0:99,'reviewCount']
cat_2=df.loc[100:199,'reviewCount']
cat_3=df.loc[200:299,'reviewCount']
cat_4=df.loc[300:399,'reviewCount']
cat_5=df.loc[400:499,'reviewCount']

y=['Top 100','Top 100-200','Top 200-300','Top 300-400','Top 400-500']
x=[cat_1,cat_2,cat_3,cat_4,cat_5]
plt.boxplot(x,patch_artist=True,labels=y)
plt.tight_layout
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/reviewsbasedSuccess")
plt.show()

