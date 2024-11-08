from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from courts import Court

courts = {}
today = datetime.now()
day_of_month = today.day
print(f"Dzisiejszy dzień miesiąca to: {day_of_month}")

days_time = ['rez_do_7_16_b', 'rez_od_11_20_b', 'rez_od_15_24_b']


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hastalavista.pl/rezerwacje/?type=badminton")

stop = False

for day_time in days_time:
    if stop:
        break
    hour_to_select = driver.find_element(By.CSS_SELECTOR, f"label.rangeHours__label[for={day_time}]")
    hour_to_select.click()

    time.sleep(1)

    for day in range(int(day_of_month), 32):
        if stop:
            break
        calendar_icon = driver.find_element(By.CSS_SELECTOR, "div.rangeDate__icon")
        calendar_icon.click()
        time.sleep(1)

        try:
            day_to_select = driver.find_element(By.XPATH, f"//a[contains(@class, 'ui-state-default') and text()='{str(day)}']")
            day_to_select.click()
            time.sleep(1)

            elements = driver.find_elements(By.CSS_SELECTOR, "div.court__item.rez_wolne")

            for element in elements:
                input_element = element.find_element(By.CSS_SELECTOR, "input.court__input--free")
                godz_od = input_element.get_attribute("data-godz_od")
                godz_do = input_element.get_attribute("data-godz_do")
                court_number = int(input_element.get_attribute("data-court-number"))

                if court_number not in courts:
                    courts[court_number] = Court(court_number)

                courts[court_number].add_free_time(godz_od, godz_do, day)


        except NoSuchElementException:
            print(f"Dzień {day} nie istnieje na stronie.")
            stop = True
            break


all_free_slots = []
for court in courts.values():
    free_slots = court.get_free_time_slots_longer_than_hour()
    for day, start, end in free_slots:
        all_free_slots.append((day, start, end, court.court_number))

all_free_slots.sort(key=lambda slot: slot[0])

for day, start, end, court_number in all_free_slots:
    start_time = start.strftime("%H:%M")
    end_time = end.strftime("%H:%M")
    print(f"W dniu {day} od godziny {start_time} do {end_time} kort {court_number} jest wolny.")

driver.quit()