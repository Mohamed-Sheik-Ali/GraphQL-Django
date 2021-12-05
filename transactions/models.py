from django.db import models


class workmodel(models.Model):
    description = models.CharField(max_length=15)
    workflow = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class Parties(models.Model):
    model_type = models.ForeignKey(workmodel,  on_delete=models.CASCADE , default = 1 )
    customer_id = models.CharField(max_length=18)
    account_number = models.CharField(max_length=18)
    name = models.CharField(max_length=35)
    base_currency  = models.CharField(max_length=3)
    address_line_1 = models.CharField(max_length=35)
    address_line_2 = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    zipcode = models.CharField(max_length=6)
    country_code = models.CharField(max_length=2)
    customer = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class ProgramType(models.Model):
    description = models.CharField(max_length=35)

    def __str__(self):
        return self.description

class Programs(models.Model):
    model = models.ForeignKey(workmodel,on_delete=models.CASCADE,default=2)
    party = models.ForeignKey(Parties,on_delete=models.CASCADE)
    program_model  = models.OneToOneField(ProgramType,on_delete=models.CASCADE)
    finance_request_type = models.BooleanField(default=False)
    currency = models.CharField(max_length=3)
    max_total_limit = models.DecimalField(max_digits=5, decimal_places=2)
    expiry = models.DateField()
    max_finance_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    max_age_for_repayment = models.IntegerField()
    minimum_period = models.IntegerField()
    maximum_period = models.IntegerField()
    minimum_amount_currency = models.CharField(max_length=3)
    minimum_amount = models.DecimalField(max_digits=5, decimal_places=2)
    financed_amount = models.DecimalField(max_digits=5, decimal_places=2)
    balance_amount = models.DecimalField(max_digits=5, decimal_places=2)
    grace_period = models.IntegerField()
    interest_type = models.BooleanField(default=False)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    margin = models.DecimalField(max_digits=5, decimal_places=2)
