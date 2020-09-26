from django.db import models
from memberapp.models import Member
from inventoryapp.models import Material


class BaseLoan(models.Model):
    date_today = models.DateField(
        db_index=True, auto_now_add=True, verbose_name="Date du jour")
    date_of_begin = models.DateField(
        db_index=True, verbose_name="Date de début")
    date_of_end = models.DateField(
        db_index=True, null=True, blank=True, verbose_name="Date de fin")
    STATUT_CHOICES = [
        ("A", "En attente"),
        ("C", "En cours"),
        ("T", "Terminé")
    ]
    statut = models.CharField(
        db_index=True, max_length=1, choices=STATUT_CHOICES,
        default="A", verbose_name="Statut")
    loan_form = models.FileField(blank=True, verbose_name="Fiche de prêt")


class LoanMade(BaseLoan):
    lender = models.ForeignKey(
        Member, on_delete=models.PROTECT, verbose_name="Prêteur",
        limit_choices_to={'grade': 'C', 'active': True})


class LoanMadeToMember(LoanMade):
    borrower = models.ForeignKey(
        Member, on_delete=models.PROTECT, verbose_name="Emprunteur",
        limit_choices_to={'active': True})


class LoanMadeToMemberMaterial(LoanMadeToMember):
    material = models.ForeignKey(
        Material, on_delete=models.PROTECT, verbose_name="Matériel",
        limit_choices_to={'statut': "A"})
    notice_of_termination = models.IntegerField(
        default=1, verbose_name="Préavis de résiliation en jour")

    class Meta:
        ordering = ['date_today']
        verbose_name = "Prêt de matériel fait à un membre"
        verbose_name_plural = "Prêts de matériel faits aux membres"
