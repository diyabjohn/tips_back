from django.db import models

class Tip(models.Model):
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tip_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    total_tip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tip Calculation - {self.created_at}"

