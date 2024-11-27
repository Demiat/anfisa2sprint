from django.contrib import admin
from .models import Category, IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано'


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):

    @staticmethod
    @admin.display(description='Топинги')
    def show_toppings(obj):
        return ', '.join(topping.title for topping in obj.toppings.all())

    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'show_toppings'
    )
    # readonly_fields = ('toppings',)
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category', 'wrapper')
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
# admin.site.register(IceCream, IceCreamAdmin)
