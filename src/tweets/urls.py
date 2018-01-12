from django.conf.urls import url
from .views import TweetDetailView, TweetListview, TweetCreateView



urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListview.as_view(), name='list'),
    url(r'^create/$', TweetCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name="detail")

]
