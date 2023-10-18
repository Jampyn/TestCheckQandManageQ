import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ManageReportTest(unittest.TestCase):
 

 def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()

        # ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
        self.driver.maximize_window()

 def tearDown(self):
        # Close the browser( ทำการปิดเบราว์เซอร์ )
        self.driver.quit()

        # รอสักครู่เพื่อให้หน้าเว็บปิดอย่างถูกต้อง
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//button[text()='แสดงรายวัน']")))

 def test_ManageReport_in_Q_Online(self):
        # Open the web application ( ทำการเปิดเว็บแอพตาม url ที่กำหนด )
        self.driver.get("https://online-web-mauve.vercel.app/")

        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID ที่กำหนดให้
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()
        # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
        time.sleep(5) 

        # คลิกปุ่ม แสดงรายวัน
        botton_click = self.driver.find_element(By.XPATH, "//button[text()='แสดงรายวัน']") 
        botton_click.click()
        time.sleep(5)

        # คลิกปุ่ม แสดงรายสัปดาห์
        botton_click = self.driver.find_element(By.XPATH, "//button[text()='แสดงรายสัปดาห์']") 
        botton_click.click()
        time.sleep(5)

        # คลิกปุ่ม แสดงรายเดือน
        botton_click = self.driver.find_element(By.XPATH, "//button[text()='แสดงรายเดือน']") 
        botton_click.click()
        time.sleep(5)



if __name__ == "__main__":
    unittest.main()