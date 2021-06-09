import pandas as pd
import ast
from matplotlib import pyplot as plt
import seaborn as sns

df_books=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/top500booksWithGenres.csv")
df_genres=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/top15Genres.csv")

for index,row in df_books.iterrows():
    genreString=df_books.loc[index,'genre']
    df_books.at[index,'genre']=ast.literal_eval(genreString)



def getGenreCount(genre):
    genreCount=[0,0,0,0,0]
    for index, row in df_books.iterrows():
        if index<=100:
            genreCount[0]+=row['genre'].count(genre)
        if 100<index<=200:
            genreCount[1]+=row['genre'].count(genre)
        if 200<index<=300:
            genreCount[2]+=row['genre'].count(genre)
        if 300<index<=400:
            genreCount[3]+=row['genre'].count(genre)
        if index>400:
            genreCount[4]+=row['genre'].count(genre)
    return genreCount



genreCountDict={}
for index,row in df_genres.iterrows():
    genre=row['genre']
    genreCountDict[genre]=getGenreCount(genre)

heatMapDf=pd.DataFrame(genreCountDict,index=['top100','top 100-200','top 200-300','top 300-400','top 400-500'])
cmap = sns.light_palette("seagreen", as_cmap=True)
sns.heatmap(heatMapDf,cmap=cmap)
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/genresDistributionTop500")
plt.show()