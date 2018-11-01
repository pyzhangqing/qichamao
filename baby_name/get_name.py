import requests
from lxml import etree
import pymysql


con = pymysql.connect(host='localhost', port=3306,
                      db='new', user='root',
                      passwd='123456', charset='utf8')

num=1

def index(url):
    headers={
        "User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code==200:
            text=response.content.decode('utf-8')
            # print(text)
            return text
    except:
        index(url)




def one_name(one_name_link):
    re_link=one_name_link.split('/')
    # print(re_link)
    boys_link = []
    girls_link = []
    for i in range(1,10):
        new_boy_link='http://'+re_link[2]+'/name/boys_'+str(i)+'.html'
        new_girl_link='http://'+re_link[2]+'/name/girls_'+str(i)+'.html'
        # print(new_girl_link)
        boys_link.append(new_boy_link)
        girls_link.append(new_girl_link)

    return (boys_link,girls_link)



def all_link(new_html):
    etree_html=etree.HTML(new_html)
    name=etree_html.xpath('//div[@class="col-xs-12"]/a[contains(@class,"btn btn-link")]/text()')
    return name





def pares_name_link(html):
    global num
    etree_html=etree.HTML(html)
    all_name_link = etree_html.xpath('//div[@class="col-xs-12"]/a[contains(@class,"btn btn2")]/@href')

    for one_name_link in all_name_link:
        boys_name,girls_name=one_name(one_name_link)
        try:
            for boy_name in boys_name:
                new_boy_html=index(boy_name)
                boy_one_name=all_link(new_boy_html)
                with con.cursor() as cursor:
                    for item in boy_one_name:
                        result = cursor.execute(
                            "insert into all_name(name,gender) values ('%s','%s')" %(item,'M')
                        )
                        if result == 1:
                            print('正在插入男生%d条名字'% num)
                            num+=1
                    con.commit()

        except MemoryError as e:
            print(e)
            con.rollback()

        try:

            for girl_name in girls_name:
                new_girl_html=index(girl_name)
                girl_one_name=all_link(new_girl_html)
                with con.cursor() as cursor:
                    for item in girl_one_name:
                        result = cursor.execute(
                            "insert into all_name(name,gender) values ('%s','%s')" %(item,'F')

                        )
                        if result == 1:
                            print('正在插入女生%d条名字'% num)
                            num+=1
                    con.commit()

        except MemoryError as e:
            print(e)
            con.rollback()




def main():
    url = 'http://www.resgain.net/xmdq.html'
    html = index(url)
    all_link=pares_name_link(html)
    # one_link=one_name(all_link)



if __name__ == '__main__':
    main()