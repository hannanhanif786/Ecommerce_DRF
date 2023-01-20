from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Maemes-Shouthall"
admin.site.site_title = "Maemes-shouthall_Admin"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls")),
    path("api/", include("user.urls")),
    path("order/", include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
