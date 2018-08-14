
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from profiles.views import RegisterView

# from menus.views    import HomeView
# from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view
# from restaurants.views import (
# 	restaurant_createview,
#     restaurant_listview,
# 	RestaurantListView,
# 	RestaurantDetailView,
# 	# restaurant_createview
#     RestaurantCreateView

# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),  
    url(r'^books/', include('books.urls', namespace='books')), 
    url(r'^category/', include('category.urls', namespace='category')),
    url(r'^period/', include('period.urls', namespace='period')),
    url(r'^budget/', include('budget.urls', namespace='budget')),
    url(r'^expense/', include('expense.urls', namespace='expense')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^logoutmessage/$', TemplateView.as_view(template_name='logoutform.html'), name='logoutmessage'),
]
