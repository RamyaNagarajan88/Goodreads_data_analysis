import pandas as pd
from bs4 import BeautifulSoup
import lxml
import requests

def getBookIDS():
    bookIDS=[]
    for pageNo in range(1,75):
        try:
            source='https://www.goodreads.com/list/show/2.The_Worst_Books_of_All_Time?page='+str(pageNo)
            page=requests.get(source).text
            soup=BeautifulSoup(page,'lxml')         

            for bookTitle in soup.findAll('a',class_='bookTitle'):
                bookHref=bookTitle['href'].split('/')[3]
                bookid=bookHref.replace('.','-').split('-')[0]
                bookIDS.append(int(bookid))
            
        
        except:
            pass
        print(pageNo)
    return bookIDS

df=pd.DataFrame(getBookIDS(),columns=['bookIDS'])
df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/worstBooksList.csv')