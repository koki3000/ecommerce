from django.urls import path
from ..views import category

urlpatterns = [
    path('category/create/', category.CreateCategoryView.as_view(), name="create-category"),
    path('category/<int:pk>/delete/', category.DeleteCategoryView.as_view(), name="delete-category"),
    path('category/<int:pk>/update/', category.UpdateCategoryView.as_view(), name="update-category"),
    path('category/<int:pk>/', category.CategoryView.as_view(), name="details-category"),
    path('category/', category.CategoryPageView.as_view(), name="category"),
]