from django.urls import path
from home.views import ProblemDisplay, problem_detail
from compiler.views import submit
urlpatterns = [
    path("", ProblemDisplay, name='ProblemDisplay'),
    path('<int:pk>/', problem_detail, name='problem_detail'),
    path("", submit, name='submit'),
   

]