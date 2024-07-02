from customtkinter import CTk, set_appearance_mode

class Window(CTk):
    def __init__(self, w: int, h: int, title: str, resizable: bool):
        """Inicializa uma janela personalizada com largura, altura, título e redimensionamento."""
        super().__init__()
        self.title(title)
        self.minsize(w, h)
        self.state("zoomed")
        self.resizable(resizable, resizable)
        set_appearance_mode("dark")
        
        self.columnconfigure(1, weight=5)  # Configura o gerenciamento de layout para expansão
        self.rowconfigure(1, weight=2)

    def fullscreen(self):
        """Ativa ou desativa o modo de tela cheia."""
        if not self.attributes("-fullscreen"):
            self.attributes("-fullscreen", True)
        else:
            self.attributes("-fullscreen", False)