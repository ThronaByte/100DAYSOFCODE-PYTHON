import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv('.env')
URL = "https://www.amazon.com/Hokafenle-Ergonomic-Mousepad-Non-Slip-Wireless/dp/B0BPD3MMQ4/ref=sxbs_pa_sp_search_thematic_btf_sspa?content-id=amzn1.sym.0894b7e3-a6d0-4415-80f5-c710cb6f141b%3Aamzn1.sym.0894b7e3-a6d0-4415-80f5-c710cb6f141b&crid=2UZ57LODSQRBG&cv_ct_cx=mouse%2Bfor%2Blaptop&dib=eyJ2IjoiMSJ9.laJlS3wI08QVyauqUseutb79WSQpbYuH3um82jexlfoK3DTNnlTb8PtF6-4TehtC.fIk09Ro07XxEKKGhPH-6Rs8pRcf5iwGD9FnvfjOddcc&dib_tag=se&keywords=mouse%2Bfor%2Blaptop&pd_rd_i=B0BPD3MMQ4&pd_rd_r=dd34e3e9-7dd9-4037-b42a-9a65782c25f7&pd_rd_w=3Qklk&pd_rd_wg=0fSQr&pf_rd_p=0894b7e3-a6d0-4415-80f5-c710cb6f141b&pf_rd_r=YEJBZ32PQTM17EAACZ5R&qid=1731002468&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=mouse%2Caps%2C4781&sr=1-2-2ce85fbe-2281-435c-ad39-d4a3c51e67ed-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWNfYnRm&th=1"
param={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "Accept-Language":"en-US,en;q=0.9"
}
response = requests.get(URL, headers=param)
amazon = response.content

soup = BeautifulSoup(amazon, 'html.parser')
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 20

if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price}"
    MY_MAIL = os.getenv('MY_MAIL')
    PASSWORD = os.getenv('APP_PASSWORD')
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(MY_MAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nLink:{URL}".encode("utf-8")
        )
