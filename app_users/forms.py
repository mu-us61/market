from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _("Lütfen kullanıcı adınızı ve şifrenizi doğru girdiğinizden emin olun."),
        "inactive": _("Bu hesap şu anda aktif değil."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Kullanıcı Adı"
        self.fields["password"].label = "Şifre"


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="E-posta",
        help_text="Lütfen geçerli bir e-posta adresi girin.",
        error_messages={
            "required": "E-posta alanı zorunludur.",
            "invalid": "Lütfen geçerli bir e-posta adresi girin.",
        },
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Kullanıcı Adı"
        self.fields["password1"].label = "Şifre"
        self.fields["password2"].label = "Şifre (Tekrar)"
        # Customize help text for username
        self.fields["username"].help_text = (
            "Gerekli. 150 karakter veya daha az. Sadece harfler, rakamlar ve @/./+/-/_ kullanılabilir."
        )
        # Customize error messages for username
        self.fields["username"].error_messages.update(
            {
                "required": "Kullanıcı adı zorunludur.",
                "unique": "Bu kullanıcı adı zaten kullanılıyor.",
                "invalid": "Geçersiz karakterler içeriyor.",
            }
        )
        # Customize help text for password1
        self.fields["password1"].help_text = mark_safe(
            "<ul>"
            "<li>Şifreniz kişisel bilgilerinizle çok benzer olamaz.</li>"
            "<li>Şifreniz en az 8 karakter içermelidir.</li>"
            "<li>Şifreniz yaygın olarak kullanılan bir şifre olamaz.</li>"
            "<li>Şifreniz tamamen sayısal olamaz.</li>"
            "</ul>"
        )
        # Customize error messages for password1
        self.fields["password1"].error_messages.update(
            {
                "required": "Şifre zorunludur.",
            }
        )
        # Customize help text for password2
        self.fields["password2"].help_text = "Doğrulama için aynı şifreyi tekrar girin."

        # Customize error messages for password2
        self.fields["password2"].error_messages.update(
            {
                "required": "Şifre doğrulaması zorunludur.",
                "password_mismatch": "Şifreler eşleşmiyor.",
            }
        )
