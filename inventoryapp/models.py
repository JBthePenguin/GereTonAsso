from io import BytesIO
from django.core.files import File
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from memberapp.models import Member
from inventoryapp.utils import render_to_pdf


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
        ("V", "Vendu"),
        ("H", "HS"),
        ("J", "Jeté")
    ]
    statut = models.CharField(
        db_index=True, max_length=1, choices=STATUT_CHOICES, default="A",
        verbose_name="État")

    class Meta:
        ordering = ['reference']
        verbose_name = "Matériel"
        verbose_name_plural = "Matériels"


class Recovery(models.Model):
    material = models.OneToOneField(
        Material, on_delete=models.PROTECT, verbose_name="Matériel",
        limit_choices_to={'acquisition': ""}, db_index=True)
    recuperator = models.ForeignKey(
        Member, on_delete=models.PROTECT, verbose_name="Récupérateur",
        limit_choices_to={'grade': 'C', 'active': True}, db_index=True)
    date = models.DateField(
        db_index=True, auto_now_add=True, verbose_name="Date")
    receipt = models.FileField(
        upload_to='receipts_pdf/recovery/', null=True, blank=True,
        verbose_name="Fiche")

    class Meta:
        ordering = ['material__reference']
        verbose_name = "Récupération"
        verbose_name_plural = "Récupérations"

    def save(self, *args, **kwargs):
        super(Recovery, self).save(*args, **kwargs)
        if not self.receipt:
            # generate and save pdf receipt
            context = {'recovery': self}
            receipt_pdf = render_to_pdf('receipts/recovery.html', context)
            filename = f"recovery_{self.id}.pdf"
            self.receipt.save(filename, File(BytesIO(receipt_pdf.content)))
            # update material acquisition mode
            recovered_material = self.material
            recovered_material.acquisition = "R"
            recovered_material.save()


@receiver(post_delete, sender=Recovery)
def delete_related_material(sender, instance, **kwargs):
    material = instance.material
    material.delete()
