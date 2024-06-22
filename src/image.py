from PIL import Image
from customtkinter import CTkButton, CTkImage

def create_image(image_path):
    img = Image.open(image_path)
    return CTkImage(light_image=img, size=img.size)
    
def get_imgs(path):
    #Pega uma lista de arquivos de um Diretorio
    #retorna uma lista destes arquivos Convertidos em CTkImage()
    files_list= [file for file in path.iterdir() if file.is_file()]
    #and ".png" == file.suffix() or ".jpg" == file.suffix()
    return [create_image(img) for img in files_list]

class BtnImage(CTkButton):
    def __init__(self, master, image, command):
        super().__init__(master, 
                         text= None,
                         image= image,
                         command= command,
                         fg_color= "#242424",
                         hover_color="#333333")