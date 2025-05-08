from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator,
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
)
from django.core.exceptions import ValidationError


# Custom UserAttributeSimilarityValidator
class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return "Şifre, kullanıcı adınızla çok benzer olamaz."

    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError as e:
            raise ValidationError("Şifre, kullanıcı adınızla çok benzer olamaz.")


# Custom MinimumLengthValidator
class CustomMinimumLengthValidator(MinimumLengthValidator):
    def get_help_text(self):
        return f"Şifreniz çok kısa. En az {self.min_length} karakter içermelidir."

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(f"Şifreniz çok kısa. En az {self.min_length} karakter içermelidir.")


# Custom CommonPasswordValidator
class CustomCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return "Bu şifre çok yaygın olarak kullanılıyor."

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError("Bu şifre çok yaygın olarak kullanılıyor.")


# Custom NumericPasswordValidator
class CustomNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return "Şifreniz tamamen sayısal olamaz."

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError("Şifreniz tamamen sayısal olamaz.")
