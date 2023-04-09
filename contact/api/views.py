from rest_framework import generics
from .serializer import ContactSerializer
from ..models import Contact


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
