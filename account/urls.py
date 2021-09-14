from django.urls import path
from .views import UserAPIView, BookmarkListView, UserView, BookmarkAPIView, BookmarkDeleteView, PayUrl, CheckPay

app_name = "account"

urlpatterns = [
    path("bookmark/", BookmarkAPIView.as_view(), name="create_bookmark"),
    path("bookmark/delete/<int:mark_id>/", BookmarkDeleteView.as_view(), name="delete_bookmark"),
    path("bookmarks/", BookmarkListView.as_view(), name="bookmarks_list"),
    path("user/", UserAPIView.as_view(), name="create_user"),
    path("me/", UserView.as_view(), name="user_info"),
    path("pay/url/", PayUrl.as_view(), name="get_pay_url"),
    path("pay/check/", CheckPay.as_view(), name="get_pay_url"),
]
