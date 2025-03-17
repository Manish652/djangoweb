from django.http import HttpResponse
from django.shortcuts import render



# def home(request):
#         return HttpResponse("Hey i am a Django server")

def home(request):

        peoples = [
                {'name': 'Manish Bhunia', 'age': 20},
                {'name': 'rohan sharma', 'age': 23},
                {'name': 'pallab Das', 'age':9},
                {'name': 'sayan maity', 'age':12}
        ]

        text = """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem consectetur, doloremque dicta neque perspiciatis voluptatibus magnam, enim totam aut corrupti facilis earum a dolorem nostrum, temporibus laudantium eligendi ea natus? 
               """

        vegetables=[]
        
        return render(request,'website/index.html', context={'peoples':peoples,'text':text})
def about(request):
        return render(request,'website/about.html')

def help(request):
        return render(request,'website/help.html')
def contact(request):
        return render(request,'website/contact.html')

def services(request):
        return render(request,'website/services.html')



def success_page(request):
        
        return HttpResponse("<h1>hi this isa success page </h1>")