from django.shortcuts import render
from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseRedirect)

from django.urls import reverse
from django.shortcuts import render

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


    html = ""

    for post in posts:
        html += f"""
                <div>
                <a href="/posts/{post["id"]}/"    
                    <h1>{post["id"]} - {post["title"]}</h1></a>
                    <p>{post["content"]}</p>
                </div>
"""
    name = "Jeff Bezos"
    # the render function will find specific html file we appoint in templates folder for individual application
    # send different context in the same template -> generating html dynamically  
    return render(request= request, 
                  template_name= "home.html", 
                  context= {"name": name, "list": ["Carrot"]})# remember using dictionary (key-value pair) to render different context dynamically


def post(request, 
         id: int):
    """
    Django regard value of Path Variable in URL as String
    """
    print(type(id))


    # Space Complexity O(n)
    post_dict = dict()
    is_valid = False
    for post in posts:
        if post["id"] == id:
            post_dict = post
            is_valid = True
            break
    
    if (is_valid):
        html = f"""
            <h1>{post_dict["title"]}</h1>
            <p>{post_dict["content"]}</p>
    """
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Post Not Available 😀")
    

def google(request, id):
    # track and get the whole url even the name of root url was changed
    url = reverse("post", args= [id])
    print(url)
    return HttpResponseRedirect(url)