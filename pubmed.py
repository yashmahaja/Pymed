import pandas as pd
from pymed import PubMed
pubmed = PubMed(tool="Yash", email="a@a.com")

max_result = int(input("\nEnter the no. of results you want: "))
search_term = input("\nEnter The Query: ")
search =  search_term.split()

for i in search:
    print("\nSearching for "+ i +"....\n")
    results = pubmed.query(i, max_results= + max_result)
    articleList = []
    articleInfo = []

    for article in results:
    # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle).
    # We need to convert it to dictionary with available function
        articleDict = article.toDict()
        articleList.append(articleDict)

    # Generate list of dict records which will hold all article details that could be fetch from PUBMED API
    for article in articleList:
    #Sometimes article['pubmed_id'] contains list separated with comma - take first pubmedId in that list - thats article pubmedId
        pubmedId = article['pubmed_id'].partition('\n')[0]
        # Append article info to dictionary 
        articleInfo.append({u'Pubmed_id':pubmedId,
                           u'Title':article['title'],
                           u'Abstract':article['abstract'],
                           u'Publication_date':article['publication_date'], 
                           u'Authors':article['authors']})

    # Generate Pandas DataFrame from list of dictionaries
    articlesPD = pd.DataFrame.from_dict(articleInfo)
    filename = i + ".csv"
    export_csv = articlesPD.to_csv (filename, index = None, header=True)

    #Print first 10 rows of dataframe
    print(articlesPD.head(10))
    print("Done")
