from django.contrib.auth.models import BaseUserManager

class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        """ Create a new user user"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password):
        """ Create a new superuser profile """
        user = self.create_user(email, first_name, last_name, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user