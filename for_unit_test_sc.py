def sifterunit(amount,Value1_selected,Value2_selected):
    mesh = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 100, 120, 140, 170, 200, 230, 270, 325, 400]
    micron = [6730, 4760, 4000, 3360, 2830, 2380, 2000, 1680, 1410, 1190, 1000, 841, 707, 595, 500, 400, 354, 297, 250, 210, 177, 149, 125, 105, 88, 74, 63, 53, 44, 37]
    milimeter = [6.73, 4.76, 4, 3.36, 2.83, 2.38, 2, 1.68, 1.41, 1.19, 1, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.125, 0.105, 0.088, 0.074, 0.063, 0.053, 0.044, 0.037]

    try:
        amount = float(amount)
       
        if amount<=0:
            return("VALUE ERROR!")

        elif Value1_selected == Value2_selected:
            return(f"{amount:g}")

        elif Value1_selected == "MESH" and Value2_selected == "MICRON":
            idx = mesh.index(int(amount))
            return(micron[idx])

        elif Value1_selected == "MESH" and Value2_selected == "MILLIMETER":
            idx = mesh.index(int(amount))
            return(milimeter[idx])

        elif Value1_selected == "MICRON" and Value2_selected == "MESH":
            idx = micron.index(int(amount))
            return(mesh[idx])

        elif Value1_selected == "MICRON" and Value2_selected == "MILLIMETER":
            fin = amount/1000
            return(f"{fin:g}")

        elif Value1_selected == "MILLIMETER" and Value2_selected == "MESH":
            idx = milimeter.index(float(amount))
            return(mesh[idx])

        elif Value1_selected == "MILLIMETER" and Value2_selected == "MICRON":
            
            return(int(amount*1000))
        else:
            return("VALUE ERROR!")
    except ValueError:
        return("VALUE ERROR!")
    except Exception as e:
        return(f"ERROR: {e}")


