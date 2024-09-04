from django.urls import path
from .views import NewInvestment , MyInvests ,prediction , Login


urlpatterns = [
    path('new_invest/' , NewInvestment.as_view()),
    path('login/' , Login.as_view()),
    path('my_invest/' , MyInvests.as_view()),
    path('predict/' , prediction)
]