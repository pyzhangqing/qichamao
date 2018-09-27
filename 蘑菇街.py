'https://list.mogujie.com/search?callback=jQuery21109528018020686176_1536678057418&_version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid=10059141&action=sports'
import json
import requests
from util.function import save_item


def one_page(page):

    url='https://list.mogujie.com/search?callback=jQuery21109528018020686176_1536678057418&_version=8193&ratio=3%3A4&cKey=15&page='+ str(page) +'&sort=pop&ad=0&fcid=10059141&action=sports'

    headers ={

        "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",

    }
    response=requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        # print(text)
        return text



def new_dict(text):
    text = text.replace('/**/jQuery21109528018020686176_1536678057418(','')[:-2]
    # print(text)
    js_dict=json.loads(text)
    print(js_dict)
    return js_dict


def get_messages(js_dict):

    mes=js_dict['result']['wall']['docs']
    # print(mes)
    mes_list=[]
    for i in mes:
        ndict={}
        ndict['img'] = i['img']
        ndict['title'] = i['title']
        ndict['org_price'] = i['orgPrice']
        ndict['price']=i['price']
        mes_list.append(ndict)
        with open('text.json','a')as f:
            json.dump(mes_list,f)
        for j in mes_list:
            img=j['img']
            r=requests.get(img)
            filename = './image/%s' % img.split('/')[-1]
            # print(filename)
            with open(filename, 'wb')as f:
                f.write(r.content)




def get_pages():
    page =1
    while True:
        text = one_page(page)
        js_dict = new_dict(text)
        is_end = js_dict['result']['wall']['isEnd']
        # print(js_dict)
        if is_end:
            return
        result = get_messages(js_dict)
        # print(result)
        for item in result:
            print(item)
        # print(is_end)
            save_item(item)
        page += 1



def main():
    get_pages()


if __name__ == '__main__':
    main()