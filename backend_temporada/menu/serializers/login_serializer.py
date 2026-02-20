<<<<<<< HEAD
from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from menu.models import Cliente


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, min_length=5, write_only=True)

    class Meta:
        model = Cliente
        fields = ('email', 'password')

    def validate_password(self, password):
        if not any(n.isdigit() for n in password):
            raise serializers.ValidationError("La contraseña es incorrecta")
        return password

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if "@" not in email:
            raise serializers.ValidationError("Email o contraseña incorrecta")

        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise serializers.ValidationError("Email o contraseña incorrecta")

        cliente = Cliente.objects.filter(email=email, is_active=True).first()

        if not cliente:
            raise serializers.ValidationError("El usuario no existe")

=======
from locale import normalize

from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt import RefreshToken
from menu.models import Cliente

class LoginSerializer(serializers.ModelSerializer):
    email_cliente = serializers.CharField(label='Email Cliente', max_length=100)
    telefono_cliente = serializers.CharField(label='Telefono Cliente', max_length=100)
    password = serializers.CharField(label='Password', max_length=6)

    class Meta:
        model = Cliente
        fields = ('email_cliente', 'password')


    def validate_password(self, password):
         if not any(n.isdigit() for n in password):
             raise serializers.ValidationError("Contraseña incorrecta")
         return password
    def validate_email_cliente(self, attrs):
        email = attrs.get('email_cliente')
        password = attrs.get('password')

        if "@" not in email:
            raise serializers.ValidationError("Formato no valido")
        if any(ext in email for ext in settings.EXTENSIONS_BLACKLIST):
            raise serializers.ValidationError("Email o contraseña incorrecto")

        cliente = Cliente.objects.get(email=email, is_active=True).first()

        if not cliente:
            raise serializers.ValidationError("El cliente no existe")
>>>>>>> bb0040f73d9083ebbe9a81245bdfdcbe2ccf1277
        if not cliente.check_password(password):
            raise serializers.ValidationError("La contraseña no coincide")

        refresh = RefreshToken.for_user(cliente)
        refresh['nombre'] = cliente.nombre

        return {
<<<<<<< HEAD
            'success': True,
            'data': {
                'nombre': cliente.nombre,
                'email': cliente.email,
                'telefono': cliente.telefono,
                'refreshToken': str(refresh),
                'token': str(refresh.access_token)
=======
            'success':True,
            'data':{
                'nombre': cliente.nombre,
                'telefono': cliente.telefono,
                'email': cliente.email,
                'refreshToken': str(refresh),
                'token': str(refresh.access_token),
>>>>>>> bb0040f73d9083ebbe9a81245bdfdcbe2ccf1277
            }
        }