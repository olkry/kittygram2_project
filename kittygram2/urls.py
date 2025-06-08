from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('cats', CatViewSet)
router.register('users', UserViewSet)
router.register('achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


''' TESTuser1  !TESTpass1
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTMwMDkxMCwiaWF0IjoxNzQ5MjE0NTEwLCJqdGkiOiJmZTdjMTU3MDJlYWE0NmYzYWVjZGU5MDg4YjY4ZDUxNiIsInVzZXJfaWQiOjF9.xcDCjCg7QzECyTtTiTD2DanfpoWyhJiJSDWdp1VfrnM",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5MzAwOTEwLCJpYXQiOjE3NDkyMTQ1MTAsImp0aSI6IjIyODk2NzljMmVhMDRjMGNhYjA3MzkwMGY2OGU0ZGMyIiwidXNlcl9pZCI6MX0.NPNA_gbsCrZekAp6pIy-1h_hmuf0Ax_PJCjsHTklnPU"
}
'''

''' TESTuser2  !TESTpass2
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTMwMDk3NiwiaWF0IjoxNzQ5MjE0NTc2LCJqdGkiOiIyYjlkNzIwNGQyZGI0Nzg0OThkMjZkNjhiNWNkZDU5ZiIsInVzZXJfaWQiOjJ9.PIspT0bVu2LxRpvN-ReLrND7ClYMXqKr3NOQbG8k2DA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5MzAwOTc2LCJpYXQiOjE3NDkyMTQ1NzYsImp0aSI6IjAxYzRmMmJhNTE1ZTQyMzBhNzhlMmQ5MGVkNjU2ZDI4IiwidXNlcl9pZCI6Mn0.c6Wx5bTHxmYD3QPcpV--NcNOL8h_gn8zchZ_T1zyvao"
}
'''