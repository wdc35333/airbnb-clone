from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "한국어"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    PREFERENCE_BOOK = "book"
    PREFERENCE_MOVIE = "movie"
    PREFERENCE_NONE = "none"
    PREFERENCE_ALL = "all"

    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOK, "책"),
        (PREFERENCE_MOVIE, "영화"),
        (PREFERENCE_ALL, "둘 다"),
        (PREFERENCE_NONE, "없음"),
    )

    GENRE_ACTION = "action"
    GENRE_SF = "sf"
    GENRE_COMEDY = "comedy"
    GENRE_ROMANCE = "romance"
    GENRE_HORROR = "horror"
    GENRE_WAR = "war"
    GENRE_SPORTS = "sports"
    GENRE_FANTASY = "fantasy"
    GENRE_NONE = "none"

    GENRE_CHOICES = (
        (GENRE_ACTION, "액션"),
        (GENRE_SF, "SF"),
        (GENRE_COMEDY, "코미디"),
        (GENRE_ROMANCE, "로맨스"),
        (GENRE_HORROR, "공포"),
        (GENRE_WAR, "전쟁"),
        (GENRE_SPORTS, "스포츠"),
        (GENRE_FANTASY, "판타지"),
        (GENRE_NONE, "없음"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default="kr")
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, default="krw")
    superhost = models.BooleanField(default=False)
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=5, default="none"
    )
    favourite_book_genre = models.CharField(
        choices=GENRE_CHOICES, max_length=7, default="none"
    )
    favourite_movie_genre = models.CharField(
        choices=GENRE_CHOICES, max_length=7, default="none"
    )
