from django.shortcuts import get_object_or_404, render

from .moderls import Profil


def index(request):
    profil = get_object_or_404(Profil, pk=2)
    context = {"profil": profil, "keahlian": profil.keahlian_set.all()}
    return render(request, "cv/index.html", context)
