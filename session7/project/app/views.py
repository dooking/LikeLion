from django.shortcuts import render

# Create your views here.


def count(request):
    return render(request, 'count.html')


def result(request):
    text = request.POST['text']
    total_len = len(text)
    noblank_text = text.replace(" ","")
    noblank_len = len(noblank_text)
    cnt = 1
    for word in text:
        if(word == ' '):
            cnt += 1

    return render(request, 'result.html', {
        'total_len': total_len,
        'text': text,
        'noblank_text': noblank_text,
        'noblank_len': noblank_len,
        'word_count' : cnt,
})

def back(request):
    return render(request, 'count.html')
