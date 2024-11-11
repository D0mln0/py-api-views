from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaViewSet,
    MovieViewSet
)


cinema_hall_list = CinemaViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genre/", GenreList.as_view(), name="movie-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="movie-detail"),

    path("actor/", ActorList.as_view(), name="movie-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="movie-detail"),

    path("hall/", cinema_hall_list, name="cinema-list"),
    path("hall/<int:pk>/", cinema_hall_detail, name="cinema-detail"),

    path("", include(router.urls))
]

app_name = "cinema"
