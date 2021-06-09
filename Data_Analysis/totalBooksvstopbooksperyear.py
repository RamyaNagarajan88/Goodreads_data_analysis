import pandas as pd
from matplotlib import pyplot as plt

totalBooks={2002:247777,2003:266322,2004:295523,2005:282500,2006:296352,2007:407646,2008:561580,2009:1335475, 
2010:4152906,2011:1608751,2012:2352797,2013:1413095}

df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/bestBooksdetails.csv")
df['year']=df['year'].apply(lambda x: int(x))
yearFilterout=(df['year']<2002) | (df['year']>2013)
df.drop(df[yearFilterout].index,inplace=True)
bookscountYearwise=df['year'].value_counts()
bookscountTopList={}

for year in totalBooks.keys():
    bookscountTopList[year]=bookscountYearwise[year]

totalbooksvsinTop_df=pd.DataFrame()

totalbooksvsinTop_df['year']=totalBooks.keys()
totalbooksvsinTop_df['totalBooks']=totalBooks.values()
totalbooksvsinTop_df['booksCountinTop']=bookscountTopList.values()
totalbooksvsinTop_df['ratioPercent']=(totalbooksvsinTop_df['booksCountinTop']/totalbooksvsinTop_df['totalBooks'])*100

plt.scatter(totalbooksvsinTop_df['totalBooks'],totalbooksvsinTop_df['booksCountinTop'])
plt.xlabel("# of books sold in a year")
plt.ylabel("number of books in top 500")
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/totalbooksvstopbooksperyear")
plt.show()
