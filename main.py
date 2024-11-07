from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from corst import get_court_times


today = datetime.now()
day_of_month = today.day
month_number = today.month
print(f"Dzisiejszy dzień miesiąca to: {day_of_month}")
print(f"Dzisiejszy miesiąc to: {month_number}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hastalavista.pl/rezerwacje/?type=badminton")

# get_court_times(driver)


date_input = driver.find_element(By.ID, "rez_wybrana_data_hid")

elements = driver.find_elements(By.CSS_SELECTOR, "div.court__item.rez_wolne")

for element in elements:
    # Wyszukaj element input wewnątrz div o klasie "court__item rez_wolne"
    input_element = element.find_element(By.CSS_SELECTOR, "input.court__input--free")

    # Pobierz godziny z atrybutów `data-godz_od` i `data-godz_do`
    godz_od = input_element.get_attribute("data-godz_od")
    godz_do = input_element.get_attribute("data-godz_do")
    court = input_element.get_attribute("data-court-number")


    print(f"Kort: {court} Godzina od: {godz_od}, godzina do: {godz_do}")

for i in range(int(day_of_month)+1, 32):
    calendar_icon = driver.find_element(By.CSS_SELECTOR, "div.rangeDate__icon")
    calendar_icon.click()
    time.sleep(1)

    try:
        day_to_select = driver.find_element(By.XPATH, f"//a[@class='ui-state-default' and text()='{str(i)}']")
        day_to_select.click()
        time.sleep(1)

        elements = driver.find_elements(By.CSS_SELECTOR, "div.court__item.rez_wolne")

        for element in elements:
            # Wyszukaj element input wewnątrz div o klasie "court__item rez_wolne"
            input_element = element.find_element(By.CSS_SELECTOR, "input.court__input--free")

            # Pobierz godziny z atrybutów `data-godz_od` i `data-godz_do`
            godz_od = input_element.get_attribute("data-godz_od")
            godz_do = input_element.get_attribute("data-godz_do")

            print(f"dasdsadasdGodzina od: {godz_od}, godzina do: {godz_do}")
    except NoSuchElementException:
    # Jeśli nie uda się znaleźć elementu (np. szukany dzień nie istnieje)
        print(f"Dzień {i} nie został znaleziony, ponieważ taki dzień nie istnieje na stronie.")
        break

# Zamknij przeglądarkę
driver.quit()