import requests

def Get_title(isbn): 
	url='https://api.openbd.jp/v1/get?isbn='+str(isbn)
	response=requests.get('https://api.openbd.jp/v1/get?isbn=9784152078469')
	content=response.json()[0]
	return (content['summary']['title'])