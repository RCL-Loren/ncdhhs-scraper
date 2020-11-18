from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class NCDHHSScraper:
    def __init__(self, baseUrl, steps):
        # these lines will help if someone faces issues like
        # chrome closes after execution
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument("--headless")
        self.opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.opts)

        params = {"behavior": "allow", "downloadPath": "/Users/bdavis/Downloads"}
        self.driver.execute_cdp_cmd("Page.setDownloadBehavior", params)

        self.driver.get(baseUrl)
        self.driver.implicitly_wait(5)  # seconds

        for step in steps:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, step))
            ).click()

            if step == steps[-1]:
                time.sleep(5)  # assumes download and forces longer sleep

        self.driver.close()


NCDHHSScraper(
    "https://public.tableau.com/views/NCDHHS_COVID-19_DataDownload/CountyCasesandDeaths?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=yes&:toolbar=yes&:animate_transition=yes&:display_static_image=no&:display_spinner=yes&:display_overlay=no&:display_count=yes&:language=en&publish=yes&:loadOrderID=0",
    [
        '//*[@id="tableauTabbedNavigation_tab_2"]',  # tab select
        "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[5]/span[1]",  # download button
        '//*[@id="DownloadDialog-Dialog-Body-Id"]/div/button[3]',  # select crosstab
        '//*[@id="export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id"]/div/div[1]/div[2]/div/div/div[2]/div',  # select the sheet
        '//*[@id="export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id"]/div/div[2]/div[2]/div/label[2]',  # select csv
        '//*[@id="export-crosstab-options-dialog-Dialog-BodyWrapper-Dialog-Body-Id"]/div/div[3]/button',  # select download button
    ],
)
