from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape
from .models import Product, Review
import telebot
import os
from django.db.models import Q

BOT_TOKEN = "7508512512:AAHOuu8klbbKR6AL-5Q4qgD_bBmHHLPZLNI"  # Замените на ваш токен
CHAT_ID = "6901083609"  # Замените на ваш chat_id

bot = telebot.TeleBot(BOT_TOKEN)

# Create your views here.

def home(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(Q(name__contains=search) | Q(description__contains=search))
    else:
        products = Product.objects.all()

    return render(request, 'index.html', {'products': products, 'search': escape(search) if search else ''})

def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        usage_duration = request.POST.get('duration')
        text = request.POST.get('review')

        review = Review(
            product=product,
            author=author,
            rating=rating,
            usage_duration=usage_duration,
            text=text,
        )
        review.save()

    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
    })

def payment(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')  # Получение номера телефона
        email = request.POST.get('email')  # Получение email

        # Отправка сообщения в Telegram
        bot.send_message(CHAT_ID, f'''📦 Новый заказ: {product.name}
💶 Цена: {product.price} рублей 💶

😄 ФИО покупателя: {name}
📮 Адрес доставки: {address}
📱 Телефон: {phone}
📧 Email: {email}
''')
        return redirect('/success')

    return render(request, "payment.html", {
        'product': product
    })

def success(request):
    return render(request, 'success.html')
