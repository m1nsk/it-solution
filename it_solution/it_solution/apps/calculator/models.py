from django.db import models

# Create your models here.


class Transfer(models.Model):
    DEBT = 'DEBT'
    REPAYMENT = 'REPAYMENT'
    TRANSFER_TYPES = (
        (DEBT, 'debt'),
        (REPAYMENT, 'repayment'),
    )
    user_id = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=10,
                            blank=False,
                            choices=TRANSFER_TYPES,
                            default=DEBT)
    value = models.IntegerField()
