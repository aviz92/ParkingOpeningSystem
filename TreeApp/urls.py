"""DjReact URL Configuration

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

from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

app_name = 'TreeApp'

urlpatterns = [
    path('', views.LeveledTreeView.as_view()),
    path('<int:pk>/', views.LeveledTreeViewSet.as_view()),

    path('WithoutParents/<int:pk>/', views.LeveledTreeViewSet2.as_view()),
    path('GetFullHierarchy/', views.LeveledTreeFullHierarchy.as_view()),
    path('GetHierarchyWithoutTestPlan/', views.LeveledTreeHierarchyWithoutTestPlan.as_view()),  # http://asil-sv-ezlife:8000/admin/TreeApp/leveledtree/tree_json/

    path('LeveledTree/', views.LeveledTreeViewRoot.as_view()),

    path('Categories/', views.CategoriesView.as_view()),
    path('Categories/<int:pk>/', views.CategoriesViewSet.as_view()),

    path('Parameters/', views.ParametersView.as_view()),
    path('Parameters/<int:pk>/', views.ParametersViewSet.as_view()),

    path('ParametersTree/', views.ParametersTreeView.as_view()),
    path('ParametersTree/<int:pk>/', views.ParametersTreeViewSet.as_view()),
]
