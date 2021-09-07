"""qalalab_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from blog import views

urlpatterns = [
    path("projects/", views.ProjectListView.as_view()),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view()),
    path("news/", views.NewsListView.as_view()),
    path("news/<int:pk>/", views.NewsDetailView.as_view()),
    path("events/", views.EventListView.as_view()),
    path("events/<int:pk>/", views.EventDetailView.as_view()),
    path("slider1/", views.Slider1View.as_view()),
    path("slider2/", views.Slider2View.as_view()),
    path("slider3/", views.Sldier3View.as_view()),
    path("slider1/<int:pk>/", views.Slider1ViewDetail.as_view()),
    path("slider2/<int:pk>/", views.Slider2ViewDetail.as_view()),
    path("slider3/<int:pk>/", views.Sldier3ViewDetail.as_view()),
]
