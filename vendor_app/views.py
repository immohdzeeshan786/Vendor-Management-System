from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import viewsets
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer

    def get_queryset(self):
        return Vendor.objects.filter(id=self.kwargs['vendor_id'])

# vendors/urls.py
