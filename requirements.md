# Requirements Document

## Introduction

Application web/mobile légère et intuitive pour suivre les vêtements laissés au travail. L'application permet d'ajouter, visualiser, rechercher et gérer le statut des vêtements avec une interface moderne mobile-first inspirée de Flowbite.

## Glossary

- **Clothing_Item**: Un vêtement enregistré dans l'application avec ses attributs (nom, type, couleur, photo, date de dépôt, lieu, statut, notes)
- **Tracker_System**: Le système principal de l'application gérant les opérations CRUD sur les vêtements
- **Auth_System**: Le système d'authentification gérant les connexions et sessions utilisateur
- **User**: Utilisateur authentifié ayant accès à ses propres vêtements
- **Status**: État d'un vêtement parmi "Au travail", "Récupéré", "Perdu"
- **Type**: Catégorie de vêtement parmi "haut", "bas", "veste", "chaussures"
- **Location**: Lieu où le vêtement a été laissé (ex: "Bureau", "Salle de pause", "Casier n°5")

## Requirements

### Requirement 1: Authentification utilisateur

**User Story:** As a user, I want to create an account and log in securely, so that I can access my personal clothing data from anywhere.

#### Acceptance Criteria

1. WHEN a new user visits the registration page, THE Auth_System SHALL allow account creation with email and password OR OAuth provider (Google, GitHub, Strava)
2. WHEN a user provides valid credentials (local or OAuth), THE Auth_System SHALL authenticate them and create a session
3. WHEN a user provides invalid credentials, THE Auth_System SHALL reject the login and display an error message
4. WHEN an unauthenticated user tries to access the application, THE Auth_System SHALL redirect them to the login page
5. WHEN a user logs out, THE Auth_System SHALL terminate their session and redirect to the login page
6. WHEN a user is authenticated, THE Tracker_System SHALL only display their own Clothing_Items
7. WHEN a user authenticates via OAuth for the first time, THE Auth_System SHALL create a new user account automatically

### Requirement 2: Affichage de la liste des vêtements

**User Story:** As a user, I want to see all my clothes currently at work, so that I can quickly know what I have left there.

#### Acceptance Criteria

1. WHEN the user opens the home page, THE Tracker_System SHALL display a list of Clothing_Items with status "Au travail" belonging to the authenticated user
2. WHEN displaying the list, THE Tracker_System SHALL sort Clothing_Items by deposit date in descending order (most recent first)
3. WHEN a Clothing_Item has a photo, THE Tracker_System SHALL display a thumbnail of the photo in the list
4. WHEN a Clothing_Item has no photo, THE Tracker_System SHALL display a default placeholder icon based on the type

### Requirement 3: Ajout d'un nouveau vêtement

**User Story:** As a user, I want to add a new clothing item with details and optional photo, so that I can track what I leave at work.

#### Acceptance Criteria

1. WHEN the user submits a valid clothing form, THE Tracker_System SHALL create a new Clothing_Item associated with the authenticated user and add it to the list
2. WHEN the user attempts to add a Clothing_Item without a name, THE Tracker_System SHALL prevent the addition and display an error message
3. WHEN the user uploads a photo, THE Tracker_System SHALL store the image and associate it with the Clothing_Item
4. WHEN a new Clothing_Item is created without a deposit date, THE Tracker_System SHALL set the deposit date to the current date
5. WHEN a new Clothing_Item is created, THE Tracker_System SHALL set the default status to "Au travail"

### Requirement 4: Modification du statut d'un vêtement

**User Story:** As a user, I want to mark a clothing item as "Récupéré" or "Perdu", so that I can track the current state of my belongings.

#### Acceptance Criteria

1. WHEN the user marks their own Clothing_Item as "Récupéré", THE Tracker_System SHALL update the status and move it out of the main list
2. WHEN the user marks their own Clothing_Item as "Perdu", THE Tracker_System SHALL update the status and move it out of the main list
3. WHEN a status change is made, THE Tracker_System SHALL persist the change immediately
4. WHEN a user tries to modify a Clothing_Item that doesn't belong to them, THE Tracker_System SHALL reject the action

### Requirement 5: Recherche et filtrage

**User Story:** As a user, I want to search and filter my clothing items, so that I can quickly find specific items.

#### Acceptance Criteria

1. WHEN the user enters a search term, THE Tracker_System SHALL filter the user's Clothing_Items by name containing the search term
2. WHEN the user selects a type filter, THE Tracker_System SHALL display only the user's Clothing_Items matching that type
3. WHEN the user selects a color filter, THE Tracker_System SHALL display only the user's Clothing_Items matching that color
4. WHEN the user selects a location filter, THE Tracker_System SHALL display only the user's Clothing_Items matching that location
5. WHEN the user selects a status filter, THE Tracker_System SHALL display only the user's Clothing_Items matching that status
6. WHEN multiple filters are applied, THE Tracker_System SHALL combine them with AND logic

### Requirement 6: Persistance des données

**User Story:** As a user, I want my clothing data to be saved, so that I can access it across sessions.

#### Acceptance Criteria

1. WHEN a Clothing_Item is added, THE Tracker_System SHALL persist it to the database immediately
2. WHEN a Clothing_Item is modified, THE Tracker_System SHALL persist the changes to the database immediately
3. WHEN the user reopens the application, THE Tracker_System SHALL restore all the user's Clothing_Items from the database

### Requirement 7: Interface responsive mobile-first

**User Story:** As a user, I want to use the application on my smartphone, so that I can manage my clothes on the go.

#### Acceptance Criteria

1. WHEN the application is viewed on a mobile device, THE Tracker_System SHALL display a responsive layout optimized for small screens
2. WHEN the application is viewed on a desktop, THE Tracker_System SHALL adapt the layout to use available space efficiently
3. THE Tracker_System SHALL provide touch-friendly buttons and controls with adequate tap targets
