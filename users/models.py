
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ These custom fields will be supplemented 
        with the Django framework default user sign up fields
        create a tuple so i can do zero, first, second or third, postgrad
        """

    uni_year = models.SmallIntegerField(null=True, blank=False)
    degree = models.CharField(max_length=40)
    