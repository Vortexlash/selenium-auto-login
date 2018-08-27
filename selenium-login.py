from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://YOURLINK.ru/')

a = browser.find_element_by_css_selector('input[type="submit"]')
amassiv = browser.find_element_by_css_selector('input[type="submit"]')
b = browser.find_element_by_id('login')
bmassiv = browser.find_element_by_id('login')
c = browser.find_element_by_class_name('menu')
cmassiv = browser.find_element_by_class_name('menu')

a.click()

# filling the login lines

login = browser.find_element_by_id('login')
login.send_keys('LOGIN')
password = browser.find_element_by_id('password')
password.send_keys('PASSWORD')
k = browser.find_element_by_css_selector('input[type="submit"]')
k.click()

# parsing div text

cmassiv = browser.find_element_by_class_name('mytext')
for x in cmassiv:
    print(x.text)

# parsing links

bmassiv = browser.find_elements_by_class_name('mylink')
for x in bmassiv:
    print(x.get_attribute('href'))



