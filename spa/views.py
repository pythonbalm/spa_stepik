from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import HouseForm
from .models import Photo, House
from django.forms.formsets import formset_factory



def home(request):
    return render(request, 'spa/home.html')


def post(request):
    return render(request, 'spa/post.html')


def contacts(request):
    return render(request, 'spa/contacts.html')


def thanks(request):
    return render(request, 'spa/thanks.html')


# def new_house(request):
#     if request.method == 'POST':
#         form = HouseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = HouseForm()
#
#     return render(request, "spa/form-1.html", {'form': form})



# def formset_view(request):
#     context = {}
#     ImageFormSet = inlineformset_factory(House, Photo, fields=('house', 'photo'))
#     house = House.objects.get(pk=1)
#     # Add the formset to context dictionary
#     context['formset'] = ImageFormSet(instance=house)
#     return render(request, "spa/form-1.html", context)


def formset_view(request):
    house = House.objects.get(pk=1)
    HouseInlineFormSet = inlineformset_factory(House, Photo, fields=('photo',))
    if request.method == "POST":
        formset = HouseInlineFormSet(request.POST, request.FILES, instance=house)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(house.get_absolute_url())
    else:
        formset = HouseInlineFormSet(instance=house)
    return render(request, 'spa/form-1.html', {'formset': formset})


class ViewHouse(DetailView):
    model = House
    context_object_name = 'house_item'
    # template_name = 'news/news_detail.html'
    # pk_url_kwarg = 'news_id'


def signup(request):
    return render(request, 'spa/signup.html')


def signin(request):
    return render(request, 'spa/signin.html')


def search(request):
    return render(request, 'spa/search.html')