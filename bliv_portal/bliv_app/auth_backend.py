from django.contrib.auth.backends import BaseBackend
from .models import leitor

class LeitorBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Autentica pelo campo reference_Id (ou username)
            user = leitor.objects.get(reference_Id=username)
            if user.check_password(password):  # Verifica a senha
                return user
        except leitor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return leitor.objects.get(pk=user_id)
        except leitor.DoesNotExist:
            return None