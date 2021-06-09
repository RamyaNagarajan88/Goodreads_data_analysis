import pandas as pd
import ast
import collections
from matplotlib import pyplot as plt
import csv

df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/books.csv')
df.sort_values(by='average_rating',inplace=True,ascending=False)
df=df.reset_index(drop=True)

df_genred=df.loc[(df['genre'].str.len())>2]
df_top=df_genred.iloc[:500]
df_top=df_top.reset_index(drop=True)

for index,row in df_top.iterrows():
    genreString=df_top.loc[index,'genre']
    df_top.at[index,'genre']=ast.literal_eval(genreString)


count=collections.Counter()

for bookid,row in df_top.iterrows():
    count.update(row['genre'])

topGenres=count.most_common(15)

labels,counts=[],[]

for genres in topGenres:    
    labels.append(genres[0])
    counts.append(genres[1])


plt.bar(labels,counts)
plt.title("most common genres among top 500")
plt.ylabel("frequency")
plt.tight_layout()
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/topGenresTop500Books")
plt.show()

df_top.to_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/top500booksWithGenres.csv",index=False)
with open("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/top15GenresTopBooks.csv",'w',newline="") as wf:
    wf.write('genre')
    wf.write("\n")
    for genre in labels:
        wf.write(genre)
        wf.write("\n")





