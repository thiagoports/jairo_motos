from django.db import models
from django.conf import settings


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
        return f"https://wa.me/{numero}?text={mensagem.replace(' ', '%20')}"

    def whatsapp_footer(self):
        numero = "5583991945349"
        return f"https://wa.me/{numero}"


class AcessorioChoices(models.TextChoices):
    CAPACETE = 'CAPACETE', 'Capacete'
    LUVA = 'LUVA', 'Luva'
    BOTA = 'BOTA', 'Bota'
    JOELHEIRA = 'JOELHEIRAS', 'Joelheira'
    JAQUETA = 'JAQUETA', 'Jaqueta'


class Acessorio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='acessorios/', blank=True, null=True)

    tipo = models.CharField(
        max_length=20,
        choices=AcessorioChoices.choices,
        default=AcessorioChoices.CAPACETE
    )

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def link_whatsapp(self):
        numero = "5583991945349"
        linhas = []

        for item in self.itens.select_related('moto'):
            linhas.append(
                f"{item.quantidade}x {item.moto.modelo} ({item.moto.ano})")

        mensagem = "Olá! Tenho interesse nas seguintes motos:\n" + \
            "\n".join(linhas)
        mensagem_url = mensagem.replace(" ", "%20").replace("\n", "%0A")

        return f"https://wa.me/{numero}?text={mensagem_url}"


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name='itens')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
