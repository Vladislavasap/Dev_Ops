from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from custom_user.models import User
from .models import Category, Genre, Title

admin.site.register(User)


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'role', 'bio', 'first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = [CategoryResource]
    list_display = ('name', 'slug')


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    resource_classes = [TitleResource]
    list_display = ('name', 'year', 'category',)


class UserAdmin(ImportExportModelAdmin):
    resource_classes = [UserResource]
    list_display = ('username', 'email',
                    'role', 'bio', 'first_name', 'last_name')
