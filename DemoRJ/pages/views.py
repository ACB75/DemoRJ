import datetime

from django.shortcuts import redirect, render
from DemoRJ.pages.models import Registro, Person
from datetime import datetime, date


def welcome(req):
    p = Person.objects.get(pk=1)
    r = Registro.objects.get(person_id=p.id)
    if r.registro_inicio:
        contador_jornada = datetime.combine(date.today(), datetime.now().time()) - datetime.combine(date.today(), r.registro_inicio.time())
        return render(req, "home.html", {"person": p, "contador_jornada": contador_jornada})

    return render(req, "home.html", {"person": p})


def registrar_jornada(req):
    if req.GET["registro_inicio"]:
        p = Person.objects.get(pk=1)
        registro_inicio = req.GET["registro_inicio"]
        Registro.objects.create(registro_inicio=registro_inicio, registro_fin="null",
                                propuesta_inicio="null", propuesta_fin="null", person_id=p.id)

        return render(req, "home.html", {"person": p, "registro_inicio": registro_inicio})


def finalizar_jornada(req):
    if req.GET["registro_fin"]:
        p = Person.objects.get(pk=1)
        registro_fin = req.GET["registro_fin"]
        r = Registro.objects.get(person_id=p.id)
        r.registro_fin = registro_fin
        r.save()

        return render(req, "home.html",
                      {"person": p, "registro_fin": registro_fin, "registro_inicio": r.registro_inicio})
