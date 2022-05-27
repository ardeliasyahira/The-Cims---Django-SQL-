from django import forms

class createPekerjaanForms(forms.Form):
    nama_pekerjaan = forms.CharField(label='Nama Pekerjaan', max_length=10, widget=forms.TextInput(attrs = {
        'class':'form-control',
        'type':'text',
        'required':True,
        'placeholder':'Masukkan Nama Pekerjaan',        
        'oninvalid' : "alert('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu 😊🙏🏻')",
    }))
    base_honor = forms.CharField(label='Base Honor', max_length=10, widget=forms.TextInput(attrs = {
        'class':'form-control',
        'type':'text',
        'required':True,
        'placeholder':'Masukkan Base Honor',        
        'oninvalid' : "alert('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu 😊🙏🏻')",
    }))

class updatePekerjaanForms(forms.Form):
    nama_pekerjaan= forms.CharField(label='Nama Pekerjaan', max_length=50, disabled=True)
    base_honor = forms.CharField(label='Base Honor', max_length=10, widget=forms.TextInput(attrs = {
        'class':'form-control',
        'type':'text',
        'required':True,
        'placeholder':'Masukkan Base Honor',        
        'oninvalid' : "alert('Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu 😊🙏🏻')",
    }))