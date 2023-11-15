from rest_framework import routers
from .views import UserViewSet, WasteCollectorViewSet 
from .views import UserViewSet, WasteCollectorViewSet, WasteRecyclerViewSet
router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("register-wastecollector", WasteCollectorViewSet, basename="register-wastecollector")
router.register("register-wasterecycler", WasteRecyclerViewSet, basename="register-wasterecycler")
urlpatterns = router.urls
