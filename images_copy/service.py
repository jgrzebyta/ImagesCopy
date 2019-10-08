

def is_picture(file_path):
    "Detectrs if given file is a picture."
    file_ext = file_path.extension()
    if (file_ext in ['jpg', 'jpeg', 'gif', 'png', 'mp4']):
        return True
    else:
        return False
