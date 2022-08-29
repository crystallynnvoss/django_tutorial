from django.urls import path #path is a function
from . import views #views module so we can reference views function

#URLConfig
urlpatterns = [ #variable that gets set to an array of url pattern objects
  # path("playg/", views.say_hello) #use path function to return URL pattern object; takes 2 parameters, 
  # one is route(url) the onter is reference to view function, from views module, we ask for function
  # but we can delete the playg because we already refernced it in urls.py in project folder so becomes:
  path("hello/", views.say_hello)
]