#-*-encoding: utf-8 -*-
#크롤링 예제 실습
import urllib
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def DataGetter(DOI):
	api_url_front = 'http://api.elsevier.com:80/content/article/doi/'
	api_url_end = '?apiKey=6492f9c867ddf3e84baa10b5971e3e3d'
	
	#api_url = api_url_front + DOI + api_url_end 
	api_url = 'http://api.elsevier.com:80/content/article/doi/10.1016/j.procs.2015.07.063?apiKey=6492f9c867ddf3e84baa10b5971e3e3d'
	fp = urllib.urlopen(api_url);
	source = fp.read();

	doc = ET.parse(source)
	root = doc.getroot();




	#print(source);
	soup = BeautifulSoup(source, "html.parser")
	#print(soup)
	Title = soup.find(element = "title")
	#print(Title)
	fp.close();


def temp():
	doc = ET.parse("note.xml")
	root = doc.getroot();

	country_text = root.findtext("country")
	#print country_text

	for neighbor in root.iter("neighbor"):
		#print neighbor.attrib
		#temp

print("===================== Crawler Start =====================")
#temp()

f_in = open("DOI_data.txt", "r");
f_in.close();
DOI = '10.1016/j.procs.2015.07.063'
DataGetter(DOI)


print("====================== Crawler End ======================")


#http://dev.elsevier.com/retrieval.html#!/Article_Retrieval/ArticleRetrieval
#10.1016/j.procs.2015.07.063