from django.conf import settings
from django.contrib import admin
from .views import redirect_index
from django.urls import path, include
from django.conf.urls.static import static
# from .views import Custom403, Custom404, custom500
#
# handler403 = Custom403.as_view()
# handler404 = Custom404.as_view()
# handler500 = custom500


urlpatterns = [
    path('', redirect_index),
    path('admin/', admin.site.urls),
    path('hasker/', include('forum.urls')),
    path('hasker/account/', include('account.urls')),
    path('hasker/api/', include('_api.urls')),
] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

