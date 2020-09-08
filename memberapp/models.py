from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from jsignature.fields import JSignatureField


class Member(models.Model):
    first_name = models.CharField(
        db_index=True, max_length=150, verbose_name="Prénom")
    last_name = models.CharField(
        db_index=True, max_length=150, verbose_name="Nom")
    email = models.EmailField(
        db_index=True, max_length=150, unique=True, verbose_name="Email")
    phone = PhoneNumberField(blank=True, verbose_name="Téléphone")
    date_of_birth = models.DateField(verbose_name="Date de naissance")
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Date d'adhésion")
    active = models.BooleanField(default=True, verbose_name="Actif")
    GRADE_CHOICES = [
        ("A", "Adhérent"),
        ("H", "Honneur"),
        ("C", "Collège")
    ]
    grade = models.CharField(
        max_length=1, choices=GRADE_CHOICES,
        default="A", verbose_name="Statut"
    )
    signature = JSignatureField(verbose_name="Signature")

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Membre"
        verbose_name_plural = "Membres"

    def clean(self):
        """Capitalize the first charact if not."""
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
