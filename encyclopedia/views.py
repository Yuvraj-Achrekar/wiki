from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from markdown import markdown 
from django.urls import reverse

from . import util


def index(request):
    if request.method == 'POST':
        form = request.POST.get('q')
        if form:
            data = util.get_entry(form)
            if data:
                return HttpResponseRedirect(reverse("wiki:entry",args=[form]),{"name": form,"content":markdown(data)})
            entries = util.list_entries()
            
        return render(request,"encyclopedia/error.html")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request,name):
    content = util.get_entry(name)
    if content:
        return render(request,"encyclopedia/entry.html",{
            "name": name,
            "content":markdown(content)
        })
    else:
        return render(request,"encyclopedia/error.html")