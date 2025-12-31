# 🔐 Configuration des Credentials OAuth

Le fichier `.env` a été créé mais contient des valeurs par défaut. Vous devez obtenir vos propres credentials OAuth pour chaque provider.

## 📝 Étapes à suivre

### 1. Google OAuth

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/)
2. Créez un nouveau projet ou sélectionnez un projet existant
3. Activez l'API "Google+ API"
4. Allez dans "APIs & Services" → "Credentials"
5. Cliquez sur "Create Credentials" → "OAuth client ID"
6. Type d'application : **Application Web**
7. Ajoutez les URIs de redirection autorisées :
   ```
   http://localhost:8000/accounts/google/login/callback/
   ```
8. Copiez le **Client ID** et le **Client Secret**
9. Mettez à jour le fichier `.env` :
   ```
   GOOGLE_CLIENT_ID=votre-client-id-google.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=votre-secret-google
   ```

### 2. GitHub OAuth

1. Allez sur [GitHub Developer Settings](https://github.com/settings/developers)
2. Cliquez sur "New OAuth App"
3. Remplissez :
   - **Application name** : Work Clothes Tracker
   - **Homepage URL** : `http://localhost:8000`
   - **Authorization callback URL** : `http://localhost:8000/accounts/github/login/callback/`
4. Cliquez sur "Register application"
5. Copiez le **Client ID**
6. Cliquez sur "Generate a new client secret" et copiez-le
7. Mettez à jour le fichier `.env` :
   ```
   GITHUB_CLIENT_ID=Iv1.xxxxxxxxxxxx
   GITHUB_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxx
   ```

### 3. Strava OAuth

1. Allez sur [Strava API Settings](https://www.strava.com/settings/api)
2. Remplissez le formulaire :
   - **Application Name** : Work Clothes Tracker
   - **Category** : Other
   - **Club** : (laisser vide)
   - **Website** : `http://localhost:8000`
   - **Authorization Callback Domain** : `localhost`
3. Cliquez sur "Create"
4. Copiez le **Client ID** et le **Client Secret**
5. Mettez à jour le fichier `.env` :
   ```
   STRAVA_CLIENT_ID=123456
   STRAVA_CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

## ✅ Vérification

Après avoir mis à jour le fichier `.env` avec vos vraies credentials :

1. Redémarrez le serveur Django :
   ```bash
   uv run python manage.py runserver
   ```

2. Testez chaque provider :
   - Google : http://localhost:8000/accounts/google/login/
   - GitHub : http://localhost:8000/accounts/github/login/
   - Strava : http://localhost:8000/accounts/strava/login/

## ⚠️ Notes importantes

- **NE JAMAIS** commiter le fichier `.env` dans git (il est déjà dans `.gitignore`)
- Les credentials sont sensibles - ne les partagez jamais
- Pour la production, utilisez de vraies URLs (pas localhost)
- Le fichier `.env` doit rester dans le répertoire racine du projet

## 🔧 Dépannage

Si vous avez toujours l'erreur "client_id invalid" :
1. Vérifiez que le fichier `.env` est bien à la racine du projet
2. Vérifiez qu'il n'y a pas d'espaces avant/après les valeurs
3. Redémarrez complètement le serveur Django
4. Vérifiez les logs du terminal pour voir si `.env` a été chargé
