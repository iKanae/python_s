
def create_urls(keywordlist):
    urllist=[]
    for keyword in keywordlist:
        url="http://www.9apps.com/search/tag-"+str(keyword)+"-1/"
        urllist.append(url)
    return urllist
