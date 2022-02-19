# 네이버 인기 상승 종목 주가 가져오기

from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

# for title in soup.select("a.tltle"):
#   print(title.get_text(strip=True)) # 종목명 가져오기

# for tr in soup.select("table.type_5 tbody tr"): # 크롬 개발자 도구에는 tbody 태그가 있지만, 원래 HTML 문서에는 tbody 태그가 없기 때문에 출력 X(페이지 소스 보기 활용)
#   print(tr)

for tr in soup.select("table.type_5 tr"):
  if len(tr.select("a.tltle")) == 0: # 필요한 정보가 들어 있지 않은 경우 건너뛰고 출력
    continue
  title = tr.select("a.tltle")[0].get_text(strip=True)
  price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True) # number 클래스를 가지는 네번째 td 태그
  change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True) # number 클래스를 가지는 여섯번째 td 태그
  print(title, price, change)