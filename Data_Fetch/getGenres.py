import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import time
import csv



def getBookGenre(bookId):
    bookGenres=[]
    try:
        source='https://www.goodreads.com/book/show/'+str(bookId)
        page=requests.get(source).text
        soup=BeautifulSoup(page,'lxml')
        
        for genre in soup.findAll('a',class_='actionLinkLite bookPageGenreLink'):
            bookGenres.append(genre.text)
        
    except:
        pass
    
    return bookGenres

'''making first set'''

# df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/data_books.csv')
# df.set_index('bookID',inplace=True)
# df['genre']=''
# for rowIndex,row in df.iterrows():
#     df.at[rowIndex,'genre']=getBookGenre(rowIndex)
#     print(rowIndex)
#     #time.sleep(0.25)

# df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/completebooks.csv',sep=',',index=False)   

'''filling missing enteries'''


def emptyGenre(fileName):
    with open(fileName,'r',encoding="utf8") as rf:
        bookNoGenre=[]
        csv_dict=csv.DictReader(rf)
        for book in csv_dict:
            if len(book['genre'])==2:
                bookNoGenre.append(book['bookID'])
        return bookNoGenre
 

for fileNo in range(50,70):

    newFinds={}
    missingIDS=emptyGenre('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/GenresFind/newGenreFinds_'+str(fileNo)+'.csv')
    missingGenre=[]

    for book in missingIDS:
        missingGenre.append(getBookGenre(int(book)))
        print(book)
        time.sleep(15)
        
    
    newFindDict={'bookID':missingIDS,'genre':missingGenre}
    df=pd.DataFrame(newFindDict)
    df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/GenresFind/newGenreFinds_'+str(fileNo+1)+'.csv',sep=',',index=False)
    

 