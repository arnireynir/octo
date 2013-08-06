import requests
import bs4
import re

def word(file):
  with open(file, encoding='utf8') as f:
    setning = f.readline().rstrip()
    word = f.readline().rstrip()
    word1 = f.readline().rstrip()

  form1 = query(word)
  form = query(word1)
  pr = re.split('\W+', setning)
  val = pr
  for i in pr:
    if i in form1:
      s = form1.index(i)
      t = pr.index(i)
      val[t] = form[s+1]
  senda = ' '.join(val)
  with open('newtext.txt', 'w') as g:
    g.write(senda)
  return


def query(word):
  r = requests.post('http://bin.arnastofnun.is/leit.php',
                 params={'q': word, 'ordmyndir':'on'})
  s = bs4.BeautifulSoup(r.text)
  form = []
  elem = s.find_all('span', 'VO_beygingarmynd')
  if elem:
    for row in elem:
      form.append(row.text)
    return (form)
  else:  # Ef orð eru tvíræð og þarf að skrapa aðra síðu
    for i in s.find_all('li'):
      if i.text.endswith('nafnorð'): #Velja það orð sem endar á nafnorð (Kvennkyns, Hvorukyns eða Karlkyns)
        rb = i.a.get('href')
        r = requests.post('http://bin.arnastofnun.is/'+ rb)
        s = bs4.BeautifulSoup(r.text)
        form = []
        elem = s.find_all('span', 'VO_beygingarmynd')
        if elem:
          for row in elem:
            form.append(row.text)
          return (form)

word('texti.txt')
