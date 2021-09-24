from selenium import webdriver
import time
import config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path=r"C:\Users\diganthp\Downloads\Chromedriver.exe")

driver.get("https://uta.joinhandshake.com/login")
driver.maximize_window()

#Explicit wait condition
wait = WebDriverWait(driver, 15, poll_frequency=3)

login = wait.until(ec.visibility_of_element_located((By.ID, "sso-name")))
login.click()

#Login Details
netidspace = wait.until(ec.visibility_of_element_located((By.ID, "netid")))
netidspace.send_keys("{}".format(config.netid))

passwordspace = wait.until(ec.visibility_of_element_located((By.ID, "password")))
passwordspace.send_keys("{}".format(config.password))

submitbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"signin-form\"]/input[3]")))
submitbtn.click()

#Home Page
jobsbtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"permanent-topbar\"]/div/div/div[1]/div/nav/div/div/div/div[1]/div/nav/ul/li[1]/div/a")))
jobsbtn.click()

#Jobs Page
oncampusbtn = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div/div[1]/div/form/div[1]/div/div/div/div[2]/button[4]/div")))
oncampusbtn.click()

postedbtn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"skip-to-content\"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[1]/div[1]/div/div[2]/div/button")))
postedbtn.click()

createdbtn = wait.until(ec.element_to_be_clickable((By.ID, "sort-by-created_at")))
createdbtn.click()

#list of jobs
for i in range(50):
    if i % 2 != 0:
        sortedjobs = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/main/div[3]/div/div[1]/div/form/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[{}]/a/div/div/div".format(i))))
        sortedjobs.click()
        applybtn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"skip-to-content\"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div[1]/span/button/span/div")))
        print(applybtn.text)









