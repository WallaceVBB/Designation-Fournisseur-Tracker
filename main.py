from playwright.sync_api import sync_playwright
from scrapers.sysco import SyscoScraper
from scrapers.pomona_episaveurs import PomonaEpisaveursScraper
#from scrapers.pomona_terreazur import PomonaTerreAzurScraper
#from scrapers.pomona_passionfroid import PomonaPassionFroidScraper

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled","--no-sandbox", "--disable-dev-shm-usage"]
        )

        #Teste para Pomona
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="fr-FR",
            timezone_id="Europe/Paris"
        )

        page = context.new_page()

        # Changez variable "Fournisseur" pour tester différents scrapers
        Fournisseur = "Pomona Episaveurs" 
        
        if Fournisseur == "Sysco": # OK
            scraper = SyscoScraper(page)
            scraper.run()
            scraper.save_to_csv("donnees_fournisseurs/donnees_sysco.csv")

        if Fournisseur == "Pomona Episaveurs":
            scraper = PomonaEpisaveursScraper(page)
            scraper.run()
            scraper.save_to_csv("donnees_fournisseurs/donnees_pomona_episaveurs.csv")

        if Fournisseur == "Pomona TerreAzur":
            scraper = PomonaTerreAzurScraper(page)
            scraper.run()
            scraper.save_to_csv("donnees_fournisseurs/donnees_pomona_terreazur.csv")

        if Fournisseur == "Pomona PassionFroid":
            scraper = PomonaPassionFroidScraper(page)
            scraper.run()
            scraper.save_to_csv("donnees_fournisseurs/donnees_pomona_passionfroid.csv")

        browser.close()

if __name__ == "__main__":
    main()