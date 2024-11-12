from django.urls import path, re_path
import api.views


urlpatterns = [
    path('test/', api.views.generate_handwritten_image, name='test'),
]
app_name = 'api'