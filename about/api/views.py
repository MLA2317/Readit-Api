from rest_framework import generics, permissions
from .serializer import FeedbackSerializer
from ..models import Feedback
from .permissions import IsAdminUserOrReadOnly


class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUserOrReadOnly]