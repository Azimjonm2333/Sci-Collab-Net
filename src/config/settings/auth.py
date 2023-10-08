from datetime import timedelta

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Access token validity period
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Refresh token sliding expiration
    'SLIDING_TOKEN_REFRESH_LIFETIME_DELTA': timedelta(days=14),  # Maximum refresh token validity period
}
