from django.urls import path, include 
from .views import mainer_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('mainer/', mainer_view),
]