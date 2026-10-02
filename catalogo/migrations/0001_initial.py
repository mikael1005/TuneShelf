from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Musica",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("titulo", models.CharField(max_length=120)),
                ("artista", models.CharField(max_length=120)),
                ("album", models.CharField(blank=True, max_length=120)),
                ("descricao", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OUVIDA", "Ouvida"),
                            ("QUERO_OUVIR", "Quero ouvir"),
                            ("OUVINDO", "Estou ouvindo"),
                        ],
                        default="QUERO_OUVIR",
                        max_length=20,
                    ),
                ),
                ("nota", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("data_adicao", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="musicas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-data_adicao"]},
        ),
    ]
