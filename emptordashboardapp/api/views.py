from rest_framework import generics
from emptordashboardapp.models import Country

class EmptorDashboard(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field = 'pk'
    # querySet     = Country.objects.all()

    def get_queryset(self):
        return Country.objects.all()