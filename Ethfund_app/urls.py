from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('about',views.about,name="about"),
    # path('projcreate',views.projcreate,name="projcreate"),
    path('create',views.create,name="create"),
    path('fund',views.fund,name="fund"),
    path('check_user_exist',views.check_user_exists,name = "check_user_exist"),
    path('details/<str:id>/',views.details,name="details"),
    path('car',views.car,name="car"),
    path("profile",views.profile,name="profile"),
    path("meta",views.meta,name="meta"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
