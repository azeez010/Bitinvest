from biti import models
from biti.helpers import enums, constants

def image_upload(file_to_upload):
    pass

def parse_bool(boolean: str) -> bool:   
    """_summary_

    Args:
        boolean (str): _description_

    Returns:
        bool: _description_
    """
    if not isinstance(boolean, bool):
        if isinstance(boolean, str):
            if boolean.lower() == "true":
                return True
        return False
    return boolean


def get_complete_url(request, suffix) -> str:
    scheme = request.is_secure() and "https" or "http"
    return f"{scheme}://{request.get_host()}{suffix}"

def get_global_variables(key: str):
    """
    Use of redis for caching values
    """
    try:
        instance = models.Settings.objects.get(key=key)
        value, value_type = instance.value, instance.value_type
        if value_type == enums.GlobalVariableType.INT.value:
            return int(value)
        elif value_type == enums.GlobalVariableType.FLOAT.value:
            return float(value)
        elif value_type == enums.GlobalVariableType.BOOL.value:
            return parse_bool(value)
        return value
    except models.Settings.DoesNotExist:
        return constants.GlobalVariableDefaultValues.get(key) if constants.GlobalVariableDefaultValues.get(key) else None
