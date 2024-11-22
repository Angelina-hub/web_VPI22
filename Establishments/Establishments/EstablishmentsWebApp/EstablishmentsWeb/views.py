from django.shortcuts import render,get_object_or_404
from .models import Establishment, Feedback
from django.http import JsonResponse, HttpResponseRedirect
from .form import FeedbackForm
from django.db.models import Avg

def EstablishmentsJson(request):
    establishments = Establishment.objects.all()
    name = request.GET.get('name')
    address = request.GET.get('address')
    establishment_type = request.GET.get('type')

    print(establishment_type)
    if name:
        establishments = establishments.filter(name__icontains=name)
    if address:
        establishments = establishments.filter(address__icontains=address)
    if establishment_type:
        establishments = establishments.filter(establishment_type__icontains=establishment_type)

    sort_by = request.GET.get('sort-by')
    if sort_by in ['name', 'address', ]:
        establishments = establishments.order_by(sort_by)
    
    
    establishments_data = []
    for establishment in establishments:
        feedbacks = Feedback.objects.filter(title__contains= establishment.name)
        avg_rating = feedbacks.aggregate(Avg('rating'))['rating__avg']
        if avg_rating is None:
            avg_rating = 0
        establishments_data.append({
            'id':establishment.id,
            'name': establishment.name,
            'address': establishment.address,
            'city': establishment.city,
            'phone_number': establishment.phone_number,
            'establishment_type': establishment.establishment_type,
            'image': establishment.image.url,
            'avg_rating': round(avg_rating,2)
        })
    return JsonResponse(establishments_data,safe=False)



def Establishments(request):
    establishments = Establishment.objects.all()
    establishment_types = list(establishments.values_list('establishment_type', flat=True).distinct())

    return render(request, "Home.html", {"establishments": establishments, "establishment_types": establishment_types})


def EstablishmentsInformation(request, id_establishment:int):
    establishment = get_object_or_404( Establishment, id = id_establishment)
    print(establishment.address)
    return render(request, "EstablishmentsInformation.html", {"establishment": establishment})


def feedback(request,id_establishment:int):
    establishment = get_object_or_404( Establishment, id = id_establishment)

    establishment_title = establishment.name

    if request.method == 'POST':
        print('POST')
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed=Feedback(
                username=form.cleaned_data['username'],
                title=establishment_title,
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating']
            )
            feed.save()
            return HttpResponseRedirect(f'/establishments/{id_establishment}')
    else:
         form = FeedbackForm(
             initial= {'title': establishment_title}
              )
    return render(request, "feedback.html", {'establishment':establishment, 'form':form})


def feedbacksestablishment(request,id_establishment:int):
    establishment = get_object_or_404( Establishment, id = id_establishment)
    feedbacks= Feedback.objects.filter(title__contains= establishment.name).filter(feedback__contains= "хорошо").order_by('-id')
    return render(request, "ReviewForEstablishment.html", {'feedbacks':feedbacks,'establishment': establishment})