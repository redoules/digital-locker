from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class ClothingItem(models.Model):
    """Modèle représentant un vêtement déposé au travail."""
    
    class Type(models.TextChoices):
        HAUT = 'haut', 'Haut'
        BAS = 'bas', 'Bas'
        VESTE = 'veste', 'Veste'
        CHAUSSURES = 'chaussures', 'Chaussures'
    
    class Status(models.TextChoices):
        AU_TRAVAIL = 'au_travail', 'Au travail'
        RECUPERE = 'recupere', 'Récupéré'
        PERDU = 'perdu', 'Perdu'
    
    # Champs du modèle
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='clothing_items',
        verbose_name='Utilisateur'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nom'
    )
    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        verbose_name='Type'
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Couleur'
    )
    photo = models.ImageField(
        upload_to='clothing_photos/%Y/%m/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        verbose_name='Photo'
    )
    deposit_date = models.DateField(
        default=timezone.now,
        verbose_name='Date de dépôt'
    )
    location = models.CharField(
        max_length=100,
        verbose_name='Lieu'
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AU_TRAVAIL,
        verbose_name='Statut'
    )
    notes = models.TextField(
        blank=True,
        verbose_name='Notes'
    )
    
    class Meta:
        verbose_name = 'Vêtement'
        verbose_name_plural = 'Vêtements'
        ordering = ['-deposit_date']
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) - {self.user.username}"


class UserProfile(models.Model):
    """Profil utilisateur étendu pour stocker les informations OAuth."""
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Utilisateur'
    )
    avatar = models.URLField(
        max_length=500,
        blank=True,
        verbose_name='Avatar'
    )
    provider = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Fournisseur OAuth',
        help_text='google, github, strava'
    )
    
    class Meta:
        verbose_name = 'Profil utilisateur'
        verbose_name_plural = 'Profils utilisateur'
    
    def __str__(self):
        return f"Profil de {self.user.username}"
