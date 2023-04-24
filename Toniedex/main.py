import json

from Crawler.get_Tonie import crawl

Tonies = []
a= crawl()
count = 0
for mund in a:
    with open("Tonies.json", "w",encoding ="utf8", ) as file:
        json.dump(Tonies, file,indent=4, ensure_ascii=False)
    Tonies.append(mund.__dict__)
    count = count + 1
    if count == 355:
        break
    





