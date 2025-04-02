from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Order
from book.models import Book
from django.utils import timezone


@user_passes_test(lambda u: u.is_staff)
def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/all_orders.html', {'orders': orders})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/my_orders.html', {'orders': orders})


@login_required
def create_order(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        plated_end_at = request.POST.get('plated_end_at') 

        book = get_object_or_404(Book, pk=book_id)

        if book.count <= 0:
            return render(request, 'order/create_order.html', {'error': 'Book is not available', 'books': Book.objects.all()})

        order = Order.create(user=request.user, book=book, plated_end_at=plated_end_at)

        if order:
            return redirect('my_orders')
        else:
            return render(request, 'order/create_order.html', {'error': 'Cannot create order', 'books': Book.objects.all()})
    else:
        books = Book.objects.all()
        return render(request, 'order/create_order.html', {'books': books})


@user_passes_test(lambda u: u.is_staff)
def close_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.update(end_at=timezone.now())
    return redirect('all_orders')
