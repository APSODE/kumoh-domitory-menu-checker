import json

import requests
from selenium import webdriver
from bs4 import BeautifulSoup, element
from typing import Optional, Dict, List


class MenuCheckerSelenium:
    def __init__(self, debug_mode: bool = False):
        self._webdriver = webdriver.Chrome(
            "chromedriver.exe",
            options=self._ChromeDriverOption() if debug_mode is False else None
        )

        self._dormitory_menu_url = "https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do"

    @staticmethod
    def _ChromeDriverOption() -> webdriver.ChromeOptions:
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        option.add_argument("--disable-gpu")
        option.add_argument("--no-sandbox")
        return option

    def Start(self):
        self._webdriver.get(self._dormitory_menu_url)
        breakpoint()
        self._webdriver.quit()


class MenuChecker:
    def __init__(self):
        self._dormitory_menu_url = "https://dorm.kumoh.ac.kr/dorm/restaurant_menu01.do"
        self._menu_data = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": []
        }
        self._start()

    @staticmethod
    def _get_site_html(site_url: str) -> Optional[BeautifulSoup]:
        site_response = requests.get(site_url)

        if site_response.status_code == 200:
            return BeautifulSoup(site_response.text, "html.parser")

        else:
            raise ConnectionError(f"response status code is not 200!!\n"
                                  f"current status code : {site_response.status_code}")

    def _start(self):
        site_html = self._get_site_html(site_url = self._dormitory_menu_url)
        menu_table_html = site_html.find("table", {"class": "smu-table tb-w150"})

        for key, menu_html_per_day in enumerate(menu_table_html.find_all("td")):
            self._menu_data[str(key if key < 7 else key - 7)].append(menu_html_per_day.text)

        self._create_menu_data_file()

    def _create_menu_data_file(self):
        extracted_menu_data = {}

        for key, menu_data in self._menu_data.items():
            day_of_the_week = ""

            if key == "0":
                day_of_the_week = "월요일"

            elif key == "1":
                day_of_the_week = "화요일"

            elif key == "2":
                day_of_the_week = "수요일"

            elif key == "3":
                day_of_the_week = "목요일"

            elif key == "4":
                day_of_the_week = "금요일"

            elif key == "5":
                day_of_the_week = "토요일"

            elif key == "6":
                day_of_the_week = "일요일"

            extracted_menu_data.update(
                {
                    key: {
                        "dotw": day_of_the_week,
                        "launch": self._menu_data.get(key)[0],
                        "dinner": self._menu_data.get(key)[1]
                    }
                }
            )

        with open("menu_data.json", "w", encoding = "utf-8") as write_file:
            json.dump(extracted_menu_data, write_file, indent = 4, ensure_ascii = False)









if __name__ == '__main__':
    # MC = MenuChecker_Selenium(debug_mode = True)
    # MC.Start()

    MenuChecker()

