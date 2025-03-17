from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
# Create your views here.

def recepies_view(request):
    if request.method == "POST":

       data = request.POST
       receipe_image = request.FILES.get('receipe_image')
       receipe_name = data.get('receipe_name')
       receipe_description = data.get('receipe_description')
       
       Recipes.objects.create(
        receipe_image = receipe_image,
        receipe_name =receipe_name,
        receipe_description = receipe_description,
       )
       return redirect('/foody/')
    
    querySet = Recipes.objects.all()
    context = {'receipes': querySet}
    
    return render(request, 'website/recepies.html',context)


def update_recepie(request,id):
  querySet = Recipes.objects.get(id = id)
  if request.method == "POST":

       data = request.POST
       receipe_image = request.FILES.get('receipe_image')
       receipe_name = data.get('receipe_name')
       receipe_description = data.get('receipe_description')

       querySet.receipe_name=receipe_name
       querySet.receipe_description=receipe_description
       if receipe_image:
          querySet.receipe_image=receipe_image
      
       querySet.save()
  context = {'receipe': querySet}
  return render(request, 'website/update_recepies.html',context)



def delete_recepie(request,id):
  querySet = Recipes.objects.get(id = id)
  querySet.delete()
  return redirect('/foody/')
