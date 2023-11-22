from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'api/vendors/(?P<vendor_id>\d+)/performance', VendorPerformanceViewSet, basename='vendor-performance')
urlpatterns = router.urls


