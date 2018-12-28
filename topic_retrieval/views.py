from django.shortcuts import render
from django.views import generic
from .models import Topic
import datetime
from django.http import JsonResponse
from django.core import serializers
 

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'topic_retrieval/index.html'
    context_object_name = 'latest_topic_list'

    
      
        
    def get_queryset(self):
        """Return the last five published questions."""
        return Topic.objects.filter(first_tweet = '1').order_by('-datetime')[:2]


class SearchView(generic.ListView):

    template_name = 'topic_retrieval/search.html'
    context_object_name = 'searched_topic_list'
    
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        self.request.session['start_date'] = start_date if start_date else datetime.date.today().strftime("%Y-%m-%d")
        self.request.session['end_date'] = end_date if end_date else datetime.date.today().strftime("%Y-%m-%d")

        context['start_date'] = self.request.session['start_date']
        context['end_date'] = self.request.session['end_date']

        
        return context

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        return Topic.objects.filter(datetime__date__range=(start_date,end_date))
    
class TweetsView(generic.ListView):
    template_name = 'topic_retrieval/tweets.html'
    context_object_name = 'relevant_tweet_list'

    def get_context_data(self, **kwargs):

        context = super(TweetsView, self).get_context_data(**kwargs)
        m_topic_id = self.request.GET.get('topic_id')
        context['topic'] = Topic.objects.filter(topic_id = m_topic_id).filter(first_tweet = 1)
        context['start_date'] = self.request.session['start_date']
        context['end_date'] = self.request.session['end_date']
        return context

        
    def get_queryset(self):
        m_topic_id = self.request.GET.get('topic_id')
        # topic_id = self.request.GET.get('topic_id')
        return Topic.objects.filter(topic_id = m_topic_id).order_by('-datetime')
    


# def search(request):
#     start_date = request.POST.get('start_date')
#     end_date = request.POST.get('end_date')
    
#     return 
    

def update_latest_tweets(request):
    data = serializers.serialize("json", Topic.objects.filter(first_tweet='1').order_by('-datetime')[:10])
    
    return JsonResponse(data, safe=False)