from db_tables import Tonies,Titles
import re
import time
import requests

def crawl():
    time.sleep(1)
    url = "https://tonies.com/_next/data/P9a9GXYGfSs6dFPQYRNNq/de-de/tonies.json?locale=de-de&slug=tonies&page=20"
    response = requests.get(url)
    base_url = "/".join(url.split("/", 6)[:6])
    response2 = response.json()
    keys = response2["pageProps"]["page"]["productList"]["normalizedProducts"]
    for i in keys:
        x = i["path"].rstrip("/")
        fullurl = base_url + x + ".json"
        print(fullurl) 
        response3 = requests.get(fullurl)
        r = response3.json()
        r2 = r["pageProps"]["product"]
        data = {}
        data["title"] = r2["name"] 
        data["figure"] = r2["series"]["label"]
        data["description"] = re.sub("<[^<]+?>", "", data["description"])
        data["runtime"] = r2.get("runTime", "Keine Laufzeit")
        data["age_recommendation"] = r2.get("ageMin","Keine Altersangabe")
        data["image"] = r2.get("images", [{}])[1].get("src", "")
        data["titles"] = []
        for i,x in enumerate(r2.get("tracks",[]),1):
            data["titles"].append(Titles(titles = x,title_nr = i))
        yield Tonies(**data)

crawl()

