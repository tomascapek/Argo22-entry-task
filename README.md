# QR Validator
by Tomáš Čapek.

## Fair warning
This webapp was my first in Django, after quite a while and my very first one using Django REST.
It shows in some places and I haven't really have time left (due to crazy amount of time spent in docs :) ) to create a proper deployment.

## How to use (in dev mode)

This webapp have two dependencies - CRON and zbar binary.
Sadly I am not sure, what OS you are using, so you have to figure this out yourself :/

I use pipenv as my dependency manager. Launch procedure includes how to create venv with it.

After that:

```
cd this
pipenv sync # run only once
pipenv shell
cd website
python manage.py runserver
```

And you'll have debugging server up and running!

## Production mode

TBD