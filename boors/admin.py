from django.contrib.admin import ModelAdmin , register
from .models import Investment , Sandogh


@register(Sandogh)
class SandoghAdmin(ModelAdmin):
    list_display = [
        'name',
        'Gold',
        'Silver',
        'Copper',
        'Oil',
        'Steel',
    ]

@register(Investment)
class InvestmentAdmin(ModelAdmin):
    list_display = [
        'user',
        'invest',
        'sandogh',
        'start_month',
        'finish_month',
    ]