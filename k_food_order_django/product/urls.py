from django.urls import path, include
from django.urls.resolvers import URLPattern
from product import views

urlpatterns = [
        path('products/hottest-products/', views.HottestProductsList.as_view()),		
        path('products/all/', views.AllCategoryList.as_view()),
        path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
        path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),	

]