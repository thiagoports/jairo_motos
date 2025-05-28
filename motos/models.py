from django.db import models

class MarcaChoices(models.TextChoices):
    HONDA = 'HONDA', 'Honda'
    AVELLOZ = 'AVELLOZ', 'Avelloz'
    SHINERAY = 'SHINERAY', 'Shineray'
    YAMAHA = 'YAMAHA', 'Yamaha'


class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='motos/')
    
    marca = models.CharField(
        max_length=20,
        choices=MarcaChoices.choices,
        default=MarcaChoices.HONDA
    )

    def __str__(self):
        return f"{self.modelo} - {self.get_marca_display()}"

    def link_whatsapp(self):
        numero = "5583991945349"
        mensagem = f"Olá, tenho interesse na moto {self.marca} {self.modelo} ({self.ano})!"
        return f"https://wa.me/{numero}?text={mensagem.replace(" ", "%20")}"
    
    def whatsapp_footer(self):
        numero = "5583991945349"
        return f"https://wa.me/{numero}"