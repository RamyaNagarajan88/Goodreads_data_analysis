import pandas as pd
import datetime

def convertDate(dateEntry):
    try:
        return datetime.datetime.strptime(dateEntry,'%m/%d/%Y').date()
    except:
        print(dateEntry)


df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/books.csv')
df['publication_date']=df['publication_date'].apply(convertDate)

max_index=df['text_reviews_count'].idxmax()
result=df.loc[max_index,['bookID','title','authors','average_rating','language_code','num_pages','text_reviews_count']]

print(result)



