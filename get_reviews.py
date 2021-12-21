from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import pandas as pd

def getReviews(URL,N):
#URL=input("Enter the URL: ")
#N=int(input("Enter the maximum number of reviews you need: "))

    driver = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get(URL)
    wait = WebDriverWait(driver,10)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    if N%25!=0:
        t=int(N/25)+1
    else:
        t=int(N/25)
    count=1
    while count<t:
        try:
            driver.find_element_by_css_selector("button#load-more-trigger").click()
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,".ipl-load-more__load-indicator")))
            soup = BeautifulSoup(driver.page_source, 'lxml')
            count+=1
        except Exception:break
    driver.quit()

    count1=0
    List=[]
    for elem in soup.find_all(class_='imdb-user-review'):
        if count1<N:
            title = elem.find(class_='title').get_text(strip=True)
            body = elem.find(class_='text').get_text(strip=True)
            List.append(title+str('.')+body)
            count1+=1
        else:
            break
    df=pd.DataFrame(List,columns=['review'])
    df.to_csv("Reviews.csv")
    #print(df)
    return(df)

if __name__ == "__main__":
    URL=input("Enter the URL: ")
    N=int(input("Enter the maximum number of reviews you need: "))
    getReviews(URL,N)


