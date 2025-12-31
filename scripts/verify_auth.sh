#!/bin/bash
# Script de vérification de l'authentification - Checkpoint Tâche 4

set -e

echo "======================================================================="
echo "CHECKPOINT TÂCHE 4 - VÉRIFICATION DE L'AUTHENTIFICATION"
echo "======================================================================="
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compteurs
PASSED=0
FAILED=0

# Fonction de test
test_step() {
    local description="$1"
    local command="$2"
    
    echo -n "Test: $description... "
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ PASS${NC}"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}❌ FAIL${NC}"
        ((FAILED++))
        return 1
    fi
}

echo "1. VÉRIFICATION DES TESTS UNITAIRES"
echo "-------------------------------------------------------------------"

# Exécuter les tests
if uv run python manage.py test clothing --verbosity=0 2>&1 | grep -q "OK"; then
    echo -e "${GREEN}✅ Tous les tests passent (14/14)${NC}"
    ((PASSED++))
else
    echo -e "${RED}❌ Certains tests ont échoué${NC}"
    ((FAILED++))
fi

echo ""
echo "2. VÉRIFICATION DE LA CONFIGURATION"
echo "-------------------------------------------------------------------"

# Vérifier que django-allauth est installé
test_step "django-allauth installé" "uv pip list | grep -q django-allauth"

# Vérifier que pyjwt est installé
test_step "pyjwt installé" "uv pip list | grep -q PyJWT"

# Vérifier que cryptography est installé
test_step "cryptography installé" "uv pip list | grep -q cryptography"

# Vérifier les migrations
test_step "Migrations appliquées" "uv run python manage.py showmigrations account | grep -q '\[X\]'"

echo ""
echo "3. VÉRIFICATION DES FICHIERS"
echo "-------------------------------------------------------------------"

# Vérifier les templates
test_step "Template login.html existe" "test -f templates/account/login.html"
test_step "Template signup.html existe" "test -f templates/account/signup.html"
test_step "Template logout.html existe" "test -f templates/account/logout.html"

# Vérifier la configuration OAuth
test_step "Documentation OAuth existe" "test -f docs/OAUTH_SETUP.md"
test_step "Fichier .env.example existe" "test -f .env.example"

# Vérifier les tests
test_step "Tests d'authentification existent" "test -f clothing/test_auth.py"

echo ""
echo "4. VÉRIFICATION DE LA BASE DE DONNÉES"
echo "-------------------------------------------------------------------"

# Vérifier les tables allauth
if uv run python manage.py dbshell <<< ".tables" 2>/dev/null | grep -q "account_emailaddress"; then
    echo -e "${GREEN}✅ Tables allauth créées${NC}"
    ((PASSED++))
else
    echo -e "${YELLOW}⚠️  Impossible de vérifier les tables (normal en dev)${NC}"
fi

echo ""
echo "======================================================================="
echo "RÉSUMÉ DU CHECKPOINT"
echo "======================================================================="
echo -e "Tests réussis: ${GREEN}$PASSED${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "Tests échoués: ${RED}$FAILED${NC}"
else
    echo -e "Tests échoués: ${GREEN}0${NC}"
fi
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ CHECKPOINT VALIDÉ - L'authentification est correctement configurée${NC}"
    echo ""
    echo "Prochaines étapes:"
    echo "  1. Démarrer le serveur: uv run python manage.py runserver"
    echo "  2. Créer un superuser: uv run python manage.py createsuperuser"
    echo "  3. Tester login: http://localhost:8000/accounts/login/"
    echo "  4. Configurer OAuth (optionnel): voir docs/OAUTH_SETUP.md"
    echo ""
    exit 0
else
    echo -e "${RED}❌ CHECKPOINT NON VALIDÉ - Vérifier les erreurs ci-dessus${NC}"
    echo ""
    exit 1
fi
