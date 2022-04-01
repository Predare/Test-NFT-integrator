from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('create/', views.TokenCreate.as_view()),
    path('list/', views.TokenList.as_view()),
    path('total_supply/', views.TotalSupply.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)