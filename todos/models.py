from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False, verbose_name="Título da Tarefa",)
    dtCriacao = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Data de criação",)
    dtFinalizado = models.DateTimeField(null=True, blank=True, verbose_name="Data de Finalização",) 