from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Введите наименование")
    description = models.TextField(
        max_length=100, blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Введите наименование")
    description = models.TextField(
        max_length=100, blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    image = models.ImageField(upload_to="products/photo", blank=True, null=True, help_text="Загрузите фото")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категорию",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, verbose_name="Создатель", help_text="Укажите создателя публикации", blank=True, null=True, on_delete=models.SET_NULL)


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]
        permissions = [
            ("can_edit_name", "Can edit name"),
            ("can_edit_description", "Can edit description"),
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product")
        ]

    def __str__(self):
        return self.name
