from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок")
    description = models.TextField(
        max_length=10000, blank=True, null=True, verbose_name="Содержимое", help_text="Введите текст"
    )
    image = models.ImageField(upload_to="blog/photo", blank=True, null=True, help_text="Загрузите превью")
    created_at = models.DateField(verbose_name="Дата создания")
    is_published = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.name
