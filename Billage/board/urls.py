from django.urls import path, include
from .views import Board_commentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('board_comments', Board_commentsViewSet)

board_comments_list = Board_commentsViewSet.as_view({
    'get':'list',
    'post':'create'
})

board_comments_detail = Board_commentsViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destory'
})

urlpatterns = [
    path('', include(router.urls)),
    path('board_comments/', board_comments_list),
    path('board_comments/<int:pk>/', board_comments_detail),
    #path('<int:id>/comment/<int:comment_id>/', views.comments_create, name='comments_create'),
    #path('<int:board_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]