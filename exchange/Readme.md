#Setup
- Create virtualenv 'virtualenv -p python3 venv'
- pip install -r requirements.txt

#Usage
- Þegar textaskráin er gerð (texti.txt) þarf að hafa textann í einni línu
- og í næstu línu kemur orðið sem á að breyta í textanum,
- þarnæst kemur það orð sem kemur í stað þess orðs sem er á undann.
- ath þarf að vera newline char (\n) eftir hverja línu.
- Run python3 word.py
- þá býr skriftan til skrá sem heitir newtext.txt með breyttum texta.

#BUG:
- Ef orð sem breytt er, er með kommu, punkt eða öðrum merkjum
- þá hreinsar skriftan þá í burt og skilar þeim ekki aftur.
