import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.decathlon.it/p/disco-gomma-bodybuilding-28mm-2-5kg/_/R-p-173212?mc=8388695&c=NERO"
URL2 = "https://www.decathlon.it/p/disco-gomma-bodybuilding-28mm-5kg/_/R-p-173213?mc=8388696&c=NERO"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def checK():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    testo = soup.find_all("h3")[2].get_text()

    print("TESTO = ", testo)

    if testo != "Attualmente indisponibile":
        print("HELLO")
        # send_mail()
    else:
        print("nada cambiò nel primo")
        # send_nudes()

    page = requests.get(URL2, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup)

    testo = soup.find_all("h3")[2].get_text()

    print("TESTO = ", testo)

    if testo != "Attualmente indisponibile":
        print("HELLO")
        # send_mail()
    else:
        print("nada cambiò nel secondo")
        # send_nudes()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user = "giacomossio98@gmail.com", password = "giaco7777")

    subject = "SONO DISPONIBBBILI"
    body = "link diretto: https://www.decathlon.it/p/disco-gomma-bodybuilding-28mm-2-5kg/_/R-p-173212?mc=8388695&c=NERO"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("giacomossio98@gmail.com", "giacomo.mossio@gmail.com", msg)

    print("EMAIL SENT!")

    server.quit()


def send_nudes():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user = "giacomossio98@gmail.com", password = "giaco7777")

    subject = "non ci sono ancora kekw"
    body = "mannaggina"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("giacomossio98@gmail.com", "giacomo.mossio@gmail.com", msg)

    print("EMAIL SENT!")

    server.quit()



while(True):
    time.sleep(15)
    checK()
    time.sleep(60*60*3)

