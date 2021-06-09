import pandas as pd

df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/GenresFind/completeFinds.csv')
df_fullList=pd.DataFrame()
df_fullList=df.loc[:,['bookID','genre']]
df_fullList.set_index('bookID',inplace=True)

def mergeDataFrames(toMergeDf):
    df_fullList.update(toMergeDf,overwrite=True)

def createDataFrames(fileName):
    toMergeDf=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/'+fileName)
    toMergeDf.set_index('bookID',inplace=True)
    return toMergeDf

for fileNo in range(5,59):
    fileName='newGenreFinds_'+str(fileNo)+'.csv'
    toMergeDf=createDataFrames(fileName)
    mergeDataFrames(toMergeDf)

df_fullList.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/booksGenresFind.csv',index=True)









