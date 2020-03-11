from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.user import User
from api.serializers.userserializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

user_info = {
    'id': 1,
    'login': 'example',
    'mail': 'mail@example.com',
    'birth_date': '2020-01-01',
    'sport_list': [
        {
            'sport_id': 1,
            'sport_proficiency': 2,
        },
        {
            'sport_id': 2,
            'sport_proficiency': 1
        }
    ],
    'gender': 'F',
    'phone_number': '+48111111111',
    'description': 'I like dogs',
}

basic_info = {
	'id': 1,
	'login': 'Ja7000',
    'sport_list': [
        {
            'sport_id': 1,
            'sport_proficiency': 2,
        },
        {
            'sport_id': 2,
            'sport_proficiency': 1
        }
    ],
    'gender': 'F',
	'description': 'Oto ja',
	'phone_number': '+48123456789',
	'age': 33,
}


class MockUserViewset(viewsets.ViewSet):
    """
    API endpoint that allows users to update their info.
    """

    def retrieve(self, request, pk=None):
        return Response(basic_info)

    @action(methods=['get', 'put', 'patch'], detail=False)
    def me(self, request):
        return Response(user_info)
