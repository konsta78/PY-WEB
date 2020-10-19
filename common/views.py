from datetime import datetime

from django.views import View
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')