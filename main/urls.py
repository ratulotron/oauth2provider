from django.contrib import admin
from django.urls import path, include
from main.views import ApiEndpoint, UserList, UserDetails, GroupList, index

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('', index)
    path('', ApiEndpoint.as_view())
]
