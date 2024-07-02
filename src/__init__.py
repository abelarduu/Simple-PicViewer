from src.image import *
from src.window import Window
from pathlib import Path

ASSETS_PATH= Path(__file__).parent / "assets"
MASTER= Window(750, 500, "Simple PicViewer", True)

#IMGs
PREVIOUS_PHOTO_BUTTON_IMG = create_image(ASSETS_PATH / "arrow1_icon.png")
NEXT_PHOTO_BUTTON_IMG = create_image(ASSETS_PATH / "arrow2_icon.png")
FOLDER_BUTTON_IMG = create_image(ASSETS_PATH / "folder_icon.png")
ROTATE_BUTTON_IMG= create_image(ASSETS_PATH / "rotate_icon.png")
DELETE_BUTTON_IMG= create_image(ASSETS_PATH / "delete_icon.png")
FULLSCREEN_BUTTON_IMG= create_image(ASSETS_PATH / "fullscreen_icon.png")
