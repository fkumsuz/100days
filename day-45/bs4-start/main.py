from  bs4 import BeautifulSoup 

import requests



url = "https://news.ycombinator.com/"

yc_web_page = requests.get(url).text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page,"html.parser") 

all_scores = soup.find_all(class_="score")
# print(all_scores)

article_span_tag =  soup.find_all('span', class_='titleline') 
article_texts=[]
article_links=[]
for articles in article_span_tag:  
    article_tag = articles.find('a')  
    article_link =article_tag.get("href") 
    article_texts.append(article_tag.getText())
    print("---------------------------------------")
    print(article_link)
    article_links.append(article_link)
article_upvotes=[]
article_upvote = soup.find_all (name="span",class_="score" )
for upvotes in article_upvote: 
    
    article_upvotes.append(int(upvotes.getText().split()[0])) 
print("*************************************************************")
largest_num = max(article_upvotes)
largest_index= article_upvotes.index(largest_num)

print(article_texts[largest_index])

print(article_links[largest_index])
print( largest_index,largest_num)
    #  <a href="https://www.esa.int/Science_Exploration/Space_Science/Webb/Webb_captures_iconic_Horsehead_Nebula_in_unprecedented_detail">Webb captures iconic Horsehead Nebula in unprecedented detail</a>
     
    # <span class="titleline"><a href="https://codedbearder.com/posts/f3-backplane/">I made a new backplane for my consumer NAS</a><span class="sitebit comhead"> (<a href="from?site=codedbearder.com"><span class="sitestr">codedbearder.com</span></a>)</span></span>
     
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