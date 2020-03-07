from rest_framework import viewsets
from rest_framework.response import Response


participation_request = {
    'id': 1,
    'workout': 1,
    'user': {
        'id': 1,
        'login': 'user97',
    },
    'message': 'bardzo chcialbym biegac tak jak wy'
}


class MockParticipationRequestViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to request participation in a workout.
    """

    def list(self, request):
        return Response([participation_request])

    def create(self, request):
        return Response(participation_request)

    def partial_update(self, request, pk=None):
        accepted_request = dict(participation_request)
        accepted_request['accepted'] = True
        return Response(accepted_request)