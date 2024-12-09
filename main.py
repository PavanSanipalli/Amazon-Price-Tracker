import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

#url = "https://appbrewery.github.io/instant_pot/"


#Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent"": ",
    "Accept-Language"": "
}

response = requests.get(url=url, headers=header)


soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()

no_symbol = price.split("$")[1]

float_price = float(no_symbol)
print(float_price)



title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 80

if float_price < BUY_PRICE:
    message = f"{title} is below for {BUY_PRICE}"

with smtplib.SMTP(os.environ["SMTP_ADDRESS"]) as connection:
    connection.starttls()
    result = connection.login(user= os.environ[EMAIL], password=os.environ["PASSWORD"])
    connection.sendmail(
        from_addr= os.environ["EMAIL"],
        to_addrs= os.environ["EMAIL"],
        msg= f"Price Drop Alert! \n\n\n{message}\n {url}".encode("utf-8")
    )