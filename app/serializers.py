from django.contrib.auth.models import User # 회원가입
from django.contrib.auth.password_validation import validate_password # 회원가입
from django.contrib.auth import authenticate # 로그인

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

# 회원가입 기능

class RegisterSerializer(serializers.ModelSerializer) :
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
    )

    password2 = serializers.CharField(write_only = True, required = True)

    class Meta :
        model = User
        fields = ('username', 'password', 'password2', 'email')
    
    def validate(self, data) :
        if data['password'] != data['password2'] :
            raise serializers.ValidationError(
                {"password": "비밀번호가 맞지 않습니다. 다시 입력해주세요."}
            )
        return data

    def create(self, validated_data) :
    # CREATE 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성한다.
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    

# 로그인의 경우 모델과 관련이 없다. 사용자가 ID/PW를 보냈을 때, 그에 해당하는 토큰으로만 응답하면 되기 때문

class LoginSerializer(serializers.Serializer) :
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)

    # write_only 옵션을 통해 클라이언트 -> 서버 방향의 역직렬화 가능, 서버 -> 클라이언트 방향의 직렬화는 불가능

    def validate(self, data):
        user = authenticate(**data)
        if user :
            token = Token.objects.get(user = user)
            return token
        raise serializers.ValidationError(
            {"error" : "아이디 혹은 패스워드가 틀립니다."}
        )