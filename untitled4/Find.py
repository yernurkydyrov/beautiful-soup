from Site import findsites

scrapper = findsites()
list = scrapper.findArticle("bitcoin")
for i in list: print(i)
print(f"\n sites: {str(len(list))}")
