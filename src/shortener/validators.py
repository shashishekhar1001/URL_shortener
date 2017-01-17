from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
        print(value)
    except:
        try:
            new_value = "http://" + value
            print(new_value)
            url_validator(new_value)
            print("Validation Successful")
        except:
            print("Validation Unsuccessful")
            raise ValidationError("Not a valid URL.")

def dot_com_validator(value):
    if not ".com" in value:
        print("Validation Unsuccessful")
        raise ValidationError("Not a .com URL")
