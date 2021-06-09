import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/bestBooksdetails.csv")
# print(df[['title','bookID']].head(5))
#print(df.loc[:,['title','bookID']].head(5))
plt.hist(df['rating'])
plt.show()