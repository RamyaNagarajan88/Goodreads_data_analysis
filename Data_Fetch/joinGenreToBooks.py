import pandas as pd
import ast

df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/completebooks.csv')
df_genres=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/booksGenresFind.csv')


df = df.assign(genre=df_genres['genre'])

df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/books.csv',index=False)