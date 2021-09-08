from django import forms

class InquiryForm(forms.Form):
    name = forms.ChaField(label='お名前', max_lemgth=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.ChaField(label='タイトル', max_lemgth=30)
    message = forms.ChaField(label='メッセージ', widget=forms.Texterea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)