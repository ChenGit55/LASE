from django.urls import path
from .views import Home, LionCubs, Evolution, Lions

app_name = 'pages'

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('programs/lion-cubs/', LionCubs.as_view(), name='lion-cubs'),
    path('programs/evolution/', Evolution.as_view(), name='evolution'),
    path('programs/lions/', Lions.as_view(), name='lions'),
]