from src import *

class App:
    def __init__(self):
        self.path= Path()
        self.index= 0
        self.btn_right= BtnImage(MASTER,
                                 image= PREVIOUS_PHOTO_BUTTON_IMG,
                                 command= self.prev_image)
                                  
        self.btn_Left= BtnImage(MASTER,
                                image= NEXT_PHOTO_BUTTON_IMG,
                                command= self.next_image)

        self.btn_rotate= BtnImage(MASTER,
                                  image= ROTATE_BUTTON_IMG,
                                  command= self.rotate_image)
       
        self.btn_delete= BtnImage(MASTER,
                                  image= DELETE_BUTTON_IMG, 
                                  command= self.delete_image)
                                   
        self.btnzoom= BtnImage(MASTER,
                               image= FULLSCREEN_BUTTON_IMG,
                               command= MASTER.fullscreen)
                               
        self.btn_right.grid(row=1, column=0, sticky="nsew")
        self.btn_Left.grid(row=1, column=4, sticky="nsew")
        self.btn_rotate.grid(row=2, column=0, sticky="nsew")
        self.btn_delete.grid(row=2, column=1, columnspan=3, sticky="nsew")
        self.btnzoom.grid(row=2, column=4, sticky="nsew")
        
    def get_folder(self):
        folder= askdirectory()
        if Path(folder).is_dir():
            self.path= Path(folder)
        
    def render_image(self):
        try:
            imgs_list= get_imgs(self.path)
            img= create_image(imgs_list[self.index])
            self.img_lbl= CTkLabel(MASTER, image= img, text= None)
        except IndexError:
            self.img_lbl= BtnImage(MASTER, 
                                   image= FOLDER_BUTTON_IMG,
                                   text= "Selecionar Pasta",
                                   command= self.get_folder)
        finally:
            self.img_lbl.grid(row=1, column=1, columnspan=3, sticky="nsew")
    
    def next_image(self):
        imgs_list= get_imgs(self.path)
        if self.index < len(imgs_list)-1:
            self.index+= 1
        MASTER.after(10, self.render_image)
    
    def prev_image(self):
        imgs_list= get_imgs(self.path)
        if self.index > 0:
            self.index-= 1
        MASTER.after(10, self.render_image)

    def rotate_image(self):
        imgs_list= get_imgs(self.path)
        with Image.open(imgs_list[self.index]) as img:
            img.rotate(90).save(imgs_list[self.index])
        MASTER.after(10, self.render_image)
            
    def delete_image(self):
        imgs_list= get_imgs(self.path)
        try:
            imgs_list[self.index].unlink()
        except FileNotFoundError:
            imgs_list[self.index].resolve().unlink()
        except IndexError: pass
        except PermissionError: pass
        finally:
            if self.index > 0:
                self.index-= 1
            MASTER.after(10, self.render_image)

    def run(self):
        MASTER.after(10, self.render_image)
        MASTER.mainloop()

if __name__ == "__main__":
    app=App()
    app.run()