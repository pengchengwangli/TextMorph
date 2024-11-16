from django.urls import path, re_path
import api.views

urlpatterns = [
    path('generate_handwritten_image/', api.views.generate_handwritten_image, name='generate_handwritten_image'),
    path('get_font_list/', api.views.get_font_list, name='get_font_list'),
]
app_name = 'api'
