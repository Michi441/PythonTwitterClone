from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.forms.utils import ErrorList
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin

class TweetCreateView(FormUserNeededMixin, CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweet/create"



    #fields = ['user', 'content']

class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)

class TweetListview(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListview, self).get_context_data(*args, **kwargs)

        return context

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    print (obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    print (queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)

# Create your views here.
