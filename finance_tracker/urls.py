from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('about', views.about),
    path('account', views.index_account),
    path('account/create', views.create_account),
    path('account/store', views.store_account),
    path('account/edit/<int:account_id>', views.edit_account),
    path("account/update/<int:account_id>", views.update_account),
    path('account/transaction/<int:account_id>/', views.create_transaction),
    path('account/save_transaction/<int:account_id>', views.save_transaction),
    path('account/delete/<int:account_id>', views.delete_account)
]
