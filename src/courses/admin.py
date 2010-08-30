from django.contrib import admin
from courses.models import Course, Lesson, Word

admin.site.register([Course, Lesson, Word])