from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, 'cart.html')
    
def add_to_cart(request, id):
    """"Add a quantity of the specified product to the cart"""
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    messages.success(request, 'Feature added to cart!')
    request.session['cart'] = cart
    return redirect(reverse('index'))
    