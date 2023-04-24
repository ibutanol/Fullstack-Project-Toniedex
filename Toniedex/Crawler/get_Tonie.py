import sys
print(sys.path[0])
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Crawler.Tonie_Object import Tonie
from helium import start_firefox
import time
import re 

def crawl():
    url = 'https://tonies.com/de-de/tonies/?page=999'
    with start_firefox(url,headless=True) as r:
        time.sleep(1)

        suppe = BeautifulSoup(r.page_source, features="html.parser")
        a = suppe.select(".IconButton__Wrapper-sc-htjiht-0.ANVJQ")

        for i in a:
            penis = i.attrs["href"]
            data={}
            muschi = urljoin(url,penis)
            with start_firefox(muschi, headless=True) as r_2:
                time.sleep(1)
                kacka = BeautifulSoup(r_2.page_source, 'html.parser')
                data["title"] = kacka.select_one("h1.sc-iBdmCd.hdJxSy").get_text()
                data["figure"]  = kacka.select_one("h2.lbAbeF").get_text()
                data["description"] = kacka.select_one(".sc-guDLRT.dXPtKg").get_text()
                data["titlelist"] = []
                for o in kacka.select(".cTIvYe"):
                    data["titlelist"].append(o.get_text())
                data["runtime"] = kacka.select(".iBpcit p")[0].get_text()
                data["age_recommendation"] = kacka.select(".iBpcit p")[1].get_text()
                data["image"] = kacka.select("img.sc-bxotGS.kwtvNw")[2].attrs["src"]
                irog = data["image"]
                x = re.findall(r"w_\d*,h_\d*",irog)
                pup = irog.replace(x[0],"w_1000,h_1200")
                print(pup)
                data["image"] = pup
                tonie = Tonie(**data)
                yield tonie
