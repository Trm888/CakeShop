from django.http import JsonResponse


def process_form_data(request):
    if request.method == 'GET':

        levels = request.POST.get('LEVELS')
        form = request.POST.get('FORM')
        topping = request.POST.get('TOPPING')
        words = request.POST.get('WORDS')
        comments = request.POST.get('COMMENTS')
        name = request.POST.get('NAME')
        phone = request.POST.get('PHONE')
        email = request.POST.get('EMAIL')
        address = request.POST.get('ADDRESS')
        date = request.POST.get('DATE')
        time = request.POST.get('TIME')
        delivcomments = request.POST.get('DELIVCOMMENTS')
        print("LEVELS:", levels)
        print("FORM:", form)
        print("TOPPING:", topping)

        return JsonResponse({"status": "success", "message": "Данные успешно получены и обработаны"})
    else:

        return JsonResponse({"status": "error", "message": "Метод не разрешен"})

