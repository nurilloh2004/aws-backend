"""
Database models.
"""
import uuid
import os

from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'recipe', filename)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    character = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Userlar")

class Category(models.Model):
    """Category model for navbar site."""
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent category", limit_choices_to={'is_active': True, 'parent_category__isnull': True}, related_name='children', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="Category title")
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class Banner(models.Model):
    """For Banner space on web info."""
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

class About(models.Model):
    """For about page info."""
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Info")


class SubAbout(models.Model):
    """For about page info."""
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("SubAbout")
        verbose_name_plural = _("SubAbout")


class Services(models.Model):
    """Hosting services model."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    RAM = models.CharField(max_length=255)
    SSD = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    extra_storage = models.CharField(max_length=255)
    backup = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_year = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Servis")
        verbose_name_plural = _("Servislar")


class ItemsDomain(models.Model):
    """For dynamically data for langing page."""
    name = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Domen haqida")
        verbose_name_plural = _("Domenlar haqida")


class Domain(models.Model):
    """For domain selling model."""
    Product_Status = (
        ('.uz', '.uz'),
        ('.ru', '.ru'),
        ('.com', '.com'),
        ('.info', '.info'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=Product_Status, default='.uz', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_year = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class OrderDomain(models.Model):
    """For Ordering custom domains."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    
    class Meta:
        verbose_name = _("Domen buyurtma")
        verbose_name_plural = _("Domen buyurtmalari")


class OrderService(models.Model):
    """For ordering Service tyoes."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    id_client_license = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class AllDomains(models.Model):
    exist_DNS_name = models.CharField(max_length=255)
    exist_DNS_site_name = models.CharField(max_length=255)
    price_DNS = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id_client_license = models.CharField(max_length=200)
    PM = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pm_all_domains')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_all_domains')


class Exist_servers_character(models.Model):
    server = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    RAM = models.CharField(max_length=255)
    SSD = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    extra_storage = models.CharField(max_length=255)
    backup = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_year = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class AllService(models.Model):
    exist_server_name = models.CharField(max_length=255)
    is_ours = models.BooleanField(default=True)
    service_character = models.ForeignKey(Exist_servers_character, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)









































































# class Recipe(models.Model):
#     """Recipe object."""
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     time_minutes = models.IntegerField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     link = models.CharField(max_length=255, blank=True)
#     tags = models.ManyToManyField('Tag')
#     ingredients = models.ManyToManyField('Ingredient')
#     image = models.ImageField(null=True, upload_to=recipe_image_file_path)

#     def __str__(self):
#         return self.title


# class Tag(models.Model):
#     """Tag for filtering recipes."""
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.name


# class Ingredient(models.Model):
#     """Ingredient for recipes."""
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         pass
