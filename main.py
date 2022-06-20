import threading
import time
import json

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class main():
    def __init__(self):
        chrome_driver = './chromedriver.exe'  # chromedriver的文件位置
        self.web = webdriver.Chrome(executable_path=chrome_driver)
        self.web.get("https://ding.cjfx.cn/f/bndro9sv")

        self.web.implicitly_wait(30)
        with open('./setting.json', encoding="utf-8") as f:
            self.json_data = json.load(f)
        # print(self.json_data)

        self.into_form()

    def into_form(self):

        self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[2]/div/span').click()

        self.web.find_element(by=By.CLASS_NAME, value="btn").click()

        # 登录
        self.web.find_element(by=By.ID, value="mobile").send_keys(self.json_data["账号"])
        self.web.find_element(by=By.ID, value="pwd").send_keys(self.json_data["密码"])
        self.web.find_element(by=By.ID, value="loginBtn").click()
        # time.sleep(3)
        WebDriverWait(self.web, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="userConfirmBtn')))
        self.web.find_element(by=By.XPATH, value='//*[@id="userConfirmBtn"]').click()

        t = threading.Thread(target=self.write_form)  # 基础信息
        t2 = threading.Thread(target=self.write_location)  # 地址
        t3 = threading.Thread(target=self.write_location_sleep)  # 外宿地址
        t4 = threading.Thread(target=self.click_no)  # 全部选否
        t.start()
        t2.start()
        t3.start()
        t4.start()
        t.join()
        t2.join()
        t3.join()
        t4.join()

        # 提交
        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[58]/div/div/button').click()

        self.web.close()

    def write_location(self):
        # 今日所在地区
        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[9]/div/div[3]/ul/li[1]/label/div/span[1]'). \
            click()
        # 今日所在城市
        # 省份
        select = Select(self.web.find_element(by=By.XPATH,
                                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[12]/div/div[3]/div/div/label[1]/select'))
        select.select_by_visible_text(self.json_data["地区"]['省份'])
        time.sleep(1)
        select = Select(self.web.find_element(by=By.XPATH,
                                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[12]/div/div[3]/div/div/label[2]/select'))
        select.select_by_visible_text(self.json_data["地区"]['市'])
        time.sleep(1)
        select = Select(self.web.find_element(by=By.XPATH,
                                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[12]/div/div[3]/div/div/label[3]/select'))
        select.select_by_visible_text(self.json_data["地区"]['区'])
        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[12]/div/div[3]/label/input').send_keys(
            self.json_data["地区"]['详细地址'])

        # 是否为风险地区
        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[13]/div/div[3]/ul/li[2]/label').click()

    def write_location_sleep(self):
        # 内宿/外宿
        if self.json_data["外宿/内宿"] == '外宿':
            self.web.find_element(by=By.XPATH, value="//*[text()='外宿']").click()
            time.sleep(1)
            select = Select(self.web.find_element(by=By.XPATH,
                                                  value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[31]/div/div[3]/div/div/label[1]/select'))
            select.select_by_visible_text(self.json_data["地区"]['省份'])
            time.sleep(1)
            select = Select(self.web.find_element(by=By.XPATH,
                                                  value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[31]/div/div[3]/div/div/label[2]/select'))
            select.select_by_visible_text(self.json_data["地区"]['市'])
            time.sleep(1)
            select = Select(self.web.find_element(by=By.XPATH,
                                                  value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[31]/div/div[3]/div/div/label[3]/select'))
            select.select_by_visible_text(self.json_data["地区"]['区'])
            self.web.find_element(by=By.XPATH,
                                  value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[31]/div/div[3]/label/input').send_keys(
                self.json_data['详细地址'])

    def write_form(self):
        # 工号
        self.web.find_element(by=By.CLASS_NAME, value="mui-input").send_keys(self.json_data["工号"])
        # 获取位置
        self.web.find_element(by=By.CLASS_NAME, value="field-geo__toggle").click()
        # 性别
        self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''性别''']}']").click()
        # 隶属公司
        self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''隶属''']}']").click()
        # 中心
        self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''中心''']}']").click()
        # 部门
        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[8]/div/div[3]/label/input'). \
            send_keys(self.json_data["部门"])

        # 是否在岗
        if self.json_data['''上班情况''']['''全天在岗''']:
            WebDriverWait(self.web, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[text()="全天在岗"')))
            self.web.find_element(by=By.XPATH, value=f"//*[text()='全天在岗']").click()
            # time.sleep(1)
            # 若在岗
            # 班次

            WebDriverWait(self.web, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"/*[text()='{self.json_data['''上班情况''']['''班次''']}']")))
            self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''上班情况''']['''班次''']}']").click()
            # 厂区
            WebDriverWait(self.web, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"/*[text()='{self.json_data['''上班情况''']['''厂区''']}']")))
            self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''上班情况''']['''厂区''']}']").click()
            # 交通工具
            WebDriverWait(self.web, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"/*[text()='{self.json_data['''上班情况''']['''步行''']}']")))
            self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''上班情况''']['''步行''']}']").click()
            # time.sleep(1)

        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[32]/div/div[3]/ul/li[1]/label/div/span[1]').click()
        # # 是否正常
        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[33]/div/div[3]/ul/li[1]/label/div').click()
        # # 12 否
        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[36]/div/div[3]/ul/li[2]/label/div/span[1]').click()
        # # 13 否
        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[40]/div/div[3]/ul/li[2]/label/div').click()
        # # 14 否
        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[42]/div/div[3]/ul/li[2]/label/div').click()
        # # 15 否
        # self.web.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[44]/div/div[3]/ul/li[2]/label/div').click()

        # 疫苗
        WebDriverWait(self.web, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[50]/div/div[3]/ul/li[1]/label/div/span[1]')))

        self.web.find_element(by=By.XPATH,
                              value='//*[@id="app"]/div/div[3]/div/article/div/section/div[1]/div[50]/div/div[3]/ul/li[1]/label/div/span[1]').click()

        WebDriverWait(self.web, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              f"//*[text()='{self.json_data['''上班情况''']['''交通工具''']}']")))
        self.web.find_element(by=By.XPATH, value=f"//*[text()='{self.json_data['''上班情况''']['''交通工具''']}']").click()

    def click_no(self):
        """ 是否异常，是否和家人朋友见面 默认填否 """
        # 是否异常
        for i in self.web.find_elements(by=By.XPATH, value="//*[text()='否']"):
            i.click()


if __name__ == '__main__':
    main()
