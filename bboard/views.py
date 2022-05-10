from django.shortcuts import render
from .models import Bb


def base(request):
    if request.POST:
        data_elements = []
        key = request.POST.get('field')
        value = request.POST.get('value').lower()
        for k in Bb.objects.all():
            if value in str(k.__getattribute__(key)).lower():
                data_elements.append(k)
        context = {'bb': data_elements}
    else:
        context = {'bb': Bb.objects.all().values('title', 'description', 'price', 'kind')}
    fields = {}
    for i in Bb._meta.fields:
        if i.name not in ('id', 'published'):
            fields[i.name] = i.verbose_name
    context['fields'] = zip(fields.keys(), fields.values())

    return render(request, 'bboard/base.html', context=context)
