import requests
import re

html = requests.get("https://www.russianfood.com/recipes/bytype/?fid=91&ysclid=m8jsskezk122439401").text

r_title = re.findall(r"<h3 itemprop=\"name\">(.+)</h3>", html)
r_products = re.findall(r"<div class=\"announce_sub\"><span>Продукты:&nbsp;(.+)</span>\s+</div>", html)
r_subtitle = re.findall(r"<div class=\"announce \" itemprop=\"description\">\s+<p>(.+)</p>\s+</div>", html)
r_src = re.findall(r"<div>\s+<img class=\"round shadow\" src=(.+)\s+title=.+\s+alt=.+\s+itemprop=.+>\s+</div>", html)

counter_k = 0
counter_i = 0
counter_n = 0

with open("jams.txt", "w", encoding="utf-8") as f:
    for index, t in enumerate(r_title):
        f.write(f"Title: {t}")
        f.write("\nProducts: ")
        
        for k in r_products[counter_k]:
            f.write(k)
        f.write("\nSub-Title: ")
        
        for i in r_subtitle[counter_i - 1]:
            f.write(i)
        f.write("\nSCR: ")
        
        for n in r_src[counter_n - 1]:
            f.write(n)
        
        counter_k += len(k)
        counter_i += len(i)
        counter_n += len(n)
        
        if index < len(r_title) - 1:
            f.write("\n\n")
f.close()