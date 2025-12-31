# Configuration OAuth - Work Clothes Tracker

## Vue d'ensemble

L'application supporte l'authentification via :
- **Email/Mot de passe** (authentification locale Django)
- **Google OAuth 2.0**
- **GitHub OAuth**
- **Strava OAuth**

## Configuration des providers OAuth

### 1. Google OAuth

1. Aller sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créer un nouveau projet ou sélectionner un projet existant
3. Activer l'API Google+ 
4. Créer des credentials OAuth 2.0 :
   - Type : Application Web
   - URIs de redirection autorisées :
     - `http://localhost:8000/accounts/google/login/callback/`
     - `https://votre-domaine.com/accounts/google/login/callback/` (production)
5. Copier le Client ID et Client Secret

### 2. GitHub OAuth

1. Aller sur [GitHub Developer Settings](https://github.com/settings/developers)
2. Cliquer sur "New OAuth App"
3. Remplir les informations :
   - Application name : Work Clothes Tracker
   - Homepage URL : `http://localhost:8000`
   - Authorization callback URL : `http://localhost:8000/accounts/github/login/callback/`
4. Copier le Client ID et générer un Client Secret

### 3. Strava OAuth

1. Aller sur [Strava API Settings](https://www.strava.com/settings/api)
2. Créer une nouvelle application
3. Remplir les informations :
   - Application Name : Work Clothes Tracker
   - Authorization Callback Domain : `localhost` (ou votre domaine)
4. Copier le Client ID et Client Secret

## Configuration dans Django

### Méthode 1 : Via l'interface Admin Django

1. Lancer le serveur : `uv run python manage.py runserver`
2. Créer un superuser : `uv run python manage.py createsuperuser`
3. Aller sur `http://localhost:8000/admin/`
4. Dans "Sites", modifier le site par défaut :
   - Domain name : `localhost:8000` (ou votre domaine)
   - Display name : Work Clothes Tracker
5. Dans "Social applications", ajouter les applications :
   - Provider : Google (ou GitHub, Strava)
   - Name : Google (ou GitHub, Strava)
   - Client id : [votre client ID]
   - Secret key : [votre secret]
   - Sites : Sélectionner votre site

### Méthode 2 : Via variables d'environnement (recommandé)

1. Copier `.env.example` vers `.env`
2. Remplir les credentials OAuth :
```bash
GOOGLE_CLIENT_ID=votre-google-client-id
GOOGLE_CLIENT_SECRET=votre-google-secret
GITHUB_CLIENT_ID=votre-github-client-id
GITHUB_CLIENT_SECRET=votre-github-secret
STRAVA_CLIENT_ID=votre-strava-client-id
STRAVA_CLIENT_SECRET=votre-strava-secret
```

3. Modifier `settings.py` pour lire ces variables :
```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Dans SOCIALACCOUNT_PROVIDERS
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID', ''),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET', ''),
            'key': ''
        },
        ...
    },
    ...
}
```

## Test de l'authentification

### Authentification locale
1. Aller sur `http://localhost:8000/accounts/signup/`
2. Créer un compte avec email et mot de passe
3. Se connecter sur `http://localhost:8000/accounts/login/`

### Authentification OAuth
1. Aller sur `http://localhost:8000/accounts/login/`
2. Cliquer sur "Continuer avec Google" (ou GitHub, Strava)
3. Autoriser l'application
4. Vous serez redirigé et connecté automatiquement

## URLs d'authentification

- Login : `/accounts/login/`
- Signup : `/accounts/signup/`
- Logout : `/accounts/logout/`
- Password reset : `/accounts/password/reset/`
- Google OAuth : `/accounts/google/login/`
- GitHub OAuth : `/accounts/github/login/`
- Strava OAuth : `/accounts/strava/login/`

## Sécurité

⚠️ **Important** :
- Ne jamais commiter le fichier `.env` dans Git
- Utiliser des secrets différents en développement et production
- En production, activer HTTPS et mettre à jour les URLs de callback
- Activer la vérification email : `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`

## Dépannage

### "Social application not found"
→ Vérifier que l'application sociale est bien configurée dans l'admin Django et associée au bon site

### "Redirect URI mismatch"
→ Vérifier que l'URI de callback dans les paramètres OAuth du provider correspond exactement à celle configurée

### "Invalid client"
→ Vérifier que le Client ID et Secret sont corrects

## Documentation

- [Django-allauth](https://docs.allauth.org/)
- [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)
- [GitHub OAuth](https://docs.github.com/en/developers/apps/building-oauth-apps)
- [Strava OAuth](https://developers.strava.com/docs/authentication/)
