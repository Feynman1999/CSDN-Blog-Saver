#encoding:utf-8 
# for windows csdn markdown article
# test on windows10 & chrome & python3.6.2
# author: Feynman1999
import time
import win32con
import win32clipboard as wincld

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# 获取系统Clipboard for windows
def get_Clipboard():
    wincld.OpenClipboard()
    result = wincld.GetClipboardData()
    wincld.CloseClipboard()
    return result


# 登录
def login(driver, username, password):
    driver.get("https://passport.csdn.net/login")
    time.sleep(15) # 目前需要手动登录 
    driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/ul/li[1]/a").click()
    time.sleep(1)
    elem_user = driver.find_element_by_id("all")
    elem_user.send_keys(username)
    time.sleep(1)
    elem_pwd = driver.find_element_by_id("password-number")
    elem_pwd.send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div[2]/form/div/div[6]/div/button").click()


Forbidden_sign = ['\\','/',':','*','?','？','"','<','>','|']

# windows下文件名有一些禁止符号
def deal_name(title):
    temp_list = []
    for char in title:
        if char in Forbidden_sign:
            temp_list.append('_')
        else:
            temp_list.append(char)
    return "".join(temp_list)


def main():
    options=webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    driver=webdriver.Chrome(executable_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                            chrome_options = options)
    login(driver, 'yourusername', 'password')

    # 此处直接使用get_article_list.py获得的结果(list.txt)
    with open('list.txt', 'r') as lt:
        Str = lt.read()
        Article_List= Str.splitlines()

    Base_dir = './articles_2/' # 先判断有无该文件夹 若无则建
    Suffix = '.txt'
    limit_id = 100000000

    for Id in Article_List:
        if int(Id) >= limit_id:
            continue
        print("处理{}中...".format(Id))
        time.sleep(3)
        driver.get("https://mp.csdn.net/mdeditor/"+Id)
        time.sleep(7)
        # element_1 是文章内容
        try:
            element_1 = driver.find_element_by_css_selector("[class='editor__inner markdown-highlighting']") #只支持markdown
        except:
            print("元素定位错误！可能是由于非markdown文档 或者 登录信息失效 所致")
            continue
        element_1.send_keys(Keys.CONTROL, "a")
        time.sleep(2)
        element_1.send_keys(Keys.CONTROL, "c")
        time.sleep(2)
        content = get_Clipboard() 
        # element_2 是文章标题
        element_2 = driver.find_element_by_css_selector("[class='article-bar__title article-bar__title--input text-input']")
        title = element_2.get_attribute('value')
        title = deal_name(title)
        txt_name = title+"_"+Id
        with open(Base_dir+txt_name+Suffix, 'w', encoding="utf-8") as f:
            f.write(content)
            print(txt_name+"写入成功")
    driver.quit()


if __name__ == '__main__':
    main()


