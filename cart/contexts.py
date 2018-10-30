from django.shortcuts import get_object_or_404
from issue.models import Issue

def cart_contents(request):
    """Ensures that the cart contents are available when rendering every page"""
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    issue_count = 0
    quantity = 1
    price = 100
    for id, quantity in cart.items():
        issue = get_object_or_404(Issue, pk=id)
        total += quantity * price
        issue_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'issue': issue, 'price': price})
    
    return {'cart_items': cart_items, 'total': total, 'issue_count': issue_count}