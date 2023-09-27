from django.urls import path
from main.views import show_main, create_item, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user, increase_amount, decrease_amount, remove_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('increase_amount/<int:id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:id>/', decrease_amount, name='decrease_amount'),
    path('remove_item/<int:id>/', remove_item, name='remove_item'),
    path('create-item', create_item, name='create_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]