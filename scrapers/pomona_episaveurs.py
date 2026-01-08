import re
import time
from .base import BaseScraper

class PomonaEpisaveursScraper(BaseScraper):

    sections = ("boissons", "epicerie")

    def run(self):
        print("🚚 Scraping Pomona Episaveurs...")
        
        for section in self.sections:
            print (f"\n🔍 Section: {section}")
            BASE_URL = f"https://www.episaveurs.fr/produits/{section}"
            self.page.goto(BASE_URL)

            self.accept_cookies()
            page_num = 1

            while True:
                
                print(f"\n📄 Page {page_num}")
                            
                self.page.wait_for_selector("div.ms-product--info-wrapper", timeout=10000) #AF : tester

                products = self.page.locator("div.ms-product--info-wrapper").all() #AF : tester

                for product in products:
                    self.data.append(self.extract_product(product))
                
                if not self.next_page():
                    print("✅ Dernière page atteinte, fin du scraping.")
                    break

                page_num += 1
                time.sleep(1)

    def extract_product(self, product):
        data = {
            "designation": None,
            "reference": None,
            "url_product": None,
            "Fournisseur": "Pomona Episaveurs"
        }

        # Nom produit
        try:
            title = product.locator("span.full-text") # AF : tester
            data["designation"] = title.inner_text().strip()
            print(f"Scraping produit: {data['designation']}")
        except:
            pass

        # URL (sans changement)
        try:
            link = product.locator("a").first #AF : tester (sans changement)
            data["url_product"] = link.get_attribute("href")
            #print(f"Scraping url: {data['url_product']}")
        except:
            pass

        # Référence
        try:
            ref = product.locator("span.ms-product--article-code").first #AF : tester
            data["reference"] = ref.inner_text().strip()
            #print(f"Scraping reference: {data['reference']}")
        except:
            pass

        return data
    
    def next_page(self):
        """Aller à la page suivante avec le bouton '>'."""
        try:
            # Attendre un court instant pour s'assurer que les éléments sont chargés
            self.page.wait_for_timeout(10000)

            # Sélectionne le bouton 'next' (icône flèche droite)
            next_btn = self.page.locator("i.fa-chevron-right").first #AF : tester
            if next_btn.count() == 0 or not next_btn.is_visible():
                return False  # s'il n'y a pas de bouton 'next', fin du scraping

            # Mémorise les URLs actuelles pour détecter le chargement de nouveaux produits
            current_urls = [p.get_attribute("href") for p in self.page.locator("div.ms-product a").all()] #AF : adapter

            next_btn.scroll_into_view_if_needed()
            next_btn.click()

            # Attendre que de nouveaux produits soient chargés
            self.page.wait_for_function(
                """(urls) => {
                    const current = Array.from(document.querySelectorAll('div.ms-product a')).map(a => a.href);
                    return current.some(u => !urls.includes(u));
                }""",
                arg=current_urls,
                timeout=10000
            )

            return True
        except:
            return False

    def accept_cookies(self):
        try:
            btn = self.page.locator("#didomi-notice-agree-button") #AF : tester
            if btn.is_visible():
                btn.click()
                self.page.wait_for_timeout(500)
                print("✅ Cookies acceptés")
        except:
            print("⚠️ Cookies Didomi non affichés ou déjà acceptés")