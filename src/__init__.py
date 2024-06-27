from src.image import *
from src.window import Window
from customtkinter import CTkImage
from pathlib import Path

MASTER= Window(750, 500, "Simple PicViewer", True)
PATH= Path(__file__).parent / "assets"
#IMGs
imgs_list= get_imgs(PATH)
PREVIOUS_PHOTO_BUTTON_IMG = create_image(PATH / "arrow1_icon.png")
NEXT_PHOTO_BUTTON_IMG = create_image(PATH / "arrow2_icon.png")
FOLDER_BUTTON_IMG = create_image(PATH / "folder_icon.png")
ROTATE_BUTTON_IMG= create_image(PATH / "rotate_icon.png")
DELETE_BUTTON_IMG= create_image(PATH / "delete_icon.png")
FULLSCREEN_BUTTON_IMG= create_image(PATH / "fullscreen_icon.png")