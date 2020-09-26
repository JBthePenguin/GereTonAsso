from django.db import models


class Material(models.Model):
    reference = models.CharField(
        db_index=True, max_length=150, unique=True,
        verbose_name="Désignation / Référence")
    value = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Valeur en €")
    CATEGORY_CHOICES = [
        ("A", "Association"),
        ("N", "Numérique"),
        ("M", "Musique"),
        ("E", "Énergie"),
        ("C", "Consommation")
    ]
    category = models.CharField(
        db_index=True, max_length=1, choices=CATEGORY_CHOICES, default="A",
        verbose_name="Catégorie")
    ACQUISITION_CHOICES = [
        ("R", "Récupération"),
        ("P", "Prêt"),
        ("A", "Achat"),
        ("D", "Don")
    ]
    acquisition = models.CharField(
        db_index=True, max_length=1, choices=ACQUISITION_CHOICES, blank=True,
        default="", verbose_name="Acquisition")
    STATUT_CHOICES = [
        ("A", "Dispo"),
        ("P", "Prêté"),
        ("R", "Rendu"),
        ("D", "Donné"),
        ("V", "Vendu")
    ]
    statut = models.CharField(
        db_index=True, max_length=1, choices=STATUT_CHOICES, default="A",
        verbose_name="État")

    class Meta:
        ordering = ['reference']
        verbose_name = "Matériel"
        verbose_name_plural = "Matériels"
