from django.http import Http404
from django.shortcuts import render

from .models import Profil


def index(request):
    profil = Profil.objects.order_by("-pk").first()
    if profil is None:
        raise Http404("Profil belum diisi. Isi dulu lewat /admin/.")

    context = {
        "profil": profil,
        "keahlian": profil.keahlian_set.all(),
        "pendidikan": profil.pendidikan_set.all(),
        "proyek": profil.proyek_set.all(),
    }
    return render(request, "cv/index.html", context)
