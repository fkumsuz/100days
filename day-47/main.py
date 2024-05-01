from bs4 import BeautifulSoup
import sys
import requests

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.amazon.com.tr/gp/product/B07W6JL85W/ref=ox_sc_saved_image_1?smid=A1UNQM1SR2CHM&psc=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml") 

price = soup.find(class_="a-offscreen") 
print("Price",price)
price=price.getText()
print(price)
price= float(str.replace(price.replace('.', '').replace(',', '.'),"TL",""))
print(price)


def send_mail(send_user, password, to_user, quote):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=send_user, password=password)

            subject = "Subject: Price Alert!!"
            body = quote#.replace('"-', '"\n-')
            message = subject + "\n\n" + body

            connection.sendmail(from_addr=send_user,
                                to_addrs=to_user, msg=message)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
        
        
if price<3500:
    send_mail(send_user="xxx@gmail.com", password="xxx",
                      to_user="xxx@gmail.com", quote=f"Price is {price}!!!")