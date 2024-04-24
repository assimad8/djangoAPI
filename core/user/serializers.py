from rest_framework import serializers
from core.user.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id',read_only=True,format='hex')
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'firstName','lastName', 'birthday', 'gender', 'avatar', 'bio', 'is_active','phone_number', 'password', 'password2', 'updated','created']
        read_only_fields = ['is_active']


    def validate(self, data):
        if self.context['request'].method == 'POST':
            if data['password'] != data['password2']:
                raise serializers.ValidationError("The passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from the validated data
        return User.objects.create_user(**validated_data)
