from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'


class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(default='')

    class Meta:
        db_table = 'products'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    prod = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"


class Size(models.Model):
    name = models.CharField(max_length=45)
    # blank = True >> 필드의 값이 ""값으로 저장됨
    # null = True >> 필드의 값이 정보없음(null)으로 저장됨
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = "sizes"


class Nutrition(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    size = models.ForeignKey("Size", on_delete=models.CASCADE)

    #  max_digits : 숫자에 허용되는 최대 자릿수, None이거나 decimal_places보다 크거나 같은 정수
    # decimal_places : 숫자와 함께 저장할 소수 자릿수
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_g = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'nutritions'


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergy"


class Allergy_Product(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_products"
