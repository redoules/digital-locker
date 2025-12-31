# Implementation Plan: Work Clothes Tracker

## Overview

Plan d'implémentation pour l'application de suivi de vêtements au travail avec Django, HTMX, Flowbite, Tailwind CSS et authentification OAuth (Google, GitHub, Strava).

## Tasks

- [-] 1. Configuration du projet Django
  - [x] 1.1 Initialiser le projet Django et l'application principale
    - Créer le projet `work_clothes_tracker` et l'app `clothing`
    - Configurer les settings de base (INSTALLED_APPS, TEMPLATES, STATIC, MEDIA)
    - _Requirements: 6.1, 6.2, 6.3_
  - [x] 1.2 Installer et configurer les dépendances
    - Installer django-allauth, Pillow, django-htmx
    - Configurer requirements.txt
    - _Requirements: 1.1, 1.2_
  - [ ] 1.3 Configurer Tailwind CSS et Flowbite
    - Installer django-tailwind ou configurer Tailwind standalone
    - Ajouter Flowbite via CDN ou npm
    - _Requirements: 7.1, 7.2, 7.3_

- [ ] 2. Modèles de données
  - [ ] 2.1 Créer le modèle ClothingItem
    - Implémenter les champs: name, type, color, photo, deposit_date, location, status, notes
    - Ajouter la relation ForeignKey vers User
    - Configurer les choix pour Type et Status
    - _Requirements: 2.1, 3.1, 4.1, 4.2_
  - [ ] 2.2 Écrire les tests property-based pour le modèle ClothingItem
    - **Property 11: Persistance des modifications (round-trip)**
    - **Validates: Requirements 4.3, 6.1, 6.2, 6.3**
  - [ ] 2.3 Créer le modèle UserProfile (optionnel)
    - Implémenter les champs: user, avatar, provider
    - _Requirements: 1.7_
  - [ ] 2.4 Créer et appliquer les migrations
    - Générer les migrations avec makemigrations
    - Appliquer avec migrate
    - _Requirements: 6.1_

- [ ] 3. Authentification avec django-allauth
  - [ ] 3.1 Configurer django-allauth dans settings.py
    - Ajouter les backends d'authentification
    - Configurer SOCIALACCOUNT_PROVIDERS pour Google, GitHub, Strava
    - Définir les paramètres ACCOUNT_*
    - _Requirements: 1.1, 1.2, 1.7_
  - [ ] 3.2 Configurer les URLs d'authentification
    - Inclure allauth.urls dans urls.py
    - _Requirements: 1.4, 1.5_
  - [ ] 3.3 Écrire les tests pour l'authentification
    - **Property 1: Authentification requise pour l'accès**
    - **Property 2: OAuth et authentification locale**
    - **Validates: Requirements 1.1, 1.2, 1.4, 1.7**
  - [ ] 3.4 Créer les templates d'authentification personnalisés
    - Créer account/login.html avec boutons OAuth et formulaire local
    - Créer account/signup.html
    - Créer account/logout.html
    - Appliquer le style Flowbite/Tailwind
    - _Requirements: 1.1, 1.2, 7.1, 7.2, 7.3_

- [ ] 4. Checkpoint - Vérifier l'authentification
  - Ensure all tests pass, ask the user if questions arise.
  - Vérifier que la connexion locale et OAuth fonctionnent

- [ ] 5. Vues et templates de l'application
  - [ ] 5.1 Créer le template de base (base.html)
    - Inclure Tailwind CSS et Flowbite
    - Ajouter HTMX
    - Créer la navigation avec info utilisateur et logout
    - _Requirements: 7.1, 7.2, 7.3_
  - [ ] 5.2 Implémenter ClothingListView
    - Filtrer par utilisateur connecté et status "au_travail"
    - Trier par deposit_date décroissant
    - Supporter les requêtes HTMX (retourner partiel)
    - _Requirements: 2.1, 2.2_
  - [ ] 5.3 Écrire les tests property-based pour la liste
    - **Property 3: Isolation des données utilisateur**
    - **Property 4: Liste filtrée par statut "Au travail"**
    - **Property 5: Tri par date de dépôt décroissante**
    - **Validates: Requirements 1.6, 2.1, 2.2**
  - [ ] 5.4 Créer les templates de liste
    - clothing/list.html - page principale
    - clothing/partials/item.html - carte d'un vêtement
    - clothing/partials/item_list.html - liste pour HTMX swap
    - _Requirements: 2.1, 2.3, 2.4, 7.1_

- [ ] 6. Formulaire d'ajout de vêtement
  - [ ] 6.1 Créer ClothingItemForm
    - Définir les champs du formulaire
    - Ajouter la validation (nom non vide, etc.)
    - Gérer l'upload de photo
    - _Requirements: 3.1, 3.2, 3.3_
  - [ ] 6.2 Implémenter ClothingCreateView
    - Associer automatiquement l'utilisateur connecté
    - Définir les valeurs par défaut (status, deposit_date)
    - Retourner le nouvel item en HTML pour HTMX
    - _Requirements: 3.1, 3.4, 3.5_
  - [ ] 6.3 Écrire les tests property-based pour la création
    - **Property 7: Création d'un vêtement valide avec propriétaire**
    - **Property 8: Rejet des noms vides**
    - **Property 9: Valeurs par défaut à la création**
    - **Validates: Requirements 3.1, 3.2, 3.4, 3.5**
  - [ ] 6.4 Créer le template du formulaire
    - clothing/partials/form.html - modal Flowbite
    - Intégrer l'upload de photo
    - _Requirements: 3.1, 3.3, 7.1_

- [ ] 7. Modification du statut
  - [ ] 7.1 Implémenter ClothingUpdateStatusView
    - Vérifier que l'utilisateur possède l'item
    - Mettre à jour le statut (récupéré/perdu)
    - Retourner une réponse HTMX pour supprimer l'item de la liste
    - _Requirements: 4.1, 4.2, 4.3, 4.4_
  - [ ] 7.2 Écrire les tests property-based pour le changement de statut
    - **Property 10: Changement de statut avec vérification de propriété**
    - **Validates: Requirements 4.1, 4.2, 4.4**
  - [ ] 7.3 Ajouter les boutons de statut dans item.html
    - Bouton "Récupéré" avec hx-post
    - Bouton "Perdu" avec hx-post
    - _Requirements: 4.1, 4.2_

- [ ] 8. Checkpoint - Vérifier les fonctionnalités CRUD
  - Ensure all tests pass, ask the user if questions arise.
  - Tester l'ajout, l'affichage et le changement de statut

- [ ] 9. Recherche et filtrage
  - [ ] 9.1 Implémenter ClothingSearchView
    - Filtrer par nom (recherche textuelle)
    - Filtrer par type, couleur, lieu, statut
    - Combiner les filtres avec AND
    - Retourner la liste filtrée en HTML partiel
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6_
  - [ ] 9.2 Écrire les tests property-based pour le filtrage
    - **Property 12: Filtrage par champ unique avec isolation utilisateur**
    - **Property 13: Recherche par nom avec isolation utilisateur**
    - **Property 14: Combinaison de filtres avec AND et isolation utilisateur**
    - **Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6**
  - [ ] 9.3 Créer le template des filtres
    - clothing/partials/filters.html
    - Barre de recherche avec hx-get
    - Dropdowns pour type, couleur, lieu, statut
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 7.1_

- [ ] 10. Affichage des photos
  - [ ] 10.1 Configurer le stockage des médias
    - Définir MEDIA_URL et MEDIA_ROOT
    - Configurer les URLs pour servir les médias en développement
    - _Requirements: 3.3_
  - [ ] 10.2 Écrire les tests pour l'affichage des photos
    - **Property 6: Affichage photo ou placeholder**
    - **Validates: Requirements 2.3, 2.4**
  - [ ] 10.3 Implémenter l'affichage conditionnel dans item.html
    - Afficher la photo si présente
    - Afficher un placeholder basé sur le type sinon
    - _Requirements: 2.3, 2.4_

- [ ] 11. Responsive et finitions UI
  - [ ] 11.1 Optimiser le layout mobile-first
    - Adapter les grilles pour mobile/desktop
    - Vérifier les tap targets
    - _Requirements: 7.1, 7.2, 7.3_
  - [ ] 11.2 Ajouter les états de chargement HTMX
    - Indicateurs de chargement
    - Transitions fluides
    - _Requirements: 7.1_

- [ ] 12. Checkpoint final
  - Ensure all tests pass, ask the user if questions arise.
  - Vérifier toutes les fonctionnalités end-to-end
  - Tester sur mobile et desktop

## Notes

- All tasks including tests are required for comprehensive coverage
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties
- Unit tests validate specific examples and edge cases
- Django-allauth handles OAuth complexity automatically
