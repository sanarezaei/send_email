from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail

from .serializers import ContactSerializers

class ContactAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            send_mail(
                subject=f"پیام از {['name']}",
                message=data['message'],
                from_email=data['email'],
                recipient_list=['sanare1382@gmail.com'],
                fail_silently=False,
            )
            return Response({"message": "پیام شما با موفقیت ارسال شد"},\
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
