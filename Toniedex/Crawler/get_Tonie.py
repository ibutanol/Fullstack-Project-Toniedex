from bs4 import BeautifulSoup
from urllib.parse import urljoin
from db_tables import Tonies,Titles
from helium import start_firefox
import time
import re
from tqdm import tqdm

def crawl():
    print("hallo hurensohn")
    url = 'https://tonies.com/de-de/tonies/?page=99'
    with start_firefox(url,headless=True) as r:
        time.sleep(1)

        suppe = BeautifulSoup(r.page_source, features="html.parser")
        a = suppe.select(".IconButton__Wrapper-sc-htjiht-0.ANVJQ")
        pbar = tqdm(total = len(a),dynamic_ncols=True)

        for i in a:
            new_link = i.attrs["href"]
            data={}
            next_link = urljoin(url,new_link)
            with start_firefox(next_link, headless=True) as r_2:
                time.sleep(1)
                neue_suppe = BeautifulSoup(r_2.page_source, 'html.parser')
                data["title"] = neue_suppe.select_one("h1.sc-iBdmCd.hdJxSy").get_text()

                data["figure"]  = neue_suppe.select_one("h2.lbAbeF").get_text()
                data["description"] = neue_suppe.select_one(".sc-guDLRT.dXPtKg").get_text()
                data["titles"] = []
                for o in neue_suppe.select(".cTIvYe"):
                    new_titles = Titles(titles = o.get_text())
                    data["titles"].append(new_titles)
                data["runtime"] = neue_suppe.select(".iBpcit p")[0].get_text()
                data["age_recommendation"] = neue_suppe.select(".iBpcit p")[1].get_text()
                data["image"] = neue_suppe.select("img.sc-lnskGP.blqpjg")[1].attrs["src"]
                irog = data["image"]
                x = re.findall(r"w_\d*,h_\d*",irog)
                pup = irog.replace(x[0],"w_900,h_800")
                print(pup)
                data["image"] = pup
                tonie = Tonies(**data)
                yield tonie
                pbar.update(1)