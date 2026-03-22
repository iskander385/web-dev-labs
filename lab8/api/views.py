from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


class CategoryDetailView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, pk=id)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)


class CategoryProductsView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, pk=id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
