from django.core.exceptions import ValidationError


def required_data(data):

    error = {}
    
    obj = {
        "name": str,
        "email": str,
        "password": str,
        "isAdm": bool
    }

    for key, value in obj.items():

        if type(data[key]) is not value:

            message_error = f"{key}: {value.__name__}"
            error[key] = message_error
    
    if error:
        raise ValidationError(None)
