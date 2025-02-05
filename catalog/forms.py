from django.core.exceptions import ValidationError
from django.forms import ModelForm
from catalog.models import Product


BAD_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-control"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену"}
        )
        self.fields["is_published"].widget.attrs.update(
            {"class": "form-check-input"}
        )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_parsed = name.split()
        bad_words_founded = []
        for word in name_parsed:
            if word.lower() in BAD_WORDS:
                bad_words_founded.append(word)

        if bad_words_founded:
            bad_words_list = ', '.join(set(bad_words_founded))
            raise ValidationError(f'Название продукта не должно содержать: {bad_words_list}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        bad_words_founded = []
        if description:
            description_parsed = description.split()
            for word in description_parsed:
                if word.lower() in BAD_WORDS:
                    bad_words_founded.append(word)

        if bad_words_founded:
            bad_words_list = ', '.join(set(bad_words_founded))
            raise ValidationError(f'Описание продукта не должно содержать: {bad_words_list}')
        return description if description else ''

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не должна быть отрицательной')
        return price
