from textblob import TextBlob 


wiki=TextBlob("Siraj is very angry that he never gets good matches on tinder")
print (wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)