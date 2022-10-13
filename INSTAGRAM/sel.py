import time
# from typing_extensions import final
from urllib.parse import urlencode
from wsgiref import headers
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.instagram.com/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

data = {
    'account' : [],
    'like' : [],
    'realese' : []
}

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get(url)

def cts_btn(css_s):
    while(True):
        try :
            driver.find_element(By.CSS_SELECTOR,f'{css_s}').click()
            print('Button Clicked!')
            break
        except:
            print(f'Not Detected Button...........{time.time()}')
            time.sleep(3)
            
            
def cts(ct):
    return f"{ct.replace(' ','.')}"
    
    


time.sleep(5)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys('firdauztria')
password.send_keys('Edo851999051')
        
log_in = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button')
log_in.click()
print('Log In Clicked!')
        
print("Login Successful")
# time.sleep(5)

cts_btn('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(1) > div > a > svg')

cts_btn(f'button.{cts("_a9-- _a9_1")}')


time.sleep(5)
html = soup(driver.page_source, 'html.parser')
articles = html.find_all('article')

try :
    for article in articles:
        # print(article.encode("utf-8","ignore")) 
        title = article.find('span', f"{cts('_aap6 _aap7 _aap8')}").get_text()
        data['account'].append(title)
        print(f"account : {title}")
        realese = article.find('time')
        print(f"{realese.title} -- {realese.get_text()}")
        data['realese'].append(realese)
        like = article.find('div', {'class' : "_aacl _aaco _aacw _aacx _aada _aade"}.span.get_text())
        print(f"like : {like}")
        data['like'].append(like)
    print(data)
except:
    driver.quit()
# start = time.time()



# initialScroll = 0 
# finalScroll = 3000

# while True:
#     try :
#         driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
#         print('scroll......')
#     except :
#         print(("Please Wait....."))
#     initialScroll = finalScroll
#     finalScroll += 1000
#     time.sleep(1)
#     end = time.time()
    
#     html = soup(driver.page_source, 'html.parser')
#     # content_div = html.find('div', class_=f'_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abc0 _abcm')
#     articles = html.find_all('article')
#     # print(articles)
#     for article in articles:
#         account = article.find('a').get_text()
#         print(f"post account : {account}")
        

#     if round(end-start) > 20:
#         break
    
    
# driver.quit()