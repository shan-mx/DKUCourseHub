from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

browser = webdriver.Chrome()
try:
    browser.get('http://dkuhub.dku.edu.cn/psp/CSPRD01/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.CLASS_SEARCH.GBL?Page=SSR_CLSRCH_ENTRY')
except WebDriverException:
    print('Internet Error: Cannot Connect To DKUHub')
    exit(0)

usr = 'ms1129'
pwd = 'qV7urPGc@@YM9Br'
term_name = '2023 Spring Term'

browser.find_element(By.ID, 'expand-netid').click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'j_username'))).send_keys(usr)
browser.find_element(By.ID, 'j_password').send_keys(pwd)
browser.find_element(By.ID, 'Submit').click()
browser.switch_to.frame('ptifrmtgtframe')
term_selector = Select(browser.find_element(By.ID, 'CLASS_SRCH_WRK2_STRM$35$'))
options_text = [each.text for each in term_selector.options]
if term_name not in options_text:
    print('Error: Invalid term, check all terms below\n', '\n'.join(options_text))
term_selector.select_by_visible_text(term_name)
time.sleep(1)
Select(browser.find_element(By.ID, 'SSR_CLSRCH_WRK_ACAD_CAREER$2')).select_by_value('UGRD')
time.sleep(1)
Select(browser.find_element(By.ID, 'SSR_CLSRCH_WRK_LOCATION$6')).select_by_visible_text('Kunshan Campus')
time.sleep(1)
browser.find_element(By.ID, 'SSR_CLSRCH_WRK_UNITS_MINIMUM$10').send_keys(Keys.ENTER)
browser.switch_to.default_content()
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'ptModFrame_0')))
browser.switch_to.frame('ptModFrame_0')
browser.find_element(By.ID, '#ICSave').click()
browser.switch_to.default_content()
browser.switch_to.frame('ptifrmtgtframe')
WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'win0divSSR_CLSRSLT_WRK_GROUPBOX2GP$0')))
class_num = int(browser.find_element(By.CLASS_NAME, 'PSGROUPBOXLABEL').text.split(' ')[0])
t = 0
index = 0
data = {}
while t < class_num:
    classes_num = len(browser.find_element(By.ID, f'ACE_$ICField48${index}').find_elements(By.TAG_NAME, 'tr')) // 8
    course_name = browser.find_element(By.ID, f'win0divSSR_CLSRSLT_WRK_GROUPBOX2GP${index}').text.strip()
    course = data[course_name] = {}
    for i in range(classes_num):
        name, section = browser.find_element(By.ID, f'win0divMTG_CLASSNAME${t}').text.split('\n')
        course[name] = {}
        course[name]['section'] = section
        course[name]['number'] = browser.find_element(By.ID, f'win0divMTG_CLASS_NBR${t}').text
        course[name]['time'] = browser.find_element(By.ID, f'win0divMTG_DAYTIME${t}').text.split('\n')
        course[name]['room'] = browser.find_element(By.ID, f'win0divMTG_ROOM${t}').text.split('\n')
        course[name]['instructor'] = browser.find_element(By.ID, f'win0divMTG_INSTR${t}').text.replace(',\n', ', ').split('\n')
        course[name]['date'] = browser.find_element(By.ID, f'win0divMTG_TOPIC${t}').text.split('\n')
        t += 1
    index += 1
print(data)