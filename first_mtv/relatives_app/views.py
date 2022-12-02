from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.template import loader 
from relatives_app.models import Family


def save_relative(request: HttpRequest) -> HttpResponse:

    relative_mother=Family(firstname="Susana", lastname="Bourband", age="60", birthday="1962-6-5")
    relative_sister=Family(firstname="Sheila", lastname="Schurmann", age="33", birthday="1989-10-19")
    relative_grandmother=Family(firstname="Juana", lastname="Suarez", age="78", birthday="1942-1-24") 
    
    relative_mother.save()
    relative_sister.save()
    relative_grandmother.save()

    templates=loader.get_template("index.html")
    
    context = {
        "relatives": [relative_mother, relative_sister, relative_grandmother]
        }

    document=templates.render(context)
    return HttpResponse(document)