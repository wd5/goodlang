from django.db import models
from django.conf.global_settings import LANGUAGES

class Course(models.Model):
    lang = models.CharField(max_length=12, choices=LANGUAGES)
    from_lang = models.CharField(max_length=12, choices=LANGUAGES, default='ru')
    description = models.TextField(blank=True)
    
class Lesson(models.Model):
    cource = models.ForeignKey(Course, related_name='lessons')
    number = models.IntegerField(editable=False)
    
    class Meta:
        ordering = ['number']
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.number:
            try:
                self.number = Lesson.objects.filter(cource=self.cource)[:1] \
                    .get().number+1
            except Lesson.DoesNotExist:
                self.number = 1
        super(Lesson, self).save(*args, **kwargs)
        
class Word(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='words')
    word = models.CharField(max_length=255)     #english word
    sound = models.FileField(upload_to='sounds/', blank=True, null=True)
    translation = models.CharField(max_length=255)      #russian for test
    description = models.TextField(blank=True)  #translation from google translator
    
    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.translation
        super(Word, self).save(*args, **kwargs)    