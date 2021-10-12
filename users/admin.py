from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "preference",
                    "favourite_book_genre",
                    "favourite_movie_genre",
                )
            },
        ),
    )

    list_filter = (
        "language",
        "preference",
        "favourite_book_genre",
        "favourite_movie_genre",
    )
