from django.shortcuts import render

# Create your views here.

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    return render(request, 'thanks.html', context)
  context = {
    'results': [
      {'name': 'Arnel Robbin', 'email': 'arnel.robin@gmail.com', 'status': 'submitted'},
      {'name': 'Rodriguez Sam Neiol', 'email': 'rodriguze@gmail.com', 'status': 'submitted'},
      {'name': 'Mari Gotze', 'email': 'mario.gotze23@gmail.com', 'status': 'submitted'},
      {'name': 'Omar Yussuf', 'email': 'omar.ysuf12@yahoo.com', 'status': 'submitted'}
    ]
  }
  return render(request, 'index.html', context)
