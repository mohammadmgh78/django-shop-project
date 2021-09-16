from django.shortcuts import render

from product.models import Category, Product


def add_product(request):
    if request.method == 'POST':
        product_category = Category.objects.filter(pk=request.POST['select_category']).first()
        print(request.POST['select_category'])
        print(product_category)
        product = Product(name=request.POST['name'], price=request.POST['price'],
                          description=request.POST['description'], category=product_category,
                          image=request.FILES['image'])
        product.save()
    categories = Category.objects.all()
    return render(request, 'product/add_product.html', {'categories': categories})
