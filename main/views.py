from rest_framework.response import Response
from rest_framework import generics
from .serializer import purchaseserializer
from .models import purchase

class purchaseData(generics.CreateAPIView):
    serializer_class = purchaseserializer
    queryset = purchase.objects.all()


class RetreiveVoucher(generics.GenericAPIView):
    serializer_class = purchaseserializer
    queryset = purchase.objects.all()

    def get(self, request, ref_code):
        voucher = purchase.objects.filter(ref_code = ref_code).first()
        if voucher is None:
            return Response(data= "Voucher not found", status=400)
        else:
            serializer = self.serializer_class(voucher)
            return Response(data= serializer.data, status=200)

class UpdateVoucher(generics.GenericAPIView):
    serializer_class = purchaseserializer
    queryset = purchase.objects.all()

    def put(self, request, ref_code):
        print(request.data)
        voucher = purchase.objects.filter(ref_code = ref_code).first()

        if voucher is None:
            return Response(data= "Voucher not found", status=400)
        else:
                
            serializer = self.serializer_class(instance = voucher, data = request.data,  partial = True)
            
            if serializer.is_valid():
                return Response(data= serializer.data, status=200)
            else:
                return Response(data= serializer.errors, status=400)





