from django.db import models


class Transaction(models.Model):
    wording = models.CharField(
        db_index=True, max_length=200, verbose_name="Libellé")
    date = models.DateField(db_index=True, verbose_name="Date")
    bank_entry = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Banque (entrée) en €",
        null=True, blank=True)
    bank_exit = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Banque (sortie) en €",
        null=True, blank=True)
    fund_entry = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Caisse (entrée) en €",
        null=True, blank=True)
    fund_exit = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Caisse (sortie) en €",
        null=True, blank=True)

    class Meta:
        ordering = ['date']
        verbose_name = "Opération"
        verbose_name_plural = "Opérations"


class MoneyDeposit(models.Model):
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Montant en €")
    date = models.DateField(
        db_index=True, auto_now_add=True, verbose_name="Date")

    class Meta:
        ordering = ['date']
        verbose_name = "Dépôt à la banque"
        verbose_name_plural = "Dépôts à la banque"

    def save(self, *args, **kwargs):
        super(MoneyDeposit, self).save(*args, **kwargs)
        Transaction.objects.create(
            wording="Dépôt à la banque", date=self.date,
            bank_entry=self.amount, fund_exit=(self.amount)
        )


class MoneyWithdrawal(models.Model):
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Montant en €")
    date = models.DateField(
        db_index=True, auto_now_add=True, verbose_name="Date")

    class Meta:
        ordering = ['date']
        verbose_name = "Retrait d'argent liquide"
        verbose_name_plural = "Retraits d'argent liquide"

    def save(self, *args, **kwargs):
        super(MoneyWithdrawal, self).save(*args, **kwargs)
        Transaction.objects.create(
            wording="Retrait d'argent liquide", date=self.date,
            bank_exit=self.amount, fund_entry=(self.amount)
        )
