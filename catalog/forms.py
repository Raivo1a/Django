from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


SPAM_WORDS = ['казино', 'биржа', 'обман', 'криптовалюта',
              'дешево', 'полиция', 'крипта', 'бесплатно', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        name_lower = name.lower()
        for word in SPAM_WORDS:
            if word in name_lower:
                raise ValidationError('Запрещенные слова, которые нельзя использовать в названиях')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        description_lower = description.lower()
        for word in SPAM_WORDS:
            if word in description_lower:
                raise ValidationError('Запрещенные слова, которые нельзя использовать в описании')
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Файл не должен превышать 5 МБ.')

            main, sub = image.content_type.split('/')
            if main != 'image' or sub not in ['jpeg', 'png']:
                raise ValidationError('Допустимы только форматы изображения JPEG или PNG.')
        return image
