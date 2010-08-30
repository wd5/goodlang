from django.core.management.base import BaseCommand
from settings import rel
from os import path
import os
from BeautifulSoup import BeautifulStoneSoup
from courses.models import Course, Lesson, Word

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        lessons_path = rel('lessons')
        course = Course.objects.get(pk=1)
        
        for file_name in os.listdir(lessons_path):
            f = open(path.join(lessons_path, file_name))
            soup = BeautifulStoneSoup(f.read())
            lesson_num = file_name.split('.')[0]
            lesson, created = Lesson.objects.get_or_create(number=lesson_num, cource=course)
            
            for item in soup.contents[2].findAll('word'):
                Word.objects.get_or_create(lesson=lesson, word=item['spell'], translation=item['translation'])
                
            f.close()
        