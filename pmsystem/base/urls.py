# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),

    path('registerPage/', views.registerPage, name="registerpage"),
    path('loginPage/', views.loginPage, name="loginpage"),
    path('logoutPage/', views.logoutPage, name="logoutpage"),

    path('catalogue/<str:pk>/', views.catalogue, name="catalogue"),
    path('about/', views.about, name="about"),
    # path('faq/', views.faq, name="faq"),

    
    path('book_unit/<str:pk>/', views.book_unit, name="bookunit"),
    path('newunit/', views.newUnit, name="newunit"),

    path('house_status/', views.house_status, name="house_status"),
    path('cart/', views.mybooked_units, name="cart"),

]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)