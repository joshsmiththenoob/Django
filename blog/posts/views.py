from django.shortcuts import render
from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         Http404)

from django.urls import reverse
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Let\'s explore Python",
        "content": "Python is interpreted, highg level, general purpose programming language. Widely used in the fields of web development, data science and machine learning."
    },
    {
        "id": 2,
        "title": "Let\'s explore Javascript",
        "content": "Javascript is intepreted, high level, general purpose programming language. Widely used in the fields of web development."
    },
    {
        "id": 3,
        "title": "Django the best web framework",
        "content": "Django is used by almost every big tech company like Facebook, Google, Youtube, Instagram etc."
    }
]



def home(request):
    # print(name)
    print(reverse("home"))

    results = Post.objects.all()

    # the render function will find specific html file we appoint in templates folder for individual application
    # send different context in the same template -> generating html dynamically  
    return render(request= request, 
                  template_name= "posts/index.html",
                  context= {"posts": results}
                  )# remember using dictionary (key-value pair) to render different context dynamically


def post(request, 
         id: int):
    """
    Django regard value of Path Variable in URL as String
    """
    print(type(id))
    
    result = get_object_or_404(Post, id= id)

    return render(request = request,
                    template_name = "posts/post.html",
                    context = {"post_dict": result}
                    )

    ## the get_object_or_404 shortcut's function is as same as the try, except if we want to get specific record like beloe example 
    # try:
    #     result = Post.objects.get(id= id)
    #     return render(request = request,
    #                   template_name = "posts/post.html",
    #                   context = {"post_dict": result}
    #                   )
    # except:
    #     # return HttpResponseNotFound("<h1>Post Not Available 😀</h1>")
    #     raise Http404() # Raise Http 404: Django will show 404 page
    
