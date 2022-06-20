from django.shortcuts import render
from .forms import TranslateForm
from .models import Translate
# Create your views here.
def translation_detail_view(request):
    obj = Translate.objects.get(id=1)
    # context = {                   this was the first way of doing things which was not as efficient
    #     "english": obj.english,
    #     "italian": obj.italian,
    #     "german": obj.german,
    #     "french": obj.french
    # }
    context = {
        'object': obj
    }

    return render(request, "translate/detail.html", context)


def translation_create_view(request):
    form = TranslateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TranslateForm()

    context = {
        'form': form
    }

    return render(request, "translate/create.html", context)