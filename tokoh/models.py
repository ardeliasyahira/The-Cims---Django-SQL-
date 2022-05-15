from django.db import models

# Create your models here.
WARNA_KULIT_CHOICES = [
    ('#f0067e', '#f0067e'),
    ('#fa1ec8', '#fa1ec8'),
    ('#a823d2', '#a823d2'),
    ('#afa825', '#afa825'),
]

JENIS_KELAMIN_CHOICES = [
    ('Laki-laki', 'Laki-laki'),
    ('Perempuan', 'Perempuan'),
]

PEKERJAAN_CHOICES = [
    ('Pelukis ', 'Pelukis'),
    ('Programmer', 'Programmer'),
    ('Komedian', 'Komedian'),
    ('Businessman', 'Businessman'),
    ('Atlet', 'Atlet'),
]

class Tokoh(models.Model):
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES, default='Perempuan', max_length=9)
    warna_kulit = models.CharField(choices=WARNA_KULIT_CHOICES, default='#f0067e', max_length=7)
    pekerjaan = models.CharField(choices=PEKERJAAN_CHOICES, default='Pelukis', max_length=11)

    def __str__(self):
        return self.nama