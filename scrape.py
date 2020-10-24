from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')

driver.get("https://public.tableau.com/views/NCDHHS_COVID-19_DataDownload/DailyCasesandDeathsMetrics?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=yes&:toolbar=yes&:animate_transition=yes&:display_static_image=no&:display_spinner=yes&:display_overlay=no&:display_count=yes&:language=en&publish=yes&:loadOrderID=0")

driver.implicitly_wait(3) # seconds
tab_select = driver.find_element_by_xpath("//*[@id=\"tableauTabbedNavigation_tab_1\"]")
tab_select.click()

time.sleep(2)
dl_button = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[5]/span[1]")

dl_button.click()

time.sleep(1)

cross_tab = driver.find_element_by_xpath("//*[@id=\"DownloadDialog-Dialog-Body-Id\"]/div/button[3]")

cross_tab.click()

time.sleep(1)

get_csv = driver.find_element_by_xpath("//*[@id=\"export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id\"]/div/div[2]/div[2]/div/label[2]")
get_csv.click()

time.sleep(1)
dl_button = driver.find_element_by_xpath("//*[@id=\"export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id\"]/div/div[3]/button")
dl_button.click()

time.sleep(4)

driver.close()

