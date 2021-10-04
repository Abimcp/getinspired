from django.urls import path
from . import views


from django.urls import include, path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from .views import QuoteList

urlpatterns = [
    path('', QuoteList.as_view()),
]

# urlpatterns = [
#     path('', views.show, name='generator-index')
# ]