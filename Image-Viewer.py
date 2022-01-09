
# ============= Image Viewer Application (VISHAL MAURYA)==============
from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog,messagebox
root=Tk()
root.title('Image Viewer')
root.geometry(str(root.winfo_screenwidth()-50)+'x'+str(root.winfo_screenheight()-70)+'+20+20')
root.winfo_rooty()
root.iconbitmap(r'C:/Users/rmaur/Desktop/python/GUI/image/favicon.ico')
print(os.system('dir'))
print(os.getcwd())
# ---------------Browse filedialog & Collectin all Image List--------------------
def show_files():
    global image_list
    global lable
    global my_image
    global index
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="select Image files",filetypes=(("PNG file",'*.png'),("JPG Files","*.jpg"),("All Files","*.*")))

    # ------------Open Choosen files----------

    lable.grid_forget()
    try:
        my_image = ImageTk.PhotoImage(Image.open(filename).resize((800,550), Image.ANTIALIAS))

    except Exception as e:
        if filename=="":
            pass
        else:
            messagebox.showwarning("Warning","Please select image file!")
        filename="C:/Users/rmaur/Desktop/python/GUI/image/sorry.jpg"
        my_image = ImageTk.PhotoImage(Image.open(filename).resize((800,550), Image.ANTIALIAS))
        print(e)

    lable = Label(image=my_image)
    lable.grid(row=1, column=0, columnspan=3,pady=5,padx=(root.winfo_width()-my_image.width())/2)
    # -------------Collectin this image related all images in their directory------------
    filepath=os.path.dirname(filename)
    path=Label(root,text=filepath,font=('italic',12,'normal'),borderwidth=2,state=DISABLED)
    path.grid(row=0,column=1,sticky=W+E,ipadx=15,ipady=8,pady=10)
    image_list = os.listdir(filepath)
    formate_ls = ['.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.ico']
    temp = list()
    # -----------Filtering images from collected files----------------
    for item in image_list:
        file_ext = os.path.splitext(item)
        if file_ext[1] not in formate_ls:
            temp.append(item)
    for item in temp:
        image_list.remove(item)
    basename=os.path.basename(filename)
    image_list.sort()
    index=image_list.index(basename)
    print(image_list,index,os.path.dirname(filename))

#     ----------------Disabling Forword and Backword button----------
#     -----If there is only one image in image_list
    if len(image_list) == 1:
        lable_forword = Button(root, text='>>', padx=20, pady=5, state=DISABLED).grid(row=2, column=2)
        lable_back = Button(root, text='<<', padx=20, pady=5, state=DISABLED).grid(row=2, column=0)
    else:
        # -------If first image select then back is disabled
        if index==0:
            lable_forword = Button(root, text='>>', padx=20, pady=5, command=lambda :forward(index)).grid(row=2, column=2)
            lable_back = Button(root, text='<<', padx=20, pady=5, state=DISABLED).grid(row=2, column=0)
        elif (len(image_list)==index+1):
            lable_forword = Button(root, text='>>', padx=20, pady=5, state=DISABLED).grid(row=2,column=2)
            lable_back = Button(root, text='<<', padx=20, pady=5,command=lambda: backward(index)).grid(row=2, column=0)
        else:
            lable_forword = Button(root, text='>>', padx=20, pady=5, command=lambda: forward(index)).grid(row=2,
                                                                                                          column=2)
            lable_back = Button(root, text='<<', padx=20, pady=5, command=lambda: backward(index)).grid(row=2, column=0)


# ?------------------Button to browse files-------------
path_button=Button(root,text='Browse',padx=50,pady=5,font=('arial',10,'bold'),bd=5,command=show_files)
path_button.grid(row=0,column=0,padx=250)



# =======================Backword button Creation===========
def backward(number):
    # print("Image number= ",number)
    global image_resize
    global lable
    global my_image
    global lable_forword
    global lable_back
    global index
    global filename
    index -=1
    lable.grid_forget()
    my_image=ImageTk.PhotoImage(Image.open(os.path.dirname(filename)+'/'+image_list[number-1]).resize((800,550),Image.ANTIALIAS))
    lable=Label(image=my_image)
    lable.grid(row=1, column=0, columnspan=3,pady=5,padx=(root.winfo_width()-my_image.width())/2)
    if index==0:
        lable_back = Button(root, text='<<', padx=20, pady=5,state=DISABLED).grid(row=2,column=0)
    if index+2 == len(image_list):
        lable_forword=Button(root,text='>>',padx=20,pady=5,command=lambda :forward(index),font=('arial',10,'bold'),bd=5).grid(row=2,column=2)


# =======================Foreword button Creation===========

def forward(number):
    # print("Image number= ",number)
    global image_resize
    global lable
    global my_image
    global lable_forword
    global lable_back
    global index
    global filename
    lable.grid_forget()
    index +=1
    my_image=ImageTk.PhotoImage(Image.open(os.path.dirname(filename)+'/'+image_list[number+1]).resize((800,550),Image.ANTIALIAS))
    lable=Label(image=my_image)
    lable.grid(row=1, column=0, columnspan=3,pady=5,padx=(root.winfo_width()-my_image.width())/2)
    if index==1:
        lable_back = Button(root, text='<<', padx=20, pady=5, command=lambda: backward(index),
                            font=('arial', 10, 'bold'), bd=5).grid(row=2, column=0)
    print(index,len(image_list))

    if index+1 == len(image_list):
        lable_forword = Button(root, text='>>', padx=20, pady=5, state=DISABLED).grid(row=2, column=2)

# ============Opening Default Image for first Time


my_image=ImageTk.PhotoImage(Image.open('sorry.jpg').resize((800,550),Image.ANTIALIAS))
print(my_image.height(),my_image.width()/2)
lable = Label(image=my_image)
lable.grid(row=1, column=0, columnspan=3,pady=5,padx=(root.winfo_width()-my_image.width())/2)
lable_forword=Button(root,text='>>',padx=20,pady=5,state=DISABLED,font=('arial',10,'bold'),bd=5).grid(row=2,column=2)
lable_exit=Button(root,text="Exit",padx=20,pady=5,command=root.quit,font=('arial',10,'bold'),bd=5).grid(row=2,column=1,pady=8)
lable_back=Button(root,text='<<',padx=20,pady=5,state=DISABLED,font=('arial',10,'bold'),bd=5).grid(row=2,column=0,padx=5)

root.mainloop()