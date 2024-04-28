from  bs4 import BeautifulSoup 

import requests



url = "https://news.ycombinator.com/"

yc_web_page = requests.get(url).text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page,"html.parser") 

all_scores = soup.find_all(class_="score")
# print(all_scores)

all_anchors = soup.find (name="span",class_="titleline" )
print(all_anchors)
article_text =all_anchors.getText()
article_link = all_anchors.get("href") 
print(article_text)
print(article_link)


# <span class="score" id="score_40190542">117 points</span>
# <span class="score" id="score_40187656">274 points</span>

  
#<a href="https://github.com/rejunity/z80-open-silicon">Zilog Z80 CPU – Modern, free and open source silicon clone</a>
# <a href="https://phys.org/news/2024-04-barley-fine-tune-root-microbial.html">Barley plants fine-tune root microbial communities through sugary secretions</a>

# with open("website.html","r", encoding="utf-8") as file:
#     contents= file.read() 
    
 
# soup = BeautifulSoup(contents,"html.parser") 
# # print(soup.title.string )

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText()) -> name
#     # print(tag.get("href")) #-> link
#     pass
# # print(soup.prettify(encoding="utf-8"))



# heading = soup.find(name="h1",id="name")
# print(heading.get("id"))


# section_heading = soup.find(name="h3",class_="heading")
# print(section_heading.getText())


# company_url = soup.select_one(selector = "#name") #sadece ilkini almak için kullanılır
# print(company_url)


# headings = soup.select( ".heading")#birden çok seçmek için
# print(headings)