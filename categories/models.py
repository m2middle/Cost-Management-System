from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    supplier = models.ManyToManyField(
        "suppliers.Supplier",
        related_name="categories",
    )

    def __repr__(self) -> str:
        return f"<[{self.pk}] - {self.name}>"
