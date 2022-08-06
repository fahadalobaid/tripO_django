from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from .serializers import UserCreateSerializer , UserLoginSerializer ,ListSerializer,TripsDetailSerializer,CreateTripSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .models import Trip
from django.http import HttpResponse
from rest_framework import generics

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    # def get_serializer_class(self):
    #     # print(self.request.data)
    #     return UserCreateSerializer





class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


# def get_Trip(request,trip_id):
#     trip = Trip.objects.get(id=trip_id)
#     return HttpResponse(trip)

# def get_trip_list(request) :
#     Trips = Trip.objects.all().values_list( flat=True)
#     Trips_list = "\n".join(f"<li>{Trip}</li>" for Trip in Trips)
#     return HttpResponse({Trips_list})

class TripListApiView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = ListSerializer


class DetailView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripsDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class CreateTripView(CreateAPIView):
    serializer_class = CreateTripSerializer


