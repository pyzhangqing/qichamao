'https://list.mogujie.com/search?callback=jQuery21109528018020686176_1536678057418&_version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid=10059141&action=sports'
import json
import requests
def one_page(page):

    url='https://fe-api.zhaopin.com/c/i/sou?pageSize='+str(page)+'&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22801%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D'
    headers ={
        "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",

    }

    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        # print(text)
        # 转换成python格式
        js_dict = json.loads(text)
        # print(js_dict)

        return js_dict

def get_messages(js_dict):
    mes=js_dict['data']['results']
    print(mes)
    mes_list=[]
    for i in mes:
        ndict = {}
        ndict['name']=i['company']['name']
        ndict['salary']=i['salary']
        ndict['emplType']=i['emplType']
        ndict['jobName']=i['jobName']
        ndict['createDate']=i['createDate']
        ndict['endDate']=i['endDate']
        mes_list.append(ndict)
        with open('message.txt','a',encoding='utf-8')as f:
            f.write(str(mes_list)+'\n')


def main():
    js_dict=one_page(500)
    get_messages(js_dict)

if __name__ == '__main__':
    main()