from tkinter import*
import random
root=Tk()
root.title("Color")
root.geometry("460x460")
root.config(bg="PeachPuff")
ls=Label(root,text="Score: ",font=("Bahnschrift Light",15),bg="PeachPuff")
ls.place(relx=0.5,rely=0.4,anchor=CENTER)
l=Label(root,font=("times",25,"bold"),bg="white")
l.place(relx=0.5,rely=0.5,anchor=CENTER)
iv=Entry(root)
iv.pack()
class GR:
    def __init__(self):
        self.__score=0
        def updategame(self):
            self.t=["RoyalBlue","Moccasin","PeachPuff","Aquamarine","Teal"]
            self.tr=randiom.randint(0,4)
            self.c=["RoyalBlue","Moccasin","PeachPuff","Aquamarine","Teal"]
            self.cr=random.randint(0,4)
            l["text"]=self.t[self.tr]
            l["fg"]=self.c[self.cr]
            def __updatescore(self,iv):
                if(iv==self.c[self.cr]):
                    print(self.c[self.cr])
                    self.__score=self.__score+random.randint(0,10)
                    ls["text"]="Score: "+ str(self.__score)
            def guv(self,iv):
                print("hello")
obj1=GR(iv,updategame)
def gi():
    v=iv.get()
    obj1.guv(v)
    obj1.updategame()
    iv.delete(0,END)
    
btn=Button(root, text="START",command=obj1.updategame, bg="dark olive green", fg="white",
           relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn1=Button(root, text="START",command=guv, bg="dark olive green", fg="white",
           relief=FLAT, padx=10, pady=1, font=("Arial",15))
root.mainloop()