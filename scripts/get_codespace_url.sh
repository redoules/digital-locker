#!/bin/bash

echo "🔍 Détection de l'environnement..."
echo ""

if [ -n "$CODESPACE_NAME" ]; then
    echo "✅ Vous êtes dans un GitHub Codespace"
    echo ""
    
    # Construire l'URL du Codespace
    CODESPACE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    
    echo "📋 Configuration OAuth pour GitHub Codespace:"
    echo ""
    echo "🌐 URL de votre application:"
    echo "   $CODESPACE_URL"
    echo ""
    echo "🔗 URL de callback à configurer dans GitHub OAuth:"
    echo "   ${CODESPACE_URL}/accounts/github/login/callback/"
    echo ""
    echo "📝 Étapes à suivre:"
    echo ""
    echo "1. Allez sur: https://github.com/settings/developers"
    echo "2. Éditez votre application OAuth"
    echo "3. Mettez à jour:"
    echo "   - Homepage URL: $CODESPACE_URL"
    echo "   - Authorization callback URL: ${CODESPACE_URL}/accounts/github/login/callback/"
    echo "4. Sauvegardez"
    echo ""
    echo "🔄 Pour les autres providers (Google, Strava):"
    echo "   - Google: ${CODESPACE_URL}/accounts/google/login/callback/"
    echo "   - Strava: Utilisez le domaine: ${CODESPACE_NAME}-8000.app.github.dev"
    echo ""
    echo "⚠️  Note: L'URL du Codespace change à chaque redémarrage du Codespace!"
    echo ""
else
    echo "💻 Vous êtes en développement local"
    echo ""
    echo "🔗 URLs de callback à configurer:"
    echo "   - GitHub: http://localhost:8000/accounts/github/login/callback/"
    echo "   - Google: http://localhost:8000/accounts/google/login/callback/"
    echo "   - Strava: utilisez le domaine 'localhost'"
    echo ""
fi
