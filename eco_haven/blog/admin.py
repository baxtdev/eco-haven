from django.contrib import admin
from .models import*


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
@admin.register(Adviсe)
class AdviceAdmin(admin.ModelAdmin):
    pass




# Register your models here.
