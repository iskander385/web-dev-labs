import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

Product.objects.all().delete()
Category.objects.all().delete()

smartphones = Category.objects.create(name='Smartphones')
laptops = Category.objects.create(name='Laptops')
headphones = Category.objects.create(name='Headphones')
tablets = Category.objects.create(name='Tablets')

Product.objects.create(name='Apple iPhone 15 Pro', price=699990, description='Flagship smartphone with A17 Pro chip and titanium design.', count=15, is_active=True, category=smartphones)
Product.objects.create(name='Samsung Galaxy S24 Ultra', price=649990, description='Premium Android phone with built-in S Pen and AI features.', count=20, is_active=True, category=smartphones)
Product.objects.create(name='Xiaomi 14 Pro', price=399990, description='High-end Xiaomi flagship with Leica cameras.', count=10, is_active=True, category=smartphones)
Product.objects.create(name='Google Pixel 8 Pro', price=449990, description='Google flagship with best-in-class AI photography.', count=8, is_active=True, category=smartphones)
Product.objects.create(name='OnePlus 12', price=349990, description='Fast and smooth flagship killer with 100W charging.', count=12, is_active=True, category=smartphones)

Product.objects.create(name='Apple MacBook Air M3', price=899990, description='Ultra-thin laptop powered by Apple M3 chip with 18-hour battery.', count=7, is_active=True, category=laptops)
Product.objects.create(name='ASUS ROG Zephyrus G14', price=749990, description='Compact gaming laptop with Ryzen 9 and RTX 4060.', count=5, is_active=True, category=laptops)
Product.objects.create(name='Lenovo ThinkPad X1 Carbon', price=799990, description='Business ultrabook with legendary durability and keyboard.', count=6, is_active=True, category=laptops)
Product.objects.create(name='Dell XPS 15', price=849990, description='Premium 15-inch laptop with OLED display and Intel Core i9.', count=4, is_active=True, category=laptops)
Product.objects.create(name='HP Spectre x360', price=699990, description='Convertible 2-in-1 laptop with OLED touch display.', count=9, is_active=True, category=laptops)

Product.objects.create(name='Apple AirPods Pro 2', price=149990, description='Best-in-class ANC earbuds with spatial audio and H2 chip.', count=30, is_active=True, category=headphones)
Product.objects.create(name='Sony WH-1000XM5', price=179990, description='Industry-leading noise cancelling over-ear headphones.', count=18, is_active=True, category=headphones)
Product.objects.create(name='Bose QuietComfort 45', price=159990, description='Comfortable wireless headphones with excellent ANC.', count=14, is_active=True, category=headphones)
Product.objects.create(name='Samsung Galaxy Buds2 Pro', price=99990, description='Premium earbuds with Hi-Fi sound and intelligent ANC.', count=25, is_active=True, category=headphones)
Product.objects.create(name='Jabra Evolve2 85', price=189990, description='Professional wireless headset designed for focus work.', count=10, is_active=True, category=headphones)

Product.objects.create(name='Apple iPad Pro 12.9 M2', price=649990, description='Professional tablet with M2 chip, Liquid Retina XDR display.', count=8, is_active=True, category=tablets)
Product.objects.create(name='Samsung Galaxy Tab S9 Ultra', price=599990, description='Large-screen Android tablet with S Pen and AMOLED display.', count=6, is_active=True, category=tablets)
Product.objects.create(name='Xiaomi Pad 6 Pro', price=249990, description='High-performance tablet with Snapdragon 8+ Gen 1.', count=11, is_active=True, category=tablets)
Product.objects.create(name='Lenovo Tab P12 Pro', price=349990, description='Premium Android tablet with AMOLED display and quad speakers.', count=7, is_active=True, category=tablets)
Product.objects.create(name='Huawei MatePad Pro 13.2', price=449990, description='Elegant tablet with HarmonyOS and OLED nano-texture display.', count=5, is_active=True, category=tablets)

print(f"Seeded {Category.objects.count()} categories and {Product.objects.count()} products.")
