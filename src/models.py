from django.db import models


class User(models.Model):
    pass


class CustomCake(models.Model):
    INGREDIENT_PRICES = {
        'уровень': {
            '1': 400,
            '2': 750,
            '3': 1100,
        },
        'форма': {
            'квадрат': 600,
            'круг': 400,
            'прямоугольник': 1000,
        },
        'топпинг': {
            'без топпинга': 0,
            'белый соус': 200,
            'карамельный сироп': 180,
            'кленовый сироп': 200,
            'клубничный сироп': 300,
            'черничный сироп': 350,
            'молочный шоколад': 200,
        },
        'ягоды': {
            'ежевика': 400,
            'малина': 300,
            'голубика': 450,
            'клубника': 500,
        },
        'декор': {
            'фисташки': 300,
            'безе': 400,
            'фундук': 350,
            'пекан': 300,
            'маршмеллоу': 200,
            'марципан': 280,
        },
        'надпись': 500
    }

    LEVEL_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    SHAPE_CHOICES = (
        ('квадрат', 'Квадрат (+600)'),
        ('круг', 'Круг (+400)'),
        ('прямоугольник', 'Прямоугольник (+1000)'),
    )

    TOPPING_CHOICES = (
        ('без топпинга', 'Без топпинга (+0)'),
        ('белый соус', 'Белый соус (+200)'),
        ('карамельный сироп', 'Карамельный сироп (+180)'),
        ('кленовый сироп', 'Кленовый сироп (+200)'),
        ('клубничный сироп', 'Клубничный сироп (+300)'),
        ('черничный сироп', 'Черничный сироп (+350)'),
        ('молочный шоколад', 'Молочный шоколад (+200)'),
    )

    BERRY_CHOICES = (
        ('ежевика', 'Ежевика (+400)'),
        ('малина', 'Малина (+300)'),
        ('голубика', 'Голубика (+450)'),
        ('клубника', 'Клубника (+500)'),
    )

    DECOR_CHOICES = (
        ('фисташки', 'Фисташки (+300)'),
        ('безе', 'Безе (+400)'),
        ('фундук', 'Фундук (+350)'),
        ('пекан', 'Пекан (+300)'),
        ('маршмеллоу', 'Маршмеллоу (+200)'),
        ('марципан', 'Марципан (+280)'),
    )

    levels = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    shape = models.CharField(max_length=100, choices=SHAPE_CHOICES)
    topping = models.CharField(max_length=100, choices=TOPPING_CHOICES)
    berries = models.CharField(max_length=100, choices=BERRY_CHOICES, blank=True)
    decor = models.CharField(max_length=100, choices=DECOR_CHOICES, blank=True)
    message = models.CharField(max_length=100, blank=True)

    def get_total_price(self):
        total_price = 0
        total_price += int(self.INGREDIENT_PRICES['уровень'][self.levels])
        total_price += self.INGREDIENT_PRICES['форма'][self.shape]
        total_price += self.INGREDIENT_PRICES['топпинг'][self.topping]
        if self.berries:
            total_price += self.INGREDIENT_PRICES['ягоды'][self.berries]
        if self.decor:
            total_price += self.INGREDIENT_PRICES['декор'][self.decor]
        if self.message:
            total_price += self.INGREDIENT_PRICES['надпись']
        return total_price

    class Meta:
        verbose_name = 'пользовательский торт'
        verbose_name_plural = 'пользовательские торты'


class CatalogCake(models.Model):
    name = models.CharField('название', max_length=50)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'торт'
        verbose_name_plural = 'торты'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cake = models.ForeignKey(CatalogCake, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    custom_cake = models.ForeignKey(CustomCake, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    address = models.CharField('адрес', max_length=100)
    date = models.DateField('дата')
    time = models.TimeField('время')
    comment = models.TextField('комментарий', blank=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
