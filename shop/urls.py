from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('signin/', views.signin, name="signin"),
	path('signup/', views.signup, name="signup"),
	path('checkout/', views.checkout, name="checkout"),
	path('fashion/', views.fashion, name="fashion"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]