from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="دسته بندی")
    slug = models.SlugField(default='', null=False, db_index=True, verbose_name="لینک")
    picture = models.ImageField(upload_to="images/products/", null=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی محصول"
        verbose_name_plural = "دسته بندی"


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=100, verbose_name="شماره تماس")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    password = models.CharField(max_length=100, verbose_name="رمز عبور")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "مشتریان"
        verbose_name_plural = "مشتریان"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام محصول")
    description = models.CharField(max_length=100, default='', blank=True, null=True)
    long_description = models.TextField(default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="قیمت")
    rate = models.IntegerField(default=0, validators=(MaxValueValidator(10), MinValueValidator(0)))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False,
                                 related_name='pro_category', verbose_name="دسته بندی محصول")
    picture = models.ImageField(upload_to="images/products/")
    is_sale = models.BooleanField(default=False, verbose_name="تخفیف ویژه")
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12, verbose_name="قیمت تخفیف خورده")
    is_available = models.BooleanField(default=True, verbose_name="موجود")
    slug = models.SlugField(default='', null=False, db_index=True, verbose_name="لینک")

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=100, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} {self.quantity}"

    class Meta:
        verbose_name = "سفارشات"
        verbose_name_plural = "سفارشات"

# Create your models here.
