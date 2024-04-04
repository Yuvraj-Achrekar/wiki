from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from markdown import markdown 
from django.urls import reverse
from django import forms

from . import util


class NewForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content",widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

def index(request):
    entries = util.list_entries()
    if request.method == 'POST':
        form = request.POST.get('q')
        if form:
            data = util.get_entry(form)
            if data:
                return HttpResponseRedirect(reverse("wiki:entry",args=[form]),{"name": form,"content":markdown(data)})
            return HttpResponseRedirect(reverse("wiki:search",args=[form]))
        return render(request,"encyclopedia/error.html")

    return render(request, "encyclopedia/index.html", {
        "entries": entries
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
    
def search(request,query):
    entries = util.list_entries()
    search_results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request,"encyclopedia/search.html",{
            "query":query,
            "search_results":search_results
        })

def create(request):
    if request.method == 'POST':
        form = NewForm(request.Post)
        return HttpResponse("post method")
    return render(request,"encyclopedia/create.html",{
        "form": NewForm()
    })