from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .form import HomeForm

from .models import ProductBacklog
from .models import ProductBacklogItem
from .models import SprintBacklog
from .models import Task

from sprints.models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    products = ''
    productBacklogItems = ''
    sprintBacklogs = ''
    tasks = ''
    def get(self, request):
        form = HomeForm()
        self.products = ProductBacklog.objects.values()
        self.productBacklogItems = ProductBacklogItem.objects.values()
        return render(request,'index.html', {
            "products":self.products, \
            "productBacklogItems": self.productBacklogItems, \
            "form": form})
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            pb = ProductBacklog.objects.all().filter(id=1)
            post.pb_id = pb[0]
            post.save()
        response = redirect('/productbg')
        return response
        
def modifyPBI(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    size = request.POST.get('size')
    status = request.POST.get('status')
    _id = request.POST.get('id')
    ProductBacklogItem.objects.filter(id = _id).update(title = title, \
    description = description, \
    size = size, \
    status = status, \
    )
    return JsonResponse({"success": "true"})

def deletePBI(request):
    _id = request.POST.get('id')
    ProductBacklogItem.objects.filter(id=_id).delete()
    return JsonResponse({"success": "true"})


def refinePBI(request):
    _id = request.POST.get('id')
    # ProductBacklogItem.objects.filter(id=_id).delete()

    pbis = request.POST.get('pbi_list')
    return JsonResponse({"success": "true"})



