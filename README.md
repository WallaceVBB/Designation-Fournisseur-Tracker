# Designation-Fournisseur-Tracker
Ce logiciel est un appui au Projet Cantine Numérique, le fournissant une base de données pour l'entraînement de sont modèle de Machine Learning.

# 🧾 Designation Fournisseur Tracker

Le **Designation Fournisseur Tracker** est un outil de web scraping développé en **Python avec Playwright**, destiné à extraire et structurer les **désignations de produits alimentaires** à partir de sites de **grossistes (fournisseurs)** de la restauration collective en France.

Ce projet vise à faciliter les travaux de **qualité des données**, **matching de produits**, **entraînemente de modèles de Machine Learning** dans des contextes de d’achats alimentaires responsables.

---

## 🚚 Fournisseurs supportés

À ce jour, les fournisseurs suivants supportés par le logiciel :

- ✅ **Sysco France**
- ✅ **Pomona – Épisaveurs**
- ✅ **Pomona – TerreAzur**
- ✅ **Pomona – PassionFroid**

L’architecture du projet permet d’ajouter facilement de nouveaux fournisseurs.

---

## 🗂️ Structure du projet

Designation-Fournisseur-Tracker/
│
├── main.py
├── scrapers/
│ ├── base.py
│ ├── sysco.py
│ ├── pomona_episaveurs.py
│ └── (autres fournisseurs...)
│
├── données_fournisseurs/
│ ├── donnees_sysco.csv
│ ├── donnees_pomona_episaveurs.csv
│ └── (autres fournisseurs...)
│
├── requirements.txt
├── LICENCE.txt
└── README.md


---

## ⚙️ Fonctionnalités

- Navigation automatisée avec **Playwright**
- Gestion robuste des bannières de consentement cookies (Didomi, OneTrust)
- Scraping multi-sections (ex. : épicerie, boissons)
- Extraction des champs suivants :
  - `designation`
  - `reference`
  - `url_product`
  - `fournisseur`
- Export des résultats au format **CSV**
- Architecture orientée **1 fournisseur = 1 scraper**

---
## 📦 Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/WallaceVBB/Designation-Fournisseur-Tracker.git
cd Designation-Fournisseur-Tracker

### 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt

### 3️⃣ Installer Playwright
playwright install
```
---
## Contribution
Ce projet est ouvert à contributions. N’hésitez pas à proposer des idées, rapports de bugs, ou améliorations via les issues ou pull requests.

---
## Licence
MIT (2025).
