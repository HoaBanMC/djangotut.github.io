from django.urls import path

from . import views

urlpatterns = [

    path('article/<int:year>', views.year_archive, name='year_archive'),
    path('article/<int:year>/<int:month>', views.month_archive),
    path('article/<int:year>/<int:month>/<int:pk>', views.article_detail),
]
