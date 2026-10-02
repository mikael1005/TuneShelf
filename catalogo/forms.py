from django import forms
from .models import Musica


class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ["titulo", "artista", "album", "descricao", "status", "nota"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ex.: Blinding Lights"}),
            "artista": forms.TextInput(attrs={"placeholder": "Ex.: The Weeknd"}),
            "album": forms.TextInput(attrs={"placeholder": "Nome do álbum"}),
            "descricao": forms.Textarea(
                attrs={"placeholder": "Escreva um comentário sobre esta música...", "rows": 4}
            ),
            "status": forms.Select(),
            "nota": forms.NumberInput(attrs={"min": 1, "max": 5, "placeholder": "1 a 5"}),
        }

    def clean_nota(self):
        nota = self.cleaned_data.get("nota")
        if nota is not None and not 1 <= nota <= 5:
            raise forms.ValidationError("A nota deve estar entre 1 e 5.")
        return nota
