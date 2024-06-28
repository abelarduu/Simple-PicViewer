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
    # Pega uma lista de arquivos de um Diretorio
    files_list= [file for file in path.iterdir() if file.is_file()]
    # Filtra apenas os arquivos de imagem com extensões específicas
    return [img for img in files_list if img.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']]

class BtnImage(CTkButton):
    def __init__(self, master, image, text= None, command= None):
        super().__init__(master,
                         text= text,
                         image= image,
                         command= command,
                         compound= "top",
                         fg_color= "#242424",
                         hover_color="#333333")