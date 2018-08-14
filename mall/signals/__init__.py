import django.dispatch

app_ready = django.dispatch.Signal(providing_args=[])
