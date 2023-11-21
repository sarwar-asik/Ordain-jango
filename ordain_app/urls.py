from django.urls import path
from  .views import UserListCreateView,UserDetailView,ServiceListCreateView,ServiceDetailView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users/',UserListCreateView.as_view(),name="user-create"),
    path('users/<int:pk>/',UserDetailView.as_view(),name="user-profile")
    
]
