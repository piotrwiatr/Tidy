from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class LaptopForm(forms.Form):
    laptop_brand = forms.ChoiceField(label="Brand",choices = (
        ("1", "-Select-"),
        ("2", "Acer"),
        ("3", "Apple"),
        ("4", "ASUS"),
        ("5", "Compaq"),
        ("6", "Dell"),
        ("7", "Gateway"),
        ("8", "HP"),
        ("9", "Lenovo"),
        ("10", "Samsung"),
        ("11", "Sony"),
        ("12", "Toshiba"),
        ("13", "Other")
    ))
    laptop_screen_size = forms.ChoiceField(label="Screen Size",choices = (
        ("1", "-Select-"),
        ("2", "14\" and under"),
        ("3", "15\""),
        ("4", "16\""),
        ("5","17\" and over")
    ))
    laptop_condition = forms.ChoiceField(label="Condition", choices = (
        ("1", "-Select-"),
        ("2", "Used - Like New"),
        ("3", "Used - Good"),
        ("4", "Used - Fair")
    ))
    laptop_price = forms.CharField(label="Price")

class DesktopForm(forms.Form):
    desktop_brand = forms.ChoiceField(label="Brand",choices = (
        ("1", "-Select-"),
        ("2", "Custom"),
        ("3", "Acer"),
        ("4", "Apple"),
        ("5", "ASUS"),
        ("6", "Compaq"),
        ("7", "Dell"),
        ("8", "Gateway"),
        ("9", "HP"),
        ("10", "IBM"),
        ("11", "Intel"),
        ("12", "Lenovo"),
        ("13", "Samsung"),
        ("14", "Sony"),
        ("15", "Toshiba"),
        ("16", "Other")
    ))
    desktop_condition = forms.ChoiceField(label="Condition", choices = (
        ("1", "-Select-"),
        ("2", "Used - Like New"),
        ("3", "Used - Good"),
        ("4", "Used - Fair")
    ))
    desktop_price = forms.CharField(label="Price")

class CameraForm(forms.Form):
    camera_brand = forms.CharField(label="Brand")
    camera_condition = forms.ChoiceField(label="Condition", choices = (
        ("1", "-Select-"),
        ("2", "Used - Like New"),
        ("3", "Used - Good"),
        ("4", "Used - Fair")
    ))
    camera_price = forms.CharField(label="Price")