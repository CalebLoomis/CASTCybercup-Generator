def check_number(dictionary, key):
    output = False
    try:
        int(dictionary[key])
        output = True
    except ValueError:
        print ("Bad value for {} in {} Are you sure that it's a number?", key, dict)

def check_number(dictionary, key):
    output = False
    try:
        int(dictionary[key])
        output = True
    except ValueError:
        print ("Bad value for {} in {} Are you sure that it's a number?", key, file)

def check_number(dictionary, key, file, item_description):
    output = False
    try:
        int(dictionary[key])
        output = True
    except ValueError:
        print ("Bad value for {} in {} for {}. Are you sure that it's a number?", key, file, item_description)

    return (output)
