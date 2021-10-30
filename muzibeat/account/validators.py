from django.core.exceptions import ValidationError


def validate_file(value):
    value= str(value)
    if value.endswith(".jpg") != True and value.endswith(".jpeg") != True and value.endswith(".png") != True:
        raise ValidationError("Only PDF and Word Documents can be uploaded")
    else:
        return value
