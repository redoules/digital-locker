from django.test import TestCase
from django.contrib.auth.models import User
from hypothesis import given, strategies as st
from hypothesis.extra.django import TestCase as HypothesisTestCase, from_model
from datetime import date, timedelta
from .models import ClothingItem, UserProfile


class ClothingItemModelTest(TestCase):
    """Tests unitaires pour le modèle ClothingItem."""
    
    def setUp(self):
        """Créer un utilisateur de test."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_clothing_item(self):
        """Test de création d'un vêtement basique."""
        item = ClothingItem.objects.create(
            user=self.user,
            name='Pull bleu',
            type=ClothingItem.Type.HAUT,
            color='Bleu',
            location='Bureau'
        )
        self.assertEqual(item.name, 'Pull bleu')
        self.assertEqual(item.user, self.user)
        self.assertEqual(item.status, ClothingItem.Status.AU_TRAVAIL)
        self.assertIsNotNone(item.deposit_date)
    
    def test_clothing_item_str(self):
        """Test de la représentation string d'un vêtement."""
        item = ClothingItem.objects.create(
            user=self.user,
            name='Baskets',
            type=ClothingItem.Type.CHAUSSURES,
            color='Blanc',
            location='Vestiaire'
        )
        expected = f"Baskets (Chaussures) - {self.user.username}"
        self.assertEqual(str(item), expected)
    
    def test_default_status(self):
        """Test que le statut par défaut est 'au_travail'."""
        item = ClothingItem.objects.create(
            user=self.user,
            name='Veste',
            type=ClothingItem.Type.VESTE,
            color='Noir',
            location='Placard'
        )
        self.assertEqual(item.status, ClothingItem.Status.AU_TRAVAIL)


class ClothingItemPropertyTest(HypothesisTestCase):
    """Tests property-based pour le modèle ClothingItem."""
    
    def setUp(self):
        """Créer un utilisateur de test."""
        self.user = User.objects.create_user(
            username='propuser',
            email='prop@example.com',
            password='proppass123'
        )
    
    @given(
        name=st.text(min_size=1, max_size=100).filter(lambda x: x.strip()),
        type_choice=st.sampled_from([t[0] for t in ClothingItem.Type.choices]),
        color=st.text(min_size=1, max_size=50).filter(lambda x: x.strip()),
        location=st.text(min_size=1, max_size=100).filter(lambda x: x.strip()),
        notes=st.text(max_size=500),
        days_ago=st.integers(min_value=0, max_value=365)
    )
    def test_property_11_persistence_round_trip(self, name, type_choice, color, location, notes, days_ago):
        """
        Property 11: Persistance des modifications (round-trip)
        
        For any ClothingItem belonging to an authenticated user, after creation or modification,
        querying the database SHALL return an item with identical attributes to those that were saved.
        
        Validates: Requirements 4.3, 6.1, 6.2, 6.3
        """
        deposit_date = date.today() - timedelta(days=days_ago)
        
        # Créer un vêtement
        item = ClothingItem.objects.create(
            user=self.user,
            name=name,
            type=type_choice,
            color=color,
            location=location,
            notes=notes,
            deposit_date=deposit_date
        )
        item_id = item.id
        
        # Récupérer depuis la base de données
        retrieved_item = ClothingItem.objects.get(id=item_id)
        
        # Vérifier que toutes les propriétés sont identiques
        self.assertEqual(retrieved_item.user, self.user)
        self.assertEqual(retrieved_item.name, name)
        self.assertEqual(retrieved_item.type, type_choice)
        self.assertEqual(retrieved_item.color, color)
        self.assertEqual(retrieved_item.location, location)
        self.assertEqual(retrieved_item.notes, notes)
        self.assertEqual(retrieved_item.deposit_date, deposit_date)
        self.assertEqual(retrieved_item.status, ClothingItem.Status.AU_TRAVAIL)
        
        # Test de modification
        new_status = ClothingItem.Status.RECUPERE
        retrieved_item.status = new_status
        retrieved_item.save()
        
        # Récupérer à nouveau
        modified_item = ClothingItem.objects.get(id=item_id)
        self.assertEqual(modified_item.status, new_status)
        
        # Vérifier que les autres champs n'ont pas changé
        self.assertEqual(modified_item.name, name)
        self.assertEqual(modified_item.type, type_choice)
        self.assertEqual(modified_item.color, color)
        self.assertEqual(modified_item.location, location)


class UserProfileModelTest(TestCase):
    """Tests unitaires pour le modèle UserProfile."""
    
    def setUp(self):
        """Créer un utilisateur de test."""
        self.user = User.objects.create_user(
            username='profileuser',
            email='profile@example.com',
            password='profilepass123'
        )
    
    def test_create_user_profile(self):
        """Test de création d'un profil utilisateur."""
        profile = UserProfile.objects.create(
            user=self.user,
            avatar='https://example.com/avatar.jpg',
            provider='google'
        )
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.avatar, 'https://example.com/avatar.jpg')
        self.assertEqual(profile.provider, 'google')
    
    def test_user_profile_str(self):
        """Test de la représentation string d'un profil."""
        profile = UserProfile.objects.create(
            user=self.user,
            provider='github'
        )
        expected = f"Profil de {self.user.username}"
        self.assertEqual(str(profile), expected)
    
    def test_user_profile_optional_fields(self):
        """Test que les champs optionnels peuvent être vides."""
        profile = UserProfile.objects.create(user=self.user)
        self.assertEqual(profile.avatar, '')
        self.assertEqual(profile.provider, '')
