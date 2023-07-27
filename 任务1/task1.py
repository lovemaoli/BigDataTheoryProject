from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def page_request(driver: webdriver,url):
    # 打开目标网址首页
    driver.get(url)
    
def next_request(driver: webdriver):
    # 获取下一页next按钮
    elem = driver.find_element(By.XPATH,'//ul[@class="pager"]/li[@class="next"]/a')
    elem.click()

def save_txt(info):
    print(info)
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(info + '\n')


def page_parse(driver,soup):
    i = 10
    j = 1
    while i > 0:
        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            # 找到并获取第一页的谚语位置span集合:items，点击下一页之后会变成下一页的谚语集合
            items = soup.find_all('span', class_='text')
            # 打印获取到第一页的谚语
            for item in items:
                save_txt('谚语'+str(j)+':')
                save_txt(item.text)
                j += 1
            next_request(driver)
            i -= 1
            # 停顿1秒，页面观察点击下一页的效果
            time.sleep(1)            
        except:
            return None


def main():
    url = 'http://quotes.toscrape.com/'
    # 加载驱动
    chromedriver = webdriver.Chrome() #在此我已经配置了driver的路径在环境变量，若未配置需要在括号中填入driver路径
    quotesoup = BeautifulSoup(chromedriver.page_source, 'lxml')
    page_request(chromedriver,url)
    page_parse(chromedriver,quotesoup)


if __name__ == '__main__':
    print("**************开始爬取quotes数据********************")
    main()
    print("*******************爬取完成*************************")