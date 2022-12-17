from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By 
import time
import requests
import random

#slack infomation
token = "xoxb-"
channel = "#channel"

#인스타그램 저장
instagram_id = "test@gmail.com"
instagram_pw = "test@gmail.com"

intc = int(input("로그인 정보를 기억할까요? \n 0은 저장된 정보로 로그인 \n 1은 save 입니다"))
#해당 기능 없음 ( db 연결시 사용 가능 )
if(intc == 1):
    inid = str(input("인스타그램 로그인 ID를 입력해주세요!"))
    inpw = str(input("인스타그램 비밀번호를 입력해주세요!"))     
    
    instagram_id = inid
    instagram_pw = inpw
    print(instagram_id,instagram_pw)

print("tip-slack 정보를 저장하시면 슬랙으로 알림을 받으실 수 있습니다!")
print("tip 2단계 인증 시스템 적용 시 미리 허용을 해주세요!!")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(1)

driver.find_element(By.CLASS_NAME,"_aa4b._add6._ac4d").send_keys(instagram_id)


driver.find_element(By.NAME,"password").send_keys(instagram_pw)


driver.find_element(By.CLASS_NAME,"_acan._acap._acas._aj1-").click()
now = driver.current_url 

time.sleep(5)
if(driver.current_url == now):
    testrc = "로그인 실패! 입력하신 ID정보를 확인해주세요!"
    # slack session
    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": testrc})
    

post = "------------------------------------------------\n 로그인 성공! \n  현재 접속 중인 계정은 test@naver.com 입니다 ------------------------------------------------"

docs = post.replace("test@naver.com", instagram_id)
requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": docs})

def slack():
    requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": dtyu})

driver.get("https://www.instagram.com/")

timer = random.randint(8, 15)
count = 0
if(driver.find_element(By.CLASS_NAME,"_abl-")):
    
    while True:
        driver.find_element(By.CLASS_NAME,"_abl-").click()
        time.sleep(timer)
        count = count + 1
        if(count == count % 10):
            date = str(count)
            dtimer = "번 반복 하트를 눌렀습니다"
            dtyu = date+dtimer
            slack()
        else:
            print("error-49012")
            dtyu = "ERROR-49012"
            slack()
    
else:
    print("error-1902,관리자 문의 요망")
    dtyu = "ERROR-1902"
    slack()


    
    