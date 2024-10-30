from django.urls import path
from . import views

urlpatterns = [
    path("voucher/", views.purchaseData.as_view(), name="purchase"),
    path("status/<str:ref_code>", views.RetreiveVoucher.as_view(), name="retrieve_purchase"),
    path("update/<str:ref_code>", views.UpdateVoucher.as_view(), name="update_purchase"),
]