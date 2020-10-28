import requests

def get_website_data(url):
    response=requests.get(url,timeout=5)
    return response
if __name__=='__main__':
    url=input('Please input website url:')
    temp_data=get_website_data(url)
    print("-----"*20)
    print("website status code:",temp_data.status_code)
    print("-----"*20)
    print("website time:",temp_data.headers['date'])
    print("-----"*20)
    for i in temp_data.headers:
        print("-----"*20)
        print(i,":",temp_data.headers[i])
