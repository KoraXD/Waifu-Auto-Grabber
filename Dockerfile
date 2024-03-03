# © Waifu Auto Grabber

"""
🔥 Developers:
     ⚡ Kora | @KoraXD
     ⚡ Dark | @IkariS0_0
     ⚡ Otazuki | @Otazuki
"""

FROM python

WORKDIR /root/Waifu

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U -r requirements.txt

CMD ["python3","-m","Waifu"]
