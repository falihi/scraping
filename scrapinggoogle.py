import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def google_search(query, max_results=5):
    # Inisialisasi browser dengan undetected-chromedriver
    options = uc.ChromeOptions()
    options.add_argument("--headless")  # Opsi untuk tidak menampilkan browser (opsional)
    driver = uc.Chrome(options=options)

    try:
        # Buka Google Search
        driver.get("https://www.google.com/")
        time.sleep(2)  # Beri jeda untuk memastikan halaman terbuka sempurna

        # Cari elemen input dan masukkan query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.RETURN)
        time.sleep(2)  # Tunggu agar hasil pencarian tampil

        # Ambil hasil pencarian
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        scraped_results = []

        for result in results[:max_results]:
            try:
                title = result.find_element(By.TAG_NAME, "h3").text
                link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                scraped_results.append({"title": title, "link": link})
            except Exception as e:
                print(f"Error extracting result: {e}")

        return scraped_results

    finally:
        driver.quit()

# Contoh penggunaan
if __name__ == "__main__":
    query = "python web scraping tutorial"
    results = google_search(query, max_results=5)

    print("Hasil Pencarian:")
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result['title']} - {result['link']}")
