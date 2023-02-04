from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class LaptopForm(forms.Form):
    brand = forms.ChoiceField(label="Brand",choices = (
        ("-Select-", "-Select-"),
        ("Acer", "Acer"),
        ("Apple", "Apple"),
        ("ASUS", "ASUS"),
        ("Compaq", "Compaq"),
        ("Dell", "Dell"),
        ("Gateway", "Gateway"),
        ("HP", "HP"),
        ("Lenovo", "Lenovo"),
        ("Samsung", "Samsung"),
        ("Sony", "Sony"),
        ("Toshiba", "Toshiba"),
        ("Other", "Other")
    ))
    screen_size = forms.ChoiceField(label="Screen Size",choices = (
        ("-Select-", "-Select-"),
        ("14\" and under", "14\" and under"),
        ("15\"", "15\""),
        ("16\"", "16\""),
        ("17\" and over","17\" and over")
    ))
    condition = forms.ChoiceField(label="Condition", choices = (
        ("-Select-", "-Select-"),
        ("Used - Like New", "Used - Like New"),
        ("Used - Good", "Used - Good"),
        ("Used - Fair", "Used - Fair")
    ))
    price = forms.CharField(label="Price (CAD) $")

class DesktopForm(forms.Form):
    brand = forms.ChoiceField(label="Brand",choices = (
        ("-Select-", "-Select-"),
        ("Acer", "Acer"),
        ("Custom", "Custom"),
        ("Apple", "Apple"),
        ("ASUS", "ASUS"),
        ("Compaq", "Compaq"),
        ("Dell", "Dell"),
        ("Gateway", "Gateway"),
        ("HP", "HP"),
        ("IBM", "IBM"),
        ("Intel", "Intel"),
        ("Lenovo", "Lenovo"),
        ("Samsung", "Samsung"),
        ("Sony", "Sony"),
        ("Toshiba", "Toshiba"),
        ("Other", "Other")
    ))
    condition = forms.ChoiceField(label="Condition", choices = (
        ("-Select-", "-Select-"),
        ("Used - Like New", "Used - Like New"),
        ("Used - Good", "Used - Good"),
        ("Used - Fair", "Used - Fair")
    ))
    price = forms.CharField(label="Price (CAD) $")

class CameraForm(forms.Form):
    brand = forms.CharField(label="Brand")
    condition = forms.ChoiceField(label="Condition", choices = (
        ("-Select-", "-Select-"),
        ("Used - Like New", "Used - Like New"),
        ("Used - Good", "Used - Good"),
        ("Used - Fair", "Used - Fair")
    ))
    price = forms.CharField(label="Price (CAD) $")