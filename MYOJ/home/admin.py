from django.contrib import admin
from home.models import problem, Solution, TestCase

admin.site.register(problem)
admin.site.register(Solution)
admin.site.register(TestCase)