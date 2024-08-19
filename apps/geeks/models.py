from django.db.models import * 
from apps.geeks.iconky import ICON

# Create your models here.
class Index(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    description = TextField(
        verbose_name="Описание сайта ()"
    )
    logo = ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    banner = ImageField(
        upload_to='image/'
    )
    twitter = URLField(
        verbose_name='Укжите ссылку на twitter'
    )
    facebook = URLField(
        verbose_name='Укжите ссылку на facebook'
    )
    github = URLField(
        verbose_name='Укжите ссылку на github'
    )
    gmail = URLField(
        verbose_name='Укжите ссылку на почту'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'


class About_us(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок о нас (о нас)'
    )
    description = TextField(
        verbose_name="Описание о нас ()"
    )
    icon = CharField(
        choices=ICON,
        max_length=155,
        verbose_name='иконка'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки о нас'


class Other(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок другое (Другое)'
    )
    description = TextField(
        verbose_name="Описание другое ()"
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки другое'

class Zagolovok(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки заголовка'

class Team(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок участника (на странице команда)'
    )
    description = TextField(
        verbose_name="Описание участника ()"
    )
    foto = ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки участника'

class Сheck(Model):
    title = CharField(
        max_length=10,
        verbose_name='Число в счете (число)'
    )
    description = TextField(
        verbose_name="Описание счета ()"
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки счета'

class Slaid(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок (сдайд)'
    )
    description = TextField(
        verbose_name="Описание слайда ()"
    )
    foto1 = ImageField(
        upload_to='image/',
        verbose_name='Фото 1'
    )
    foto2 = ImageField(
        upload_to='image/',
        verbose_name='Фото 2'
    )


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки слайда'

class History(Model):
    foto = ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    title = CharField(
        max_length=255,
        verbose_name='Заголовок ()'
    )
    description = TextField(
        verbose_name="Описание ()"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки истории'

class Denga(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок ()'
    )
    description = CharField(
        max_length=255,
        verbose_name="Описание ()"
    )
    tip = CharField(
        max_length=255,
        verbose_name="Описание тип ()"
    )
    date = CharField(
        max_length=255,
        verbose_name="Описание дата ()"
    )
    slovo = CharField(
        max_length=255,
        verbose_name="Описание  слово()"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки denga'