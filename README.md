# TP Selenium - Automatisation Web

Ce projet a pour objectif d’automatiser des parcours utilisateurs sur deux sites web dédiés aux tests d’automatisation : **SauceDemo** et **Automation Practice**. Il met en œuvre des scripts Python utilisant Selenium pour simuler des actions humaines telles que la connexion, la navigation, la recherche de produits, l’ajout au panier, la soumission de formulaires et la vérification d’états.

---

## Structure du projet

Le dossier contient les fichiers suivants :

- `login_and_list_products.py`
- `add_to_cart_and_checkout.py`
- `sort_products.py`
- `register_user.py`
- `search_and_add_to_cart.py`
- `contact_form.py`
- `credentials.txt` (généré automatiquement)
- `README.md`

---

## Partie 1 : Automatisation sur SauceDemo

### `login_and_list_products.py`

Ce script se connecte au site [https://www.saucedemo.com](https://www.saucedemo.com) avec les identifiants `standard_user` / `secret_sauce`. Une fois authentifié, il récupère et affiche dans le terminal les noms des six produits disponibles sur la page d’accueil.

### `add_to_cart_and_checkout.py`

Ce script effectue une connexion identique, ajoute deux produits au panier, puis procède au checkout. Il remplit les champs requis (prénom, nom, code postal) et vérifie que le message de confirmation "THANK YOU FOR YOUR ORDER" s’affiche.

### `sort_products.py`

Ce script se connecte, applique le tri "Price (low to high)", puis récupère et affiche les noms et prix des trois produits les moins chers.

---

## Partie 2 : Automatisation sur Automation Practice

### `register_user.py`

Ce script accède à [https://automationexercise.com](https://automationexercise.com), clique sur "Signup / Login", puis crée un nouvel utilisateur avec un nom et un email générés aléatoirement. Il remplit l’ensemble du formulaire d’inscription (titre, mot de passe, date de naissance, coordonnées, etc.) et vérifie que le message "ACCOUNT CREATED!" s’affiche. Les identifiants sont sauvegardés dans `credentials.txt`.

### `search_and_add_to_cart.py`

Après connexion avec les identifiants stockés dans `credentials.txt`, ce script navigue vers la page des produits, recherche des articles contenant le mot-clé "dress", sélectionne deux produits différents et les ajoute au panier. Il accède ensuite au panier et vérifie que les deux produits sont présents.

### `contact_form.py`

Ce script accède à la section "Contact us", remplit le formulaire avec un nom, une adresse email, un objet et un message, puis joint un fichier texte généré dynamiquement. Il soumet le formulaire, gère l’alerte JavaScript qui apparaît, et vérifie que le message de confirmation s’affiche. Une capture d’écran est prise à la fin.

---

## Dépendances

Les bibliothèques suivantes sont nécessaires :

- `selenium` : pour l’automatisation du navigateur
- `webdriver-manager` : pour la gestion automatique du driver Firefox (geckodriver)

Installation :

```bash
pip install selenium webdriver-manager