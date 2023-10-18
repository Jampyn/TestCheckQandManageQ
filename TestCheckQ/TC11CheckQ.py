import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckQueueTest(unittest.TestCase):

    
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
         id_input.send_keys("1739901969649")
         password_input.send_keys("123456")
         time.sleep(5)

         # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
         login_button = self.driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
         login_button.click()

         # คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID ที่กำหนดให้
         login_button = self.driver.find_element(By.ID, "Login")
         login_button.click()
         # รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
         time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

         # คลิกปุ่ม "รายการจองคิว" โดยใช้ XPath
         queue_list_button = self.driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")
         queue_list_button.click()
         time.sleep(5)

         # คลิกที่ input ประเภทวันที่ (type="date")
         date_input = self.driver.find_element(By.ID, "TableBookDate")
         date_input.click()
         
         # ตั้งค่าวันที่เป็นวันนี้หรือวันที่เรากำหนดเอง (สามารถใช้วิธีอื่น ๆ ในการตั้งค่าวันที่ตามที่คุณต้องการ)
         # date_input.clear()
         date_input.send_keys("10-27-2023")  # เอาเป็นวันเดือนปีนะจ๊ะ ต้องดูด้วยว่าแต่ละเครื่องวันเดือนปีเรียงกันยังไงด้วย
         time.sleep(5)

         # เลือกแผนกใน dropdown ที่คุณต้องการ (เช่น "ทั่วไป") โดยใช้ ID
         department_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedDepartment"))
         # เลือกแผนกที่คุณต้องการ (เช่น "ทั่วไป")
         department_dropdown.select_by_visible_text("ผิวหนัง")
         time.sleep(5)

         # เลือกคิวที่ dropdown โดยใช้ ID (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว ) 
         queue_status_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedStatusId"))
         # เลือกคิวที่คุณต้องการ (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว ) 
         queue_status_dropdown.select_by_value("1")
         time.sleep(5)

         # เลือกปุ่ม ปริ้นคิว โดยใช้ ID
         try:
                element = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.ID, "Manager_button_status"))
                )

                # คลิกที่ปุ่ม
                element.click()
         except Exception as e:
                print(f"เกิดข้อผิดพลาด: {e}")
         time.sleep(7)



if __name__ == "__main__":
    unittest.main()