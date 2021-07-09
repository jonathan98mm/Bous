from django.shortcuts import render
from django.http import HttpResponseRedirect
import psycopg2
import openpyxl
import xlrd

# Create your views here.
from Excel.forms import DocumentoForm
from Excel.models import Documento


def guardar_archivo(file):
    with open(file.name, "wb+") as destino:
        for chunk in file.chunks():
            destino.write(chunk)


def guardar_a_bd(file):
    conn = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host="db")
    cur = conn.cursor()
    print("Base abierta")
    
    if file.name.endswith(".xls"):
        table_name = file.name[:len(file.name) - 4].replace(" ", "_")
        
        create = f"CREATE TABLE {table_name} ("
        insert = f"INSERT INTO {table_name} ("
        
        return True
    elif file.name.endswith(".xlsx"):
        table_name = file.name[:len(file.name) - 5].replace(" ", "_")
        
        create = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        insert = f"INSERT INTO {table_name} ("
        
        workbook = openpyxl.load_workbook(file.name, read_only=True)
        ws = workbook.active
        
        cabeceros = list(ws.rows)[0]
        aux = list(ws.rows)[1]
        
        for i in range(len(cabeceros)):
            cadena = cabeceros[i].value.replace(" ", "_")
            create += f"{cadena} "
            
            if(i == len(cabeceros)-1):
                if aux[i].number_format == "General":
                    create += "varchar"
                elif aux[i].number_format == "mm-dd-yy":
                    create += "date"
                
                insert += f"{cadena}"
            else:
                if aux[i].number_format == "General":
                    create += "varchar, "
                elif aux[i].number_format == "mm-dd-yy":
                    create += "date, "
                    
                insert += f"{cadena}, "
                
        create += ");"
        insert += ") VALUES "
                
        print(create)
        
        cur.execute(create)
        conn.commit()
        
        aux = list(ws.rows)
        
        for i in range(1, len(aux)):
            for j in range(len(aux[i])):
                
                if j == 0:
                    insert += "("
                
                if i == ws.max_row -1:
                    if j == ws.max_column - 1:
                        insert += f"'{aux[i][j].value}'); "
                    else:
                        insert += f"'{aux[i][j].value}', "
                else:
                    if j == ws.max_column - 1:
                        insert += f"'{aux[i][j].value}'), "
                    else:
                        insert += f"'{aux[i][j].value}', "
        
        print(insert)
        
        cur.execute(insert)
        conn.commit()
        cur.close()
        conn.close()
                    
        return True
    else:
        return False
        

def principal(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)

        if form.is_valid():

            guardar_archivo(request.FILES["file"])
            
            if guardar_a_bd(request.FILES["file"]):
                return render(request, "exito.html", {"mensaje": "¡Excel cargado con exito!"})
            else:
                return HttpResponseRedirect("error")
    else:
        form = DocumentoForm()

    return render(request, "principal.html", {"form": form})

def exito(request):
    return render(request, "exito.html")

def info(request):
    return render(request, "info.html")