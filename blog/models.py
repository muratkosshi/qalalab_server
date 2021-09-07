from django.db import models


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание")
    content = models.TextField("Контент")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата последнего изминения", auto_now=True)
    url = models.SlugField(max_length=160, unique=True, )

    class Meta:
        abstract = True


class Projects(Post):
    name = models.CharField('Название', max_length=150)
    target = models.CharField('Цель', max_length=500)
    image = models.ImageField("Изображение", upload_to="projects/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class News(Post):
    image = models.ImageField("Изображение", upload_to="news/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Event(Post):
    image = models.ImageField("Изображение", upload_to="events/")
    place = models.CharField("Место мероприятия", null=True, max_length=150)
    data = models.DateTimeField("Дата и время события")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class EventPhotos(models.Model):
    event = models.ForeignKey(Event, verbose_name="Мероприятие", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="event_photos/")

    class Meta:
        verbose_name = "Фото мероприятия"
        verbose_name_plural = "Фотографии мероприятий"


class NewsPhotos(models.Model):
    news = models.ForeignKey(News, verbose_name="Новости", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="news_photos/")

    def __str__(self):
        return "Фото новостей"

    class Meta:
        verbose_name = "Фото новости"
        verbose_name_plural = "Фотографии новостей"


class ProjectsPhotos(models.Model):
    project = models.ForeignKey(Projects, verbose_name="Проект", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="project_photos/")

    class Meta:
        verbose_name = "Фото проекта"
        verbose_name_plural = "Фотографии проектов"


class Slider1(models.Model):
    project = models.ForeignKey(Projects, null=True, verbose_name='Проект', on_delete=models.SET_NULL,
                                related_name='slider1')

    class Meta:
        verbose_name = "Первый слайдер"
        verbose_name_plural = "Первый слайдер"


class Slider2(models.Model):
    news = models.ForeignKey(News, null=True, verbose_name='Новость', on_delete=models.SET_NULL, related_name='slider2')

    class Meta:
        verbose_name = "Второй слайдер"
        verbose_name_plural = "Второй слайдер"


class Slider3(models.Model):
    event = models.ForeignKey(Event, null=True, verbose_name='Мероприятие', on_delete=models.SET_NULL,
                              related_name='slider3')

    class Meta:
        verbose_name = "Третий слайдер"
        verbose_name_plural = "Третий слайдер"


class MainNews(models.Model):
    news = models.ForeignKey(News, null=True, verbose_name='Главная новость', on_delete=models.SET_NULL, related_name='MainNews')

    class Meta:
        verbose_name = "Главная новость"
        verbose_name_plural = "Главная новость"
