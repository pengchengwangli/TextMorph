from django.urls import path, re_path
import api.views

urlpatterns = [
    path('generate_handwritten_image/', api.views.generate_handwritten_image, name='generate_handwritten_image'),
    path('get_font_list/', api.views.get_font_list, name='get_font_list'),
    path('get_download_history/', api.views.get_download_history, name='get_download_history'),
    path('download_history', api.views.download_history, name='download_history'),
]
app_name = 'api'
