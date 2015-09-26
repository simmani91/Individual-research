#-*-encoding: utf-8 -*-
#실시간 검색어 예습
import requests as rs
import bs4

def getTopRank():
	naver_url = 'http://www.naver.com'
	#요청
	response = rs.get(naver_url)

	#응답으로부터 html추출
	html_content = response.text.encode(response.encoding, "html.parser");


	#파싱
	navigator = bs4.BeautifulSoup(html_content)

	#네비게이터를 이용해 원하는 태그 리스트 가져오기
	realRankTag = navigator.find_all(id='realrank')
	resultList = realRankTag[0].find_all('a')

	#키워드 추출
	keywords = [item['title'] for item in resultList]

	#키워드 출력
	for index, keywords in enumerate(keywords):
		resultText = '[%d위] %s'%(index,keywords.encode('utf-8'))
		print resultText.decode('utf-8')#.encode('euc-kr')


print("dfadfa")
getTopRank()