# accounts
Django open source accounts app


## Get Started

Clone this repo at the root of your project. After that, change your `settings.py` file

```
# settings.py

INSTALLED_APPS = [
    ...
    'accounts',
]
```

And, at the bottom of `settings.py`, add the Login configuration

```
# settings.py
...
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
```

