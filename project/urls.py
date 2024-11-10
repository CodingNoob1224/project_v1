from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # 導入 TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),  # 使用 TemplateView 直接渲染 index.html
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('member/', include('member.urls')),
    # 你可以為其他應用添加路由
]
