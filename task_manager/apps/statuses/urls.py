from django.urls import path
from task_manager.apps.statuses.views import StatusesList, \
     CreateStatus, DeleteStatus, UpdateStatus


urlpatterns = [
    path('', StatusesList.as_view(), name='statuses'),
    path('create/', CreateStatus.as_view(), name='create_st'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete_st'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='update_st'),
]
