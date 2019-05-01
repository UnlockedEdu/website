from django.urls import path
from .admin import user_admin
from . import views

app_name = 'worksheets'
urlpatterns = [
    path('useradmin/', user_admin.urls),
    path('multiple_choice', views.multiple_choice_questions,
         name='multiple-choice'),
    path('free_response', views.free_response_questions, name='free-response'),
    path('raw_dump', views.raw_dump, name='raw_dump'),
]
