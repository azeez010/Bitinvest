import uuid
# from datetime import timedelta
from biti.helpers import utils, enums
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from biti.helpers.mixins import BaseModelMixin
from django_countries.fields import CountryField
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now
from django.urls import reverse

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

    def get_by_alternate_key(self, phone_number):
        return self.get(**{self.model.ALTERNATE_KEY_FIELD: phone_number})

# Create your models here.

class User(AbstractUser):
    country = CountryField()
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    wallet = models.FloatField(_("Wallet funds"), default=0.0)
    
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

    class Meta:
        verbose_name = _("User")

    def __str__(self):
        return self.username + " - " + self.email
    
    def __repr__(self):
        return self.username + " - " + self.email

class KGS(BaseModelMixin):
    key = models.CharField(max_length=64, default=uuid.uuid4(), blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User KGS"), related_name='user_kgs')
    used = models.BooleanField(default=False)
    product_type = models.CharField(max_length=50, choices=enums.ProductType.choices(), null=False, blank=False)
    price = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"{self.user.email} key is {self.used}"
    
    def use(self, user, _type):
        self.used = True
        self.user = user
        self.product_type = _type
        self.save()

    def check_use(self, user):
        if self.used and self.user == user:
            return True
        return False

    
    class Meta:
        verbose_name_plural = "KGS"
        verbose_name = "KGS"
    

class InvestmentCountries(BaseModelMixin):
    returns = models.IntegerField(_("Return multiples"))
    country = CountryField()
    
    def __str__(self):
        return self.country.name + " returns " + str(self.returns)
    
    class Meta:
        verbose_name_plural = "investment Countries"
        verbose_name = "investment Country"
    
class Invest(BaseModelMixin):
    product = models.ImageField(upload_to="invest/", max_length=150)
    title = models.CharField(max_length=50)
    start_range = models.IntegerField(_("Start Due Date"))
    end_range = models.IntegerField(_("End Due Date"))
    price = models.FloatField(default=0.0)
    investment_location = models.ManyToManyField(InvestmentCountries, verbose_name=_("Investment Locations"))
    
    def __str__(self):
        return self.title + " for " + str(self.price)  
    
class Trade(BaseModelMixin):
    product = models.ImageField(upload_to="trade/", max_length=150)
    price = models.FloatField()
    title = models.CharField(max_length=50)
    returns = models.IntegerField(_("Return multiples"))
    start_range = models.IntegerField(_("Start Due Date"))
    end_range = models.IntegerField(_("End Due Date"))
    country = CountryField()

    def __str__(self):
        return self.title + " " + self.country.name

class Partner(BaseModelMixin):
    price = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True, related_name="user_partner")
    
    
class Settings(models.Model):
    key = models.CharField(max_length=20, blank=False, null=False)
    value = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=100, choices=enums.GlobalVariableType.choices(), default=enums.GlobalVariableType.STR.value, blank=False, null=False)

    def __str__(self) -> str:
        return self.key + " - " + self.value 
    
    
    class Meta:
        verbose_name_plural = "Settings"
        verbose_name = "Setting"
    
        
    