def get_formatted_name(first_name, last_name, middle_name = ""):
    if middle_name:
        formatted_name =  f"{first_name} {middle_name} {last_name}"
    else:
        formatted_name = f"{first_name} {last_name}"
    return formatted_name.title()