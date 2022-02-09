#I have created this file-Anshuman
from django.http import HttpResponse 
def index(request):
    return HttpResponse('''<a href="https://www.hackerrank.com/orion_anshuman"> Hacker rank</a>''')
    

def about(request):
    return HttpResponse("About Anshuman Singh")