from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('home/',views.tasklist.as_view(),name='home'),
    path('detaillist/<int:pk>/',views.taskdetail.as_view(),name='detaillist'),
    path('updatelist/<int:pk>/',views.taskupdate.as_view(),name='updatelist'),
    path('cbvdelete/<int:pk>/',views.taskdelete.as_view(),name='cbvdelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)