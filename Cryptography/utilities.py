# -*- coding: utf-8 -*-
def InputText():
    code = raw_input("Code:").upper()
    code = code.replace(" ","")
    code = code.replace(".","")
    code = code.replace(",","")
    code = code.replace(":","")
    code = code.replace(";","")
    code = code.replace("!","")
    code = code.replace('"',"")
    code = code.replace("$","")
    code = code.replace("%","")
    code = code.replace("(","")
    code = code.replace(")","")
    code = code.replace("/","")
    code = code.replace("?","")
    code = code.replace("@","")
    code = code.replace("#","")
    code = code.replace("'","")
    code = code.replace("’","")
    code = code.replace("1","")
    code = code.replace("2","")
    code = code.replace("3","")
    code = code.replace("4","")
    code = code.replace("5","")
    code = code.replace("6","")
    code = code.replace("7","")
    code = code.replace("8","")
    code = code.replace("9","")
    code = code.replace("0","")
    code = code.replace("-","")
    code = code.replace("=","")
    return code
    
