from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# 현재 views는 기본 예시

# --> FBV : Function Based View = 함수 기반 뷰
@api_view(['GET']) # Decorator -> 함수를 꾸미는 역할(함수에 대한 성격을 표시해주는 표기법)
def HelloAPI(request) :
    return Response("hello world!")

# --> CBV : Class Based View = 클래스 기반 뷰
# class HelloAPI(APIView) :
#     def get(self, request) :
#         return Response("hello wolrd")