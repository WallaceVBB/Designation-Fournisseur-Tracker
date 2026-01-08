from playwright.sync_api import sync_playwright
from scrapers.sysco import SyscoScraper

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        # 1 page = 1 fournisseur
        page = browser.new_page()

        scraper = SyscoScraper(page)
        scraper.run()
        scraper.save_to_csv("donnees_sysco.csv")

        browser.close()

if __name__ == "__main__":
    main()