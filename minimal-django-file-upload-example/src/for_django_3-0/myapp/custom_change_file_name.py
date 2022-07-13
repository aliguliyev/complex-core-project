import uuid
def change_name(name):
    name_no_ext = name.rsplit('.', 1)[0]
    ext = name.rsplit('.', 1)[1]
    newname = name_no_ext + str(uuid.uuid4()) + "." + ext
    return newname