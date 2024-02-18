from django.contrib import admin
from django.urls import path
from books.views import home,about,contact,book
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('book/', book.html),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

