from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Crawler.Tonie_Object import Tonie
from helium import start_firefox
import time
import re 

def crawl():
    url = 'https://tonies.com/de-de/tonies/?page=999'
    with start_firefox(url,headless=True) as r:
        time.sleep(5)

        suppe = BeautifulSoup(r.page_source, features="html.parser")
        a = suppe.select(".IconButton__Wrapper-sc-htjiht-0.ANVJQ")

        for i in a:
            penis = i.attrs["href"]
            print(penis)
            data={}
            muschi = urljoin(url,penis)
            print(muschi)
            with start_firefox(muschi, headless=True) as r_2:

                kacka = BeautifulSoup(r_2.page_source, 'html.parser')
                data["title"] = kacka.select_one("h1.sc-iBdmCd.hdJxSy").get_text()
                data["figure"]  = kacka.select_one("h2.lbAbeF").get_text()
                data["description"] = kacka.select_one(".sc-guDLRT.dXPtKg").get_text()
                data["titlelist"] = []
                for o in kacka.select(".cTIvYe"):
                    data["titlelist"].append(o.get_text())
                data["runtime"] = kacka.select("p.sc-iBdmCd.hlFbcq")[0].get_text()
                data["age_recommendation"] = kacka.select("p.sc-iBdmCd.hlFbcq")[1].get_text()
                data["image"] = kacka.select("img.sc-bxotGS.kwtvNw")[2].attrs["src"]
                a = 'https://res.cloudinary.com/tonies/image/fetch/f_auto,q_auto,c_fill,b_rgb:ffffff,w_166,h_125/https://278163f382d2bab4b036-4f5ec62496a160f3570d3b6e48fc4516.ssl.cf3.rackcdn.com/10001473-50004892-b-CH2wvqo-.png'
                x = re.findall(r"w_\d*,h_\d*",a)
                y =(x[0])
                print(a.replace(x[0],"w_2500,h_3000"))
                tonie = Tonie(**data)
                yield tonie