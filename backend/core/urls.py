from django.urls import path, include
from .views import ProductViewSet, SellSomethingForm, SoldItems, ContactUS

urlpatterns = [
    path('products/', include([
        path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    ])),
    path('submit-form/', SellSomethingForm.as_view(), name='submit_form'),
    path('sold-items/', SoldItems.as_view(), name='sold_items'),
    path('contact-us/', ContactUS.as_view(), name='contact-us'),

]
