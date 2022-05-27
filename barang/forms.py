from django import forms


class PemainCreateMenggunakanBarang(forms.Form) :
    nama_tokoh = forms.ChoiceField(widget=forms.Select(attrs={'id': 'nama_tokoh'}))
    barang = forms.ChoiceField(widget=forms.Select(attrs={'id': 'barang'}))