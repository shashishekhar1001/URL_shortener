from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
        print(value)
    except:
        raise ValidationError("Not a valid URL.")

def dot_com_validator(value):
    if not ".com" in value:
        raise ValidationError("Not a .com URL")
