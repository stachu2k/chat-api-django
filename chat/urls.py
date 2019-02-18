from django.urls import path
from chat import views

urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('rooms/<int:pk>/messages/', views.RoomMessages.as_view(), name='room-messages'),
    path('messages/', views.MessageList.as_view(), name='message-list'),
]
