import urllib.request
import time
  
def get_webservertime(url):
   #返回一个对象
    
    response=urllib.request.urlopen(url,timeout=5)
    #打印出远程服务器返回的header信息
    header=response.info()
    # print(header)
    for i in range(len(header._headers)):
        if 'Date' in header._headers[i]:
            ts=header._headers[i][1]
            #将GMT时间转换成北京时间
            ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
            ttime=time.localtime(time.mktime(ltime)+8*60*60)
            dat="%u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
            tm="%02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
            #print (dat,tm)
            return dat+' '+tm
            
        # else:
        #     continue
            # print('获取的信息不存在。')
            # return 'Error:获取的信息不存在!'
    
    
def get_time_url():
    # url_list=['www.baidu.com','www.jd.com','www.sina.com','www.sohu.com','192.168.28.143'] 
    #url_list=['10.116.45.11','10.116.45.24','10.116.2.20']
    with open('time_service.txt') as fn:
        get_time_service=fn.read()
    url_list=get_time_service.split('\n')
    # print(url_list)
    for i in url_list:
        try:
            temp=get_webservertime('http://'+i)
            print(i,':',temp)
            return temp
            break
        except Exception as e:
            print('Error:',e)
            continue
if __name__ == '__main__':
      
    get_time_url()
    # print(get_webservertime('http://www.baidu.com'))
 