from django.shortcuts import render
from django.http import HttpResponseRedirect
import psycopg2
import openpyxl

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

    table_name = file.name[:len(file.name) - 5]
    print(table_name)

    workbook = openpyxl.load_workbook(file.name)




    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ()")

def principal(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)

        if form.is_valid():

            guardar_archivo(request.FILES["file"])
            guardar_a_bd(request.FILES["file"])

            return HttpResponseRedirect("exito")
    else:
        form = DocumentoForm()

    return render(request, "principal.html", {"form": form})

def exito(request):
    return render(request, "exito.html")