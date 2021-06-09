import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np

df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/bestBooksdetails.csv")

booksCount=df['year'].value_counts(sort=False)
booksYearWise=df.groupby(['year'])
averagePages=booksYearWise['pages'].mean()
booksPages_df=pd.concat([booksCount,averagePages],axis=1)
booksPages_df.rename(columns={'year':'totalBooks'},inplace=True)

totalbooksArray=booksPages_df['totalBooks'].values.astype(int)
averagepgsArray=booksPages_df['pages'].values.round(3)

ss=StandardScaler()
scaled_totalbooks=(ss.fit_transform(totalbooksArray.reshape(-1, 1)).flatten()).tolist()
scaled_averagepgs=(ss.fit_transform(averagepgsArray.reshape(-1, 1)).flatten()).tolist()

years=[]
for index,row in booksPages_df.iterrows():
    years.append(index)


plt.plot(years,scaled_averagepgs,label='Average number of pages')
plt.bar(years,scaled_totalbooks,label='Number of books')
plt.xlim(1950,2010)
plt.ylim(0,4)
plt.legend()
plt.tight_layout()
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/pgsBooksVsYear")
plt.show()
