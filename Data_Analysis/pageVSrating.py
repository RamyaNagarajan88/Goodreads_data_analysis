import pandas as pd
from matplotlib import pyplot as plt

def createScatterPlots(bookType):
    fileName=bookType+"Booksdetails.csv"
    imageFileName='pageVSrating'+bookType+'Books'

    df=pd.read_csv("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data/"+fileName)
    pages=df['pages'].apply(lambda x: int(x))
    ratings=df['rating']

    plt.scatter(ratings,pages)
    plt.xlim(1,4.8)
    plt.ylim(0,4000)
    plt.title("Distribution of pages by ratings")
    plt.xlabel('ratings')
    plt.ylabel('number of pages')
    plt.savefig("E:/Ramya/brushUps/Basics/CASE_STUDIES/GOOD_READS/Data_Analysis/AnalysisPlots/"+imageFileName,bbox_inches='tight')
    plt.tight_layout()
    plt.show()

booksTypes=['best','worst']
for booktype in booksTypes:
    createScatterPlots(booktype)


