from django.db import models


# Create your models here.
class Purchase(models.Model): #Should I save the contact information on this object?
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class Insured(models.Model):
    document_url = models.CharField(max_length=300)
    policy_number = models.CharField(max_length=100, null=True)
    zurich_policy_number = models.CharField(max_length=100, null=True)
    assist_trip_id = models.IntegerField()
    travel_assistance_voucher = models.CharField(max_length=100 , null=True)
    insurance_ticket = models.CharField(max_length=100, null=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self):
        return f"id:{self.assist_trip_id} purchase:{self.purchase_id}"

