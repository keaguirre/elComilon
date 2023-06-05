from django.db import models

# Create your models here.

class Registro(models.Model):
    def __str(self):
        return self.registro

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=30, default='Armando casas')
    password = models.CharField(max_length=15, default='●●●●●●●')
    dir_entrega = models.CharField(max_length=40, default='av. falsa 123', blank=True)
    #pedidos = models.ForeignKey(Pedido, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_imagen_producto = models.CharField(max_length=50, default='default_value')
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    #nombre_imagen_producto = models.ImageField(verbose_name="Foto_Producto")

    #Retorna primary key que es un int
    def __int__(self):
        return self.nombre_producto

#Falta poder agregar mas de un producto al pedido
#calcular total sumando todos los productos y asignandolos a una variable
class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    #email_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_pedido = models.DateField()
    total = models.IntegerField()
    estado = models.CharField(max_length=15)

    def __int__(self):
        return self.id_pedido