from django.core.exceptions import ValidationError
from django.db import models


class Profil(models.Model):
    nama = models.CharField(max_length=100)
    profesi = models.CharField(max_length=100)
    email = models.EmailField()
    tentang = models.TextField()
    foto = models.ImageField(
        upload_to="foto/",
        blank=True,
        help_text="Opsional. Jika kosong, dipakai foto bawaan dari folder static.",
    )

    class Meta:
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.nama


class Keahlian(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Keahlian"

    def __str__(self):
        return self.nama


class Pendidikan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    institusi = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    tahun_mulai = models.PositiveSmallIntegerField()
    tahun_selesai = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Kosongkan jika masih berjalan.",
    )

    class Meta:
        ordering = ["-tahun_mulai"]
        verbose_name_plural = "Pendidikan"

    def __str__(self):
        return f"{self.jurusan} - {self.institusi}"

    def clean(self):
        if self.tahun_selesai and self.tahun_selesai < self.tahun_mulai:
            raise ValidationError(
                "Tahun selesai tidak boleh lebih kecil dari tahun mulai."
            )


class Proyek(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    judul = models.CharField(max_length=100)
    tahun = models.PositiveSmallIntegerField()
    deskripsi = models.TextField(blank=True)
    tautan = models.URLField(
        blank=True, help_text="Opsional, mis. link GitHub atau demo."
    )

    class Meta:
        ordering = ["-tahun"]
        verbose_name_plural = "Proyek"

    def __str__(self):
        return self.judul
