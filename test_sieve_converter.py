from unit_test_sc import sifterunit
import pytest



def test_integer_input():
    assert sifterunit(1000,"MICRON","MILLIMETER") == "1"
    assert sifterunit(1000,"MICRON","MESH") == 18
    assert sifterunit(1,"MILLIMETER","MESH") == 18

def test_float_input():
    assert sifterunit(1000.0,"MICRON","MILLIMETER") == "1"
    assert sifterunit(1000.0,"MICRON","MESH") == 18
    assert sifterunit(1.0,"MILLIMETER","MESH") == 18
    

def test_string_input():
    assert sifterunit("1000.0","MICRON","MILLIMETER") == "1"
    assert sifterunit("1000.0","MICRON","MESH") == 18
    assert sifterunit("1.0","MILLIMETER","MESH") == 18

    assert sifterunit("ab","MICRON","MILLIMETER") == "VALUE ERROR!"
    assert sifterunit("ab","MICRON","MESH") == "VALUE ERROR!"
    assert sifterunit("ab","MILLIMETER","MESH") == "VALUE ERROR!"
    assert sifterunit("ab","MILLIMETER","MICRON") == "VALUE ERROR!"


def test_same_selected():
    assert sifterunit(500,"MICRON","MICRON") == "500"
    assert sifterunit(1000,"MICRON","MICRON") == "1000"
    assert sifterunit(1000.0,"MICRON","MICRON") == "1000"

    assert sifterunit(18,"MESH","MESH") == "18"
    assert sifterunit(18.0,"MESH","MESH") == "18"
    
    assert sifterunit(3,"MILLIMETER","MILLIMETER") == "3"
    assert sifterunit(3.0,"MILLIMETER","MILLIMETER") == "3"
    assert sifterunit(3.2,"MILLIMETER","MILLIMETER") == "3.2"
   



def test_mesh_to_micron():
    assert sifterunit(18,"MESH","MICRON") == 1000
    assert sifterunit(10,"MESH","MICRON") == 2000
    assert sifterunit(400,"MESH","MICRON") == 37
    

def test_micron_to_mesh():
    assert sifterunit(1000,"MICRON","MESH") == 18
    assert sifterunit(2000,"MICRON","MESH") == 10
    assert sifterunit(37,"MICRON","MESH") == 400
    

def test_micron_to_millimeter():
    assert sifterunit(3000,"MICRON","MILLIMETER") == "3"
    assert sifterunit(3200,"MICRON","MILLIMETER") == "3.2"
    assert sifterunit(3250.0,"MICRON","MILLIMETER") == "3.25"

def test_millimeter_to_micron():
    assert sifterunit(3,"MILLIMETER","MICRON") == 3000
    assert sifterunit(3.2,"MILLIMETER","MICRON") == 3200
    assert sifterunit(3.25,"MILLIMETER","MICRON") == 3250
    

def test_millimeter_to_mesh():
    assert sifterunit(6.73,"MILLIMETER","MESH") == 3
    assert sifterunit(1,"MILLIMETER","MESH") == 18
    assert sifterunit(0.4,"MILLIMETER","MESH") == 40
    

def test_mesh_to_millimeter():
    assert sifterunit(3,"MESH","MILLIMETER") == 6.73
    assert sifterunit(18,"MESH","MILLIMETER") == 1
    assert sifterunit(40,"MESH","MILLIMETER") == 0.4
    

def test_negative_edge():
    assert sifterunit(15,"MESH","MILLIMETER") == "VALUE ERROR!" #not existing value
    assert sifterunit(99999999,"MICRON","MILLIMETER") == "100000"
    assert sifterunit(6.73,"MILLIMETER","MICRON") == 6730
    assert sifterunit(9999,"MILLIMETER","MICRON") == 9999000

    assert sifterunit((-18),"MESH","MILLIMETER") == "VALUE ERROR!"
    assert sifterunit((-999),"MICRON","MILLIMETER") == "VALUE ERROR!"
    assert sifterunit((-3),"MILLIMETER","MICRON") == "VALUE ERROR!" 

    


