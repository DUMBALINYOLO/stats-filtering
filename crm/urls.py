"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from access.views import AppInit
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',AppInit.as_view(), name='crm'),
    url(r'^', include('access.urls')),
    url(r'^inventory/',include('inventory.urls')),
    url(r'^sales/',include('sales.urls')),
    url(r'^purchase/',include('purchase.urls')),
    url(r'^cash/',include('cash.urls')),
    url(r'^receipt/',include('receipt.urls')),
    url(r'^invoice/',include('invoice.urls')),
    url(r'^supplier/',include('supplier.urls')),
    url(r'^customer/',include('customer.urls')),
    url(r'^access/',include('access.urls')),
    url(r'^stats/',include('stats.urls')),
    url(r'^logger/',include('logger.urls')),
    url(r'^accounting/',include('accounting.urls')),

]