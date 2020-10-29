import os
import json
import requests

start_url='https://www.ximalaya.com'
headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.10 Safari/537.36',
	}
def get_html(url):
	#2.解析url，得到网页源码
	#请求头，模拟浏览器

	html=requests.get(url,headers=headers)
	ret_html=html.content.decode('utf-8','ignore')
	print(ret_html)
def xima():
	#1.获取想要的url                                           19017184
	url='https://www.ximalaya.com/revision/play/tracks?trackIds=49364963%2C49364964%2C49364965%2C49364966%2C49364967'
	url2='https://mpay.ximalaya.com/mobile/track/pay/49364963?device=pc&isBackend=false&_=1565831080166'
	url3='https://mpay.ximalaya.com/mobile/track/pay/49364964?device=pc&isBackend=false&_=1565831728024'
	url4='https://mpay.ximalaya.com/mobile/track/pay/49364967?device=pc&isBackend=false&_=1565831826166'
	search_url2='https://www.ximalaya.com/revision/search?core=all&kw=%E5%91%A8%E6%81%A9%E6%9D%A5&spellchecker=true&device=iPhone'
	search_url='https://www.ximalaya.com/revision/seo/getTdk?typeName=SEARCH&uri=%2Fsearch%2F%E5%91%A8%E6%81%A9%E6%9D%A5'
	#2.解析url，得到网页源码
	#请求头，模拟浏览器

	html=requests.get(search_url2,headers=headers)
	ret_html=html.content.decode('utf-8','ignore')
	# print(ret_html)
	#3.提取数据，获取src地址
	result=json.loads(ret_html)
	# try:
	# 	result=json.loads(ret_html)
	# except:
	# 	print(ret_html)
	
	info_list=[]
	for i in range(9):
		url_list=[]
		name=result['data']['result']['album']['docs'][i]['title']
		print(name)
		url_list.append(name)
		get_url=start_url+result['data']['result']['album']['docs'][i]['url']
		print(get_url)
		print("###   ###   ###   ###")
		url_list.append(get_url)
		info_list.append(url_list)
	
	for i in info_list:
		get_html(i[1])
	# for i in result['data']['tracksAudioPlay']:
	# 	src=i['src']
	# 	name=i['trackName']
	# 	print(name)
	# #4.保存数据
	# 	with open('./img/{}.m4a'.format(name),'ab') as fn:
	# 		music=requests.get(src,headers=headers)
	# 		fn.write(music.content)

if __name__ == '__main__':
	xima()

	'''
https://www.qchannel03.cn/1.gif?url=-&domain=www.ximalaya.com&account=9a120171&channel=PC&point=PC&platform=PC&ts=1565830590194&dur=15
http://audio.pay.xmcdn.com/download/1.0.0/group1/M01/0C/5E/wKgJN1mqEfSCOH4lAG4BIi19U6Q320.m4a?sign=2b08850f7f018383e88c4363055c7ebb&buy_key=fe4f133ccbf4b22dfa2a1e704ccbbda8&token=2608&timestamp=1565830575&duration=890
http://audio.pay.xmcdn.com/download/1.0.0/group1/M01/0C/5E/wKgJN1mqEfSCOH4lAG4BIi19U6Q320.m4a?sign=2b08850f7f018383e88c4363055c7ebb&buy_key=fe4f133ccbf4b22dfa2a1e704ccbbda8&token=2608&timestamp=1565830575&duration=890
https://www.ximalaya.com/revision/seo/getTdk?typeName=SEARCH&uri=%2Fsearch%2F%E5%91%A8%E6%81%A9%E6%9D%A5
	'''