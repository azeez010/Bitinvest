from biti import models
from django.core.cache import cache
from biti.helpers.constants import GlobalVariableDefaultValues

def globals(request):
    context = {}
    get_settings = cache.get("settings")
    if get_settings:
        context["settings"] = cache.get("settings")
        return context
    else:    
        _settings = models.Settings.objects.all() 
        save = {}
        
        for setting in _settings:
            save[setting.key] = setting.value
        
        for key, value in GlobalVariableDefaultValues.items():
            if not save.get(key):
                save[key] = value
        context["settings"] = save
        cache.set("settings", save, 3600)
        return context