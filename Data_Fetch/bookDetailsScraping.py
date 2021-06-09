import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time

def getTitle(soup):
    try:
        title =(soup.find('h1',id='bookTitle').text).strip()+(soup.find('h2',id='bookSeries').text).strip()
        return title
    except:
        return str(0)


def getAuthor(soup):
    try: 
        author=(soup.find('a',class_='authorName').text).strip()
        return author
    except:
        return str(0)

def getRating(soup):
    try: 
        rating=(soup.find('span', itemprop='ratingValue').text).strip()
        return rating
    except:
        return str(0)

def getRatingReviewCount(soup):
    try: 
        ratingreviewList=(soup.find('div',class_='reviewControls--left greyText').text).split("\n")
        ratingCount=int(ratingreviewList[2].lstrip().replace(',',''))
        reviewCount=int(ratingreviewList[5].lstrip().replace(',',''))
        return ratingCount,reviewCount
    except:
        return str(0),str(0)

def getPages(soup):
    try: 
        pages=int((soup.find('span',itemprop='numberOfPages').text).strip().split(' ')[0])
        return pages
    except:
        return str(0)


def getPublicationYear(soup):
    try: 
        publicationDetails=soup.findAll('div',class_='row')
        publicationYear=publicationDetails[1].text.strip().split("\n")[1].split(" ")[-1]
        if publicationYear=='':
            publicationDetails=soup.find('nobr',class_='greyText').text
            publicationYear=publicationDetails.strip().split(' ')[3].strip(')')
        
        return publicationYear
    except:
        return str(0)

def getDescription(soup):
    try: 
        description=(soup.find('div',id='description').text).strip("").split("\n")[2]
        return description
    except:
        return str(0)

def getReviews(soup):
    try: 
        reviews=soup.findAll('div',class_='reviewText stacked')
        reviews[:]=[r.text for r in reviews]
        return reviews
    except:
        return str(0) 

def getGenres(soup):
    try: 
        bookGenres=set()
        for genre in soup.findAll('a',class_='actionLinkLite bookPageGenreLink'):
            bookGenres.add(genre.text)
        return list(bookGenres)
    except:
        return str(0) 


def getBookDetails(bookID):
    book={}
    source='https://www.goodreads.com/book/show/'+str(bookID)
    page=requests.get(source).text
    soup=BeautifulSoup(page,'lxml')
    book['bookID']=bookID
    book['title']=getTitle(soup)
    book['author']=getAuthor(soup)
    book['rating']=getRating(soup)
    book['ratingCount'],book['reviewCount']=getRatingReviewCount(soup)
    book['pages']=getPages(soup)
    book['year']=getPublicationYear(soup)
    book['description']=getDescription(soup)
    book['reviews']=getReviews(soup)
    book['genres']=getGenres(soup)
   
    return book


#for first time
# with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/worstBooksList.csv','r') as rf:
#     books=[]
#     csv_reader=csv.reader(rf)
#     next(csv_reader)
#     for row in csv_reader:
#         books.append(getBookDetails(int(row[1])))
#         time.sleep(10)
#         print(row[0])
    
#     df=pd.DataFrame(books)
#     df.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/WorstBooks.csv')

#for filling missing enteries
booksdf=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/WorstBooks.csv')
with open ('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/tempWorstBooks.csv',"w",encoding="utf-8") as wf:
    csv_writer=csv.writer(wf)
    emptyRows=len(booksdf)

    while(emptyRows>0):
    
        for index,row in booksdf.iterrows():

            if row['title']=='0':
            
                bookDetails=getBookDetails(int(row['bookID']))
                booksdf.at[index,'title']=bookDetails['title']
                booksdf.at[index,'author']=bookDetails['author']
                booksdf.at[index,'rating']=bookDetails['rating']
                booksdf.at[index,'ratingCount'],booksdf.at[index,'reviewCount']=bookDetails['ratingCount'],bookDetails['reviewCount']
                booksdf.at[index,'pages']=bookDetails['pages']
                booksdf.at[index,'year']=bookDetails['year']
                booksdf.at[index,'description']=bookDetails['description']
                booksdf.at[index,'reviews']=bookDetails['reviews']
                booksdf.at[index,'genres']=bookDetails['genres']
                print(row['bookID'])
                time.sleep(10)
            csv_writer.writerow(booksdf.loc[index])

        emptyRows=len(booksdf.loc[booksdf['title']=='0'])
        print("empty rows count",emptyRows)
        time.sleep(20)

booksdf.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/worstBooksdetails.csv')










    
