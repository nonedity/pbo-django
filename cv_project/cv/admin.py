from django.contrib import admin

from .models import Keahlian, Pendidikan, Profil, Proyek


class KeahlianInline(admin.TabularInline):
    model = Keahlian
    extra = 1


class PendidikanInline(admin.TabularInline):
    model = Pendidikan
    extra = 1


class ProyekInline(admin.StackedInline):
    model = Proyek
    extra = 1


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("nama", "profesi", "email")
    inlines = [KeahlianInline, PendidikanInline, ProyekInline]
