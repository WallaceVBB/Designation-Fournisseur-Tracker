import re
import time
from .base import BaseScraper

class SyscoScraper(BaseScraper):

    BASE_URL = "https://shop.sysco.fr/Produits/c/produits?q=%3AnumeroOrdreTarif&text=&mode=0&page=1"

    def run(self):
        print("🚚 Scraping Sysco...")
        self.page.goto(self.BASE_URL)

        self.accept_cookies()
        page_num = 1

        while True:
            
            print(f"\n📄 Page {page_num}")
            
            self.page.wait_for_selector("div.product-row", timeout=10000)

            products = self.page.locator("div.product-row").all()

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
            "Fournisseur": "Sysco"
        }

        # Nom produit
        try:
            title = product.locator("h2, product-row__title")
            data["designation"] = title.inner_text().strip()
            print(f"Scraping produit: {data['designation']}")
        except:
            pass

        # URL
        try:
            link = product.locator("a").first
            data["url_product"] = link.get_attribute("href")
        except:
            pass

        # Référence
        try:
            ref = product.locator("span.product-row__code").first
            data["reference"] = ref.inner_text().strip()
        except:
            pass

        return data
    
    def next_page(self):
        """Aller à la page suivante avec le bouton '>'."""
        try:
            # Attendre un court instant pour s'assurer que les éléments sont chargés
            self.page.wait_for_timeout(10000)

            # Sélectionne le bouton 'next' (icône flèche droite)
            next_btn = self.page.locator("i.fa-angle-right").first
            if next_btn.count() == 0 or not next_btn.is_visible():
                return False  # s'il n'y a pas de bouton 'next', fin du scraping

            # Mémorise les URLs actuelles pour détecter le chargement de nouveaux produits
            current_urls = [p.get_attribute("href") for p in self.page.locator("div.product-row a").all()]

            next_btn.scroll_into_view_if_needed()
            next_btn.click()

            # Attendre que de nouveaux produits soient chargés
            self.page.wait_for_function(
                """(urls) => {
                    const current = Array.from(document.querySelectorAll('div.product-row a')).map(a => a.href);
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
            banner = self.page.locator("#onetrust-accept-btn-handler")
            if banner.count() > 0 and banner.first.is_visible():
                banner.first.click()
                self.page.wait_for_timeout(500)
                print("✅ Cookies acceptés")
        except:
            pass