from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from corts import Court

courts = {}
today = datetime.now()
day_of_month = today.day
print(f"Dzisiejszy dzień miesiąca to: {day_of_month}")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hastalavista.pl/rezerwacje/?type=badminton")



elements = driver.find_elements(By.CSS_SELECTOR, "div.court__item.rez_wolne")

hour_to_select = driver.find_element(By.CSS_SELECTOR, "label.rangeHours__label[for='rez_do_7_16_b']")
hour_to_select.click()

time.sleep(1)

for i in range(int(day_of_month), 32):
    calendar_icon = driver.find_element(By.CSS_SELECTOR, "div.rangeDate__icon")
    calendar_icon.click()
    time.sleep(1)

    try:
        # day_to_select = driver.find_element(By.XPATH, f"//a[@class='ui-state-default' and text()='{str(i)}']")
        day_to_select = driver.find_element(By.XPATH, f"//a[contains(@class, 'ui-state-default') and text()='{str(i)}']")

        day_to_select.click()
        time.sleep(1)

        elements = driver.find_elements(By.CSS_SELECTOR, "div.court__item.rez_wolne")

        for element in elements:
            # Wyszukaj element input wewnątrz div o klasie "court__item rez_wolne"
            input_element = element.find_element(By.CSS_SELECTOR, "input.court__input--free")

            # Pobierz godziny z atrybutów `data-godz_od` i `data-godz_do`
            godz_od = input_element.get_attribute("data-godz_od")
            godz_do = input_element.get_attribute("data-godz_do")
            court_number = int(input_element.get_attribute("data-court-number"))

            # Dodaj godziny do odpowiedniego kortu
            if court_number not in courts:
                courts[court_number] = Court(court_number)

            courts[court_number].add_free_time(godz_od, godz_do, i)


    except NoSuchElementException:
        print(f"Dzień {i} nie został znaleziony, ponieważ taki dzień nie istnieje na stronie.")
        break

for court in courts.values():
    free_days = court.has_free_time_longer_than_hour()
    if free_days:
        print(f"Kort {court.court_number} jest wolny przez ponad godzinę w dniach: {', '.join(map(str, free_days))}.")
    else:
        print(f"Kort {court.court_number} nie jest wolny przez ponad godzinę.")
# Zamknij przeglądarkę
driver.quit()