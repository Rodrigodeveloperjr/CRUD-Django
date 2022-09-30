def required_keys(data):

    error = {}

    keys = [
        "name",
        "email",
        "password",
        "isAdm"
    ]

    for key in keys:

        if key not in data.keys():
            error[key] = "Missing key"
    
    if error:
        raise KeyError
