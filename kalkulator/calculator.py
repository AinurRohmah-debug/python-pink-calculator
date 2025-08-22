from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR")
root.geometry("340x430")
root["bg"]= "#ffc0cb"   

myfont= font.Font(size=15)

# ==== FRAME BIAR KE TENGAH ====
main_frame = Frame(root, bg="#00040c")
main_frame.place(relx=0.5, rely=0.5, anchor="center")  # auto center

# Entry
e = Entry(main_frame,width=15,borderwidth=5,justify="right")

# Remove this line if you want to allow manual typing in the entry
e.bind("<Key>", lambda event: "break") # # Prevents the user from typing directly into the entry

e["font"] = myfont
e["bg"]= "#fff0f5"  # LavenderBlush (soft pink)  
e.grid(row=0,column=0,columnspan=4,padx=10,pady=15)

# ===== FUNGSI =====
def angka(nilai):
    sebelum = e.get()

    # If the entry currently shows 'Error', clear it before inserting the new value
    if sebelum == 'Error':
       e.delete(0, END)
       e.insert(0, str(nilai)) 
    else:
        e.insert(END, str(nilai))

def tambah():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "penjumlahan"
    e.delete(0,END)

def kurang():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "pengurangan"
    e.delete(0,END)

def kali():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "perkalian"
    e.delete(0,END)

def bagi():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "pembagian"
    e.delete(0,END)

def hapus():
    e.delete(0,END)

def akar():
    n_awal = float(e.get())
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))

def pangkat():
    n_awal = float(e.get())
    e.delete(0,END)
    e.insert(0,n_awal**2)

def sisabagi():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "sisabagi"
    e.delete(0,END)

def samadengan():
    global mtk, n_awal
    try:
        # kalau belum ada operasi, jangan ngapa-ngapain
        if mtk is None:
            return  

        nomor_akhir = e.get()
        e.delete(0,END)

        if mtk == "penjumlahan":
            hasil = n_awal + float(nomor_akhir)
        elif mtk == "pengurangan":
            hasil = n_awal - float(nomor_akhir)
        elif mtk == "perkalian":
            hasil = n_awal * float(nomor_akhir)
        elif mtk == "pembagian":
            hasil = n_awal / float(nomor_akhir)
        elif mtk == "sisabagi":
            hasil = n_awal % float(nomor_akhir)
        else:
            hasil = "Error"

        e.insert(0, hasil)
        mtk = None  
        n_awal = hasil 
    except:
        e.insert(0, "Error")


# ===== TOMBOL =====
btn1 = Button(main_frame,bg="#ff1493",fg="white",text="1",width=5,height=2,command=lambda:angka(1))
btn2 = Button(main_frame,bg="#ff1493",fg="white",text="2",width=5,height=2,command=lambda:angka(2))
btn3 = Button(main_frame,bg="#ff1493",fg="white",text="3",width=5,height=2,command=lambda:angka(3))
btn4 = Button(main_frame,bg="#ff1493",fg="white",text="4",width=5,height=2,command=lambda:angka(4))
btn5 = Button(main_frame,bg="#ff1493",fg="white",text="5",width=5,height=2,command=lambda:angka(5))
btn6 = Button(main_frame,bg="#ff1493",fg="white",text="6",width=5,height=2,command=lambda:angka(6))
btn7 = Button(main_frame,bg="#ff1493",fg="white",text="7",width=5,height=2,command=lambda:angka(7))
btn8 = Button(main_frame,bg="#ff1493",fg="white",text="8",width=5,height=2,command=lambda:angka(8))
btn9 = Button(main_frame,bg="#ff1493",fg="white",text="9",width=5,height=2,command=lambda:angka(9))
btn0 = Button(main_frame,bg="#ff1493",fg="white",text="0",width=5,height=2,command=lambda:angka(0))

tam = Button(main_frame,fg="#ff69b4",text="+",width=5,height=2,command=tambah)
kur = Button(main_frame,fg="#ff69b4",text="-",width=5,height=2,command=kurang)
kal = Button(main_frame,fg="#ff69b4",text="*",width=5,height=2,command=kali)
bag = Button(main_frame,fg="#ff69b4",text="/",width=5,height=2,command=bagi)

hap = Button(main_frame,bg="#db7093",fg="white",text="C",width=5,height=2,command=hapus)
sam = Button(main_frame,bg="#db7093",fg="white",text="=",width=5,height=2,command=samadengan)  
kom = Button(main_frame,bg="#db7093",fg="white",text="•",width=5,height=2,command=lambda:angka("."))

ak = Button(main_frame,fg="#ff69b4",text="√",width=5,height=2,command=akar)
sisa = Button(main_frame,fg="#ff69b4",text="%",width=5,height=2,command=sisabagi)
pang = Button(main_frame,fg="#ff69b4",text="^2",width=5,height=2,command=pangkat)

# grid tombol
hap.grid(row=1,column=0,pady=2)
bag.grid(row=1,column=1,pady=2)
sisa.grid(row=1,column=2,pady=2)
kal.grid(row=1,column=3,pady=2)

btn7.grid(row=2,column=0,pady=2)
btn8.grid(row=2,column=1,pady=2)
btn9.grid(row=2,column=2,pady=2)
tam.grid(row=2,column=3,pady=2)

btn4.grid(row=3,column=0,pady=2)
btn5.grid(row=3,column=1,pady=2)
btn6.grid(row=3,column=2,pady=2)
kur.grid(row=3,column=3,pady=2)

btn1.grid(row=4,column=0,pady=2)
btn2.grid(row=4,column=1,pady=2)
btn3.grid(row=4,column=2,pady=2)
kom.grid(row=4,column=3,pady=2)

btn0.grid(row=5,column=1,pady=2)
pang.grid(row=5,column=0,pady=2)
ak.grid(row=5,column=2,pady=2)
sam.grid(row=5,column=3,pady=2)

root.mainloop()
