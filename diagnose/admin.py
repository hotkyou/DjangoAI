from django.contrib import admin
from django.apps import apps

app_models = apps.get_app_config('diagnose').get_models()

# 各モデルをadminサイトに追加
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
