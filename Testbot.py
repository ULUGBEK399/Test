from django.contrib import admin

# Register your models here.
from course.models import Course
from course.models import Subject

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

admin.site.register(Course,CourseAdmin)
admin.site.register(Subject)
import telebot

bot = telebot.TeleBot('7743791918:AAFVNhBM4ZWVB1QLg4_IEgPNPO4RCcSJMuE')
@bot.message_handler(commnds=['start', 'hello', 'main'])
def main(message):

