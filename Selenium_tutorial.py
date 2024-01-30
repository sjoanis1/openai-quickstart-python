from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# https://scrapfly.io/blog/web-scraping-with-selenium-and-python/
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


# configure webdriver
options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen
# configure chrome browser to not load images and javascript
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.images": 2}
)

driver = webdriver.Chrome(options=options, chrome_options=chrome_options)
driver.get("https://www.twitch.tv/directory/game/Art")
# wait for page to load
element = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=directory-first-item]'))
)
#print(driver.page_source)


sel = Selector(text=driver.page_source)
parsed = []
for item in sel.xpath("//div[contains(@class,'tw-tower')]/div[@data-target]"):
    parsed.append({
        'title': item.css('h3::text').get(),
        'url': item.css('.tw-link::attr(href)').get(),
        'username': item.css('.tw-link::text').get(),
        'tags': item.css('.tw-tag ::text').getall(),
        'viewers': ''.join(item.css('.tw-media-card-stat::text').re(r'(\d+)')),
    })

driver.quit()


# -------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.twitch.tv/")
search_box = driver.find_element_by_css_selector('input[aria-label="Search Input"]') 
search_box.send_keys(
    'fast painting'
)
# either press the enter key
search_box.send_keys(Keys.ENTER)
# or click search button
search_button = driver.find_element_by_css_selector('button[icon="NavSearch"]')
search_button.click()

driver.quit()


