import pandas as pd
import csv
import datetime



with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/raw_data_books.csv','r',encoding="utf8") as readFile:
    csv_dict=csv.DictReader(readFile)
    columns=[]
    col_count=0
    booksList=[]
    #for collecting column names and columns count
    for book in csv_dict:
        columns=list(book.keys())
        col_count=len(columns)
        break
    #for reassigning columns with their respective values    
    for book in csv_dict:
        if len(book)>col_count:
            book['authors']=book['authors']+book['average_rating']
            for col in range(3,(col_count-1)):
                book[columns[col]]=book[columns[col+1]]
            book[columns[col_count-1]]=book[None]
            del book[None]

        if book['bookID']=='31373':
            book['publication_date']='10/31/2000'

        if book['bookID']=='45531':
            book['publication_date']='6/1/1982'
                    
        booksList.append(book)

    df=pd.DataFrame(booksList)
    df['bookID']=df['bookID'].astype(int)
    df['average_rating']=df['average_rating'].astype(float)
    df['isbn13']=df['isbn13'].apply(lambda x:int(x))
    df.rename(columns={'  num_pages':'num_pages'},inplace=True)
    df['num_pages']=df['num_pages'].astype(int)
    df['ratings_count']=df['ratings_count'].astype(int)
    df['text_reviews_count']=df['text_reviews_count'].astype(int)
    

    df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/data_books.csv',sep=',',index=False)

         

