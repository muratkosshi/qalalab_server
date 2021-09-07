from django import forms
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from blog.models import News, Event, Projects, EventPhotos, NewsPhotos, ProjectsPhotos, Slider1, Slider2, Slider3

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# НОВОСТИ
class NewsPhotosInline(admin.StackedInline):
    model = NewsPhotos
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Фотографии из данной новости'


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Контент", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'created_at')
    readonly_fields = ("get_image",)
    inlines = [NewsPhotosInline]
    form = NewsAdminForm
    prepopulated_fields = {'url': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Изображение'


# МЕРОПРИЯТИЯ
class EventPhotosInline(admin.StackedInline):
    model = EventPhotos
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Фотографии мероприятия'


class EventAdminForm(forms.ModelForm):
    content = forms.CharField(label="Контент", widget=CKEditorUploadingWidget())

    class Meta:
        model = Event
        fields = '__all__'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'created_at',)
    readonly_fields = ("get_image",)
    inlines = [EventPhotosInline]
    form = EventAdminForm
    prepopulated_fields = {'url': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Изображение'


# ПРОЕКТЫ
class ProjectsPhotosInline(admin.StackedInline):
    model = ProjectsPhotos
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Фотографии с данного проекта'


class ProjectAdminForm(forms.ModelForm):
    content = forms.CharField(label="Контент", widget=CKEditorUploadingWidget())

    class Meta:
        model = Projects
        fields = '__all__'


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'created_at',)
    readonly_fields = ("get_image",)
    form = ProjectAdminForm
    prepopulated_fields = {'url': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} wight="100" height="100"/>')

    get_image.short_description = 'Изображение'


admin.site.register(Slider1)
admin.site.register(Slider2)
admin.site.register(Slider3)
admin.site.site_title = "Администрирование QalaLab"
admin.site.site_header = "Администрирование QalaLab"
