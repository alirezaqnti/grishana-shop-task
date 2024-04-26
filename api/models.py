from django.db import models
from myshop.models import Product as BaseProduct
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    Name = models.CharField(_("Name"), max_length=200)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    Image = models.ImageField(_("Image"), upload_to="Category/", max_length=150)
    Active = models.BooleanField(_("فعالیت"), default=True)

    class Meta:
        verbose_name_plural = _("Categories")
        verbose_name = _("Category")

    def __str__(self):
        return self.Name

    def to_json(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "parent_id": str(self.parent_id),
            "level": self.level,
        }


class ProductTable(BaseProduct):
    Category = models.ForeignKey(
        Category, verbose_name=_("Category"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "ProductTable"
        verbose_name_plural = "ProductTables"

    def __str__(self):
        return self.product_name
