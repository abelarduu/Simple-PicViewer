from src import *
from customtkinter import *

class App:
    def __init__(self):
        self.index= 0
        self.imgs_list= get_imgs(PATH)
        self.btn_right= BtnImage(MASTER,
                                 image= PREVIOUS_PHOTO_BUTTON_IMG,
                                 command= self.prev_image)
                                  
        self.btn_Left= BtnImage(MASTER,
                                image= NEXT_PHOTO_BUTTON_IMG,
                                command= self.next_image)
         
        self.btn_right.grid(row=1, column=0, sticky="nsew")
        self.btn_Left.grid(row=1, column=4, sticky="nsew")
        #estado	"normal" (padrão) ou "desativado" (não clicável, cor mais escura)
        
        self.btn_rotate= BtnImage(MASTER,
                                  image= PREVIOUS_PHOTO_BUTTON_IMG,
                                  command= None)
       
        self.btn_delete= BtnImage(MASTER,
                                  image= DELETE_BUTTON_IMG,
                                  command= None)
                                   
        self.btnzoom= BtnImage(MASTER,
                               image= NEXT_PHOTO_BUTTON_IMG,
                               command= MASTER.fullscreen)
                                
        self.btn_rotate.grid(row=2, column=0, sticky="nsew")
        self.btn_delete.grid(row=2, column=1, columnspan=3, sticky="nsew")
        self.btnzoom.grid(row=2, column=4, sticky="nsew")

    def img_center(self):
        self.img_lbl= CTkLabel(MASTER, image= self.imgs_list[self.index], text= None)
        self.img_lbl.grid(row=1, column=1, columnspan=3, sticky="nsew")
        
    def next_image(self):
        if self.index < len(self.imgs_list)-1:
            self.index+= 1
            MASTER.after(10, self.img_center)
        
    def prev_image(self):
        if self.index > 0:
            self.index-= 1
            MASTER.after(10, self.img_center)
            
    def run(self):
        MASTER.mainloop()
        
if __name__ == "__main__":
    app=App()
    app.run()