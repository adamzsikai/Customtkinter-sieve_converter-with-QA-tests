import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

mesh = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 140, 170, 200, 230, 270, 325, 400]
micron = [6730, 4760, 4000, 3360, 2830, 2380, 2000, 1680, 1410, 1190, 1000, 841, 707, 595, 500, 400, 354, 297, 250, 210, 177, 149, 125, 105, 88, 74, 63, 53, 44, 37]
milimeter = [6.73, 4.76, 4, 3.36, 2.83, 2.38, 2, 1.68, 1.41, 1.19, 1, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.125, 0.105, 0.088, 0.074, 0.063, 0.053, 0.044, 0.037]

def dropdownindicator(*args):

    val1 = Unit1.get()
    val2 = Unit2.get()

    if val1!= "UNITS:" and val2 != "UNITS:":
        button.configure(state="normal")

    else:
        button.configure(state="disabled")







def sifterunit():
    try:
        amount = float(amounte.get())
        Value1_selected = Unit1.get()
        Value2_selected = Unit2.get()

        if Value1_selected == Value2_selected:
            Result.set(amount)

        elif Value1_selected == "MESH" and Value2_selected == "MICRON":
            idx = mesh.index(int(amount))
            Result.set(micron[idx])

        elif Value1_selected == "MESH" and Value2_selected == "MILIMETER":
            idx = mesh.index(int(amount))
            Result.set(milimeter[idx])

        elif Value1_selected == "MICRON" and Value2_selected == "MESH":
            idx = micron.index(int(amount))
            Result.set(mesh[idx])

        elif Value1_selected == "MICRON" and Value2_selected == "MILIMETER":
            
            Result.set(amount/1000)

        elif Value1_selected == "MILIMETER" and Value2_selected == "MESH":
            idx = milimeter.index(float(amount))
            Result.set(mesh[idx])

        elif Value1_selected == "MILIMETER" and Value2_selected == "MICRON":
            
            Result.set(int(amount*1000))
        else:
            Result.set("NOT FOUND.")
    except ValueError:
        Result.set("VALUE ERROR!")
    except Exception as e:
        Result.set(f"ERROR: {e}")

win = ctk.CTk()
win.geometry("370x270")
win.title("Sieve size converter")
win.resizable(False, False)

ctk.CTkLabel(win,font=("Helvetica",14),text="SIEVE SIZE:",text_color="#04F1F1").grid(row=2,column=1,pady=10,padx=10)
amounte=ctk.CTkEntry(master=win, width=220,height=35,text_color="black",font=("Helvetica",14),fg_color="#F8CB00",corner_radius=10)
amounte.grid(row=2,column=2,pady=10, padx=10)

ctk.CTkLabel(win,font=("Helvetica",14),text="FROM:",text_color="#04F1F1").grid(row=3,column=1,pady=10,padx=10)
Unit1=ctk.StringVar(value="UNITS:")
Unitt=ctk.CTkOptionMenu(win,variable=Unit1,width=170,corner_radius=10,values=["MICRON", "MESH", "MILIMETER"],command=dropdownindicator)
Unitt.grid(row=3,column=2,pady=10, padx=10)

ctk.CTkLabel(win,font=("Helvetica",14),text="TO:",text_color="#04F1F1").grid(row=4,column=1,pady=10,padx=10)
Unit2=ctk.StringVar(value="UNITS:")
Unite=ctk.CTkOptionMenu(win,variable=Unit2,width=170,corner_radius=10,values=["MICRON", "MESH", "MILIMETER"],command=dropdownindicator)
Unite.grid(row=4,column=2,pady=10, padx=10)



Result=ctk.StringVar()

ctk.CTkLabel(win,font=("Helvetica",14),text="RESULT:",text_color="#04F1F1").grid(row=5,column=1,pady=10,padx=10)
ctk.CTkLabel(win,textvariable=Result,font=("Helvetica",14),text_color="black",width=220,height=35,text="RESULT:",fg_color="#F8CB00",corner_radius=10).grid(row=5,column=2,pady=10,padx=10)

button=ctk.CTkButton(win,text="CONVERT",command=sifterunit,font=("Helvetica",14),width=140,text_color="black",corner_radius=10,fg_color="#04F1F1",hover_color="#6B04F1")
button.grid(row=6,column=2,pady=15,padx=0)
button.configure(state="disabled")

win.mainloop()
