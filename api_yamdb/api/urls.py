from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoriesViewSet, CommentViewSet, GenreViewSet, GetToken,
                    ReviewViewSet, SignUp, TitleViewSet, UserViewSet)

router = DefaultRouter()
router.register('categories', CategoriesViewSet,
                basename='category')
router.register('genres', GenreViewSet,
                basename='genres')
router.register('users', UserViewSet,
                basename='users')
router.register('titles', TitleViewSet,
                basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename="reviews")
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUp.as_view(), name='register'),
    path('v1/auth/token/', GetToken.as_view(), name='token')
]
