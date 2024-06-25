from PIL import Image
from customtkinter import CTkButton, CTkImage

def create_image(image_path):
    img = Image.open(image_path)
    if img.size > (600, 600):
        size = (img.size[0] // 2, img.size[1] // 2)
    else:
        size = img.size
    return CTkImage(light_image=img, size=size)

def get_imgs(path):
    #Pega uma lista de arquivos de um Diretorio
    files_list= [file for file in path.iterdir() if file.is_file()]
    #and ".png" == file.suffix() or ".jpg" == file.suffix()
    return [img for img in files_list]

class BtnImage(CTkButton):
    def __init__(self, master, image, command= None):
        super().__init__(master,
                         text= None,
                         image= image,
                         command= command,
                         fg_color= "#242424",
                         hover_color="#333333")