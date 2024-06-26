from src.image import *
from src.window import Window
from customtkinter import CTkImage
from pathlib import Path

MASTER= Window(750, 500, "Simple PicViewer", True)
PATH= Path(__file__).parent / "assets"
#IMGs
imgs_list= get_imgs(PATH)
PREVIOUS_PHOTO_BUTTON_IMG = create_image(PATH / "arrow1.png")
NEXT_PHOTO_BUTTON_IMG = create_image(PATH / "arrow2.png")
ROTATE_BUTTON_IMG= create_image(PATH / "rotate.png")
DELETE_BUTTON_IMG= create_image(PATH / "delete.png")
FULLSCREEN_BUTTON_IMG= create_image(PATH / "fullscreen.png")