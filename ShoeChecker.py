from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def UrlGenwithSize(size, model, name):
    base = 530
    mySize = (size-4)*20
    finalSize = base + mySize
    Url = "https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)

def UrlGenProduct(name, model):
    url = "https://www.adidas.ca/en/"+name+"/"+model+".html"
    print(url)

def CheckStock(myUrl, model):
    try:
        driver = webdriver.Chrome()
        driver.get(myUrl)
        WebDriverWait(driver, 10).until(EC.presence_of_element_loacted((By.CLASS_NAME, "add_to_bag_form___22702")))
        username = driver.find_element_by_class_name('gl-dropdown__select-element')
        options = username.find_element_by_tag_name("option")
        optionsList = []
        for option in options:
            optionsList.append(option.get_attribute('innerHTML'))
        for sizes in optionsList:
            if sizes.isdigit():
                print("Size "+sizes+ " for "+model+"is available")
    finally:
        driver.quit()

def addToCart(myUrl):
    driver = webdriver.Chrome()
    driver.get(myUrl)
    driver.find_element_by_xpath("(//SPAN[@class='gl-cta__text'][text()='Add to bag'])[1]").click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_loacted((By.CLASS_NAME, "gl-modal__main-content")))
    driver.find_element_by_xpath("//SPAN[@class='gl-cta__text'][text()='Go to checkout']").click()


url=UrlGenProduct("ultraboost-19-shoes", "EF1345")
CheckStock(url,"EF1345")
size=int(input("Please enter size "))
UrlGenwithSize(size, "EF1345","ultraboost-19-shoes")