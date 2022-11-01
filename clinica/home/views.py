from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from profesional.models import Profesional


def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )


def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(last_name__contains=search_param), Q.OR)
        profesionales = Profesional.objects.filter(query)
        context_dict.update(
            {
                "profesionales": profesionales,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )

