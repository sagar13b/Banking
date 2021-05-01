from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,name,email,phone,profilepic,address,password=None,**kwarg):
        if not email:
            raise ValueError('User must have email address')
        user = self.model(email=self.normalize_email(email),
                          name = name,
                          phone = phone,
                          profilepic = profilepic,
                          address = address,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_client(self,name,email,phone,profilepic,address,password=None,**kwarg):
        user = self.create_user(name,email,phone,profilepic,address,password=None,**kwarg)
        user.client = True
        user.save(using=self._db)
        return user

    def create_casier(self,name,email,phone,profilepic,address,password=None,**kwarg):
        user = self.create_user(name,email,phone,profilepic,address,password=None,**kwarg)
        user.casier = True
        user.save(using=self._db)
        return user

    def create_manager(self,name,email,phone,profilepic,address,password=None,**kwarg):
        user = self.create_user(name,email,phone,profilepic,address,password=None,**kwarg)
        user.manager = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='email_address',max_length=255,unique=True)
    phone = models.IntegerField()
    profilepic = models.ImageField(upload_to='profile/')
    address = models.CharField(max_length=250)
    client = models.BooleanField(default=False)
    casier = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    account_created = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone','profilepic','address']

    object = UserManager()
    @property
    def is_client(self):
        return self.client

    @property
    def is_manager(self):
        return self.manager

    @property
    def is_casier(self):
        return self.casier

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perm(self,app_label):
        return True

class ManagerDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #PROTECT, SET_NULL, DO_NOTHING
    branch = models.CharField(max_length=30)
    salary = models.IntegerField(null=True)
