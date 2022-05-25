from django import forms

class createPekerjaanForms(forms.Form):
    jumlah = forms.CharField(label='Nama Pekerjaan', max_length=10, widget=forms.TextInput(attrs = {
        'class':'form-control',
        'type':'text',
        'required':True,
        'placeholder':'Masukkan Nama Pekerjaan',        
        'oninvalid' : "alert('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu 😊🙏🏻')",
    }))

class createBaseHonorForms(forms.Form):
    jumlah = forms.CharField(label='Base Honor', max_length=10, widget=forms.TextInput(attrs = {
        'class':'form-control',
        'type':'text',
        'required':True,
        'placeholder':'Masukkan Base Honor',        
        'oninvalid' : "alert('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu 😊🙏🏻')",
    }))