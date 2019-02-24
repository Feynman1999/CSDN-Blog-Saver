import requests
from lxml import etree


def request_get(url):
    headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=5)
    return response


#  得到大于least_id的文章id 默认得到所有    (默认文章列表按照时间排序)
def get_article_id_list(username, least_id="0"):
    ans_list = []
    base_url = 'https://blog.csdn.net/' + username + '/article/list/'
    start_url = base_url + '1'
    now_list_id = 1
    article_num = 0
    html = request_get(start_url)

    while html.status_code ==200: # 200说明request_get完成，这是因为http协议里面定义的状态码
        selector = etree.HTML(html.text)
        cur_article_list_page = selector.xpath('//*[@id="mainBox"]/main/div[2]')
        d = cur_article_list_page[0].xpath('//*[@id="mainBox"]/main/div[2]/div[2]/h4/a')
        l = cur_article_list_page[0].findall('data-articleid')
        for elem in cur_article_list_page[0]:
            item_content = elem.attrib
            # 通过对比拿到的数据和网页中的有效数据发现返回每一个article_list中的list都有一两个多余元素，每个多余元素都有style属性，利用这一特点进行过滤
            if item_content.has_key('style'):
                continue
            else:
                if item_content.has_key('data-articleid'):
                    articleid = item_content['data-articleid'].strip()
                    if int(articleid) <= int(least_id.strip()):
                        return ans_list
                    article_num += 1
                    ans_list.append(articleid)
                    print("\n找到第" + str(article_num) + "篇博客...")


        now_list_id += 1
        next_url = base_url + str(now_list_id)
        html = request_get(next_url)


if __name__ == '__main__':
    # 默认
    List = get_article_id_list('yourusername','0')
    fl=open('list1.txt', 'w')  # 放到当前工作路径下的list.txt中
    sep = '\n'
    fl.write(sep.join(List))
    fl.close()
