#!/bin/bash

echo "🔍 Vérification de la configuration OAuth..."
echo ""

# Vérifier si le fichier .env existe
if [ ! -f ".env" ]; then
    echo "❌ Le fichier .env n'existe pas !"
    echo "   → Copiez .env.example vers .env"
    exit 1
fi

echo "✅ Fichier .env trouvé"
echo ""

# Vérifier si python-dotenv est installé
if ! uv pip list | grep -q "python-dotenv"; then
    echo "❌ python-dotenv n'est pas installé !"
    echo "   → Exécutez: uv add python-dotenv"
    exit 1
fi

echo "✅ python-dotenv installé"
echo ""

# Charger les variables d'environnement
source .env 2>/dev/null || true

# Vérifier les credentials
echo "📋 État des credentials OAuth :"
echo ""

check_credential() {
    local name=$1
    local value=$2
    
    if [ -z "$value" ] || [ "$value" = "your-${name,,}-client-id" ] || [ "$value" = "your-${name,,}-client-secret" ]; then
        echo "❌ $name : Non configuré (valeur par défaut)"
        return 1
    else
        # Masquer partiellement la valeur
        local masked="${value:0:10}...${value: -4}"
        echo "✅ $name : Configuré ($masked)"
        return 0
    fi
}

all_ok=true

check_credential "GOOGLE_CLIENT_ID" "$GOOGLE_CLIENT_ID" || all_ok=false
check_credential "GOOGLE_CLIENT_SECRET" "$GOOGLE_CLIENT_SECRET" || all_ok=false
echo ""
check_credential "GITHUB_CLIENT_ID" "$GITHUB_CLIENT_ID" || all_ok=false
check_credential "GITHUB_CLIENT_SECRET" "$GITHUB_CLIENT_SECRET" || all_ok=false
echo ""
check_credential "STRAVA_CLIENT_ID" "$STRAVA_CLIENT_ID" || all_ok=false
check_credential "STRAVA_CLIENT_SECRET" "$STRAVA_CLIENT_SECRET" || all_ok=false
echo ""

if [ "$all_ok" = true ]; then
    echo "🎉 Tous les credentials OAuth sont configurés !"
    echo ""
    echo "Vous pouvez maintenant tester l'authentification :"
    echo "  1. Démarrez le serveur : uv run python manage.py runserver"
    echo "  2. Visitez : http://localhost:8000/accounts/login/"
else
    echo "⚠️  Certains credentials ne sont pas configurés."
    echo ""
    echo "Consultez OAUTH_CREDENTIALS_SETUP.md pour obtenir vos credentials."
    exit 1
fi
