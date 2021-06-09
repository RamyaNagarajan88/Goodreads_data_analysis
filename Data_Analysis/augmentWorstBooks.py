import pandas as pd

df_1=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/WorstBooks.csv")
df_2=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/tempWorstBooks.csv")
df_2.columns=list(df_1.columns)

empty_df_2=df_2.groupby(['title']).get_group('0')

for index,row in empty_df_2.iterrows():
    df_2.drop(index,inplace=True)

df_1.update(df_2,overwrite=True)

empty_df_1=df_1.groupby(['title']).get_group('0')


for index,row in empty_df_1.iterrows():
    df_1.drop(index,inplace=True)

df_1.to_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/worstBooksdetails.csv")





