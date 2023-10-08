from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from src.config import settings
from src.apps.gallery import urls as gallery_urls
from src.apps.accounts import urls as accounts_urls
from src.apps.handbook import urls as handbook_urls
from src.apps.project import urls as project_urls
# from src.apps.favorites import urls as favorites_urls
# from src.apps.orders import urls as orders_urls
# from src.apps.storage import urls as storage_urls
# from src.apps.company import urls as company_urls
# from src.apps.wallet import urls as wallet_urls
from src.apps.accounts.views import confirm_email
from . import swagger



urlpatterns = [
    path('confirm/<str:token>/', confirm_email, name='confirm_email'),
    path('admin/', admin.site.urls),
    path('api/v1/gallery/', include(gallery_urls)),
    path('api/v1/account/', include(accounts_urls)),
    path('api/v1/handbook/', include(handbook_urls)),
    path('api/v1/projects/', include(project_urls)),
    # path('api/v1/favorites/', include(favorites_urls)),
]

urlpatterns += swagger.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
