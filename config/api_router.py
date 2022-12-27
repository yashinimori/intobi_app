from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from intobi_app.core.api.views import CurrentMenuView, MenuViewSet, RestaurantViewSet
from intobi_app.users.api.views import UserViewSet
from intobi_app.vote.api.views import VoteViewSet, VotingView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet)
router.register("vote", VotingView)
router.register("votes", VoteViewSet)
router.register("current_menu", CurrentMenuView)


app_name = "api"
urlpatterns = router.urls
