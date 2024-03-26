from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username Must Be Set !")
        if not email:
            raise ValueError("Username Must Be Set !")
        if not password:
            raise ValueError("Username Must Be Set !")

        email = self.normalize_email(email)

        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser must be set is_staff=True ")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be set is_staff=True ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be set is_superuser=True ")

        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
