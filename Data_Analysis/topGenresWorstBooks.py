import pandas as pd
import ast
import collections
from matplotlib import pyplot as plt
import csv

df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/worstBooksdetails.csv")

df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1,inplace=True)
 
for index,row in df.iterrows():
    genreString=df.loc[index,'genres']
    df.at[index,'genres']=ast.literal_eval(genreString)

count=collections.Counter()

for bookid,row in df.iterrows():
    count.update(row['genres'])

topGenres=count.most_common(15)

labels,percents=[],[]

for genres in topGenres:    
    labels.append(genres[0])
    percents.append((genres[1]/5692)*100)


plt.bar(labels,percents)
plt.title("most common genres among worst 5692 books")
plt.ylabel("percentage of books")
plt.tight_layout()
plt.xticks(rotation='vertical')
plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/topGenresWorstBooks",bbox_inches='tight')
plt.show()

with open("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/top15GenresWorstBooks.csv",'w',newline="") as wf:
    wf.write('genres')
    wf.write("\n")
    for genre in labels:
        wf.write(genre)
        wf.write("\n")





