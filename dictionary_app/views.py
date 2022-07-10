from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def find_world(request):
    context = {}

    if word_to_find := request.GET.get('word'):
        response = requests.get('https://regionwielkopolska.pl/kultura-ludowa/gwara/podreczny-slownik-gwary-poznanskiej/')

        list_of_words = response.text[response.text.find('blubry.mp3<br />'):response.text.find('<p>Symbolicznym słowem gwary poznańskiej')].split('<br />')
        gwary = {}

        for item in list_of_words:
            if '-' in item:
                gwara, word = item.split(' - ')
            elif '–' in item:
                gwara, word = item.split(' – ')
            else:
                continue

            if 'strong' in word:
                word = word[:word.find('</p>')].lower()
            gwary[word] = gwara

        for key, value in gwary.items():
            if word_to_find.lower() in key.lower():
                context['word_to_find'] = word_to_find.capitalize()
                context['poznan_word'] = value.capitalize()
        
        if not context.get('poznan_word'):
            context['not_found'] = True

    return render(request, 'find_word.html', context)