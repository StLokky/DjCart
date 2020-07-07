from django.db import models

class ClassCart(models.Model):  # Лазерный, струйный, матричный
    name = models.CharField(max_length=10, unique=True, verbose_name='Класс картриджа (лазерный, струйный, матричный)')
    slug = models.SlugField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс картриджа'
        verbose_name_plural = 'Класс картриджей'


# *****************************************************************************************#
class TypeCart(models.Model):  # тонер-картридж, драм-унит, фузер и т.д...
    name = models.CharField(max_length=20, unique=True, verbose_name='Тип картриджа (тонер-картридж, драм-картридж, фузер и т.д..)')
    name_rus = models.CharField(max_length=20, verbose_name='Тип картриджа (тонер-картридж, драм-картридж, фузер и т.д..) на русском', blank=True)
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип картриджа'
        verbose_name_plural = 'Тип картриджей'

# *****************************************************************************************#
class Brand(models.Model):  # Производитель
    name = models.CharField(max_length=20, unique=True, verbose_name='Наименование производителя', db_index=True)
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

# *****************************************************************************************#
class Cartridge(models.Model): # Картридж
    name = models.CharField(max_length=20, unique=True, verbose_name='Наименование расходника', db_index=True)
    slug = models.SlugField(max_length=25, unique=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Бренд расходника')
    classcart = models.ForeignKey('ClassCart', on_delete=models.PROTECT, verbose_name='Класс расходника')
    typecart = models.ForeignKey('TypeCart', on_delete=models.PROTECT, verbose_name='Тип расходника')
    device = models.ManyToManyField('Device', verbose_name='В каких устройствах...')
    cartparam = models.ManyToManyField('CartParam', verbose_name='Параметры картриджа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

# *****************************************************************************************#
class TypeDevice(models.Model): # Тип аппарата - принтер, копир, мфу...
    name = models.CharField(max_length=20, unique=True, verbose_name='Тип аппарата (принтер, копир, мфу')
    slug = models.SlugField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Тип устройств'

# *****************************************************************************************#
class Device(models.Model): # Аппарат
    name = models.CharField(max_length=20, unique=True, verbose_name='Наименование устройства', db_index=True)
    slug = models.SlugField(max_length=25, unique=True)
    typedevice = models.ForeignKey('TypeDevice', on_delete=models.PROTECT, verbose_name='Тип устройства...')
    deviceparam = models.ManyToManyField('DeviceParam', verbose_name='Параметры устройства')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель устройства'
        verbose_name_plural = 'Модели устройства'

# *****************************************************************************************#
# Таблица с дополнительными полями для картриджей и аппаратов.
# Количество доп полей у разных устройств разное и неизвестное,
# варьируется от 0 до 10+
# Поэтому всю доп информацию сваливаем в кучу и пристыковываем отдельную запись к нужному объекту
class CartParam(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя параметра', db_index=True)
    param = models.CharField(max_length=20, verbose_name='Значение параметра', db_index=True)
    # cartridge = models.ForeignKey('Cartridge', on_delete=models.PROTECT, verbose_name='Картридж')

    class Meta:
        verbose_name = 'Параметр картриджа'
        verbose_name_plural = 'Параметры картриджа'

# *****************************************************************************************#
class DeviceParam(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя параметра', db_index=True)
    param = models.CharField(max_length=1000, verbose_name='Значение параметра', db_index=True)
    # device = models.ForeignKey('Device', on_delete=models.PROTECT, verbose_name='Картридж')

    class Meta:
        verbose_name = 'Параметр устройства'
        verbose_name_plural = 'Параметры устройства'