from django.urls import path

from .views import *

urlpatterns = [
	#Leave as empty string for base url
	path('', index, name="index"),
	path('cart/', cart, name="cart"),
	path('signin/', signin, name="signin"),
	path('signup/', signup, name="signup"),
	path('checkout/', checkout, name="checkout"),
	path('fashion/', fashion, name="fashion"),
	path('productdetail/<int:id>/', productdetail, name="productdetail"),

	path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process_order"),

]