from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "C:/webdriver/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")
time.sleep(5)

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")

open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.ID, "LoginID_Card")
password_input = driver.find_element(By.ID, "LoginPassword")

# กรอกข้อมูลใน input field
id_input.send_keys("7777777777777")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID ที่กำหนดให้
login_button = driver.find_element(By.ID, "Login")
login_button.click()
# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

botton_click = driver.find_element(By.XPATH, "//button[text()='แสดงรายวัน']") 

botton_click.click()
time.sleep(5)

botton_click = driver.find_element(By.XPATH, "//button[text()='แสดงรายสัปดาห์']") 

botton_click.click()
time.sleep(5)

botton_click = driver.find_element(By.XPATH, "//button[text()='แสดงรายเดือน']") 

botton_click.click()
time.sleep(5)

