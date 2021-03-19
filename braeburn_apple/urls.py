from django.urls import path
from .views import BraeburnAppleListView, BraeburnAppleDetailView, BraeburnAppleCreateView, BraeburnAppleUpdateView, BraeburnAppleDeleteView

urlpatterns = [
    path('', BraeburnAppleListView.as_view(), name='braeburn_list'),
    path('create/', BraeburnAppleCreateView.as_view(), name='braeburn_create'),
    path('<int:pk>/delete/', BraeburnAppleDeleteView.as_view(), name='braeburn_delete'),
]