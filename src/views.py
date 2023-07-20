from django.http import JsonResponse


def process_form_data(request):
    if request.method == 'GET':

        levels = request.GET.get('LEVELS')
        form = request.GET.get('FORM')
        topping = request.GET.get('TOPPING')
        words = request.GET.get('WORDS')
        comments = request.GET.get('COMMENTS')
        name = request.GET.get('NAME')
        phone = request.GET.get('PHONE')
        email = request.GET.get('EMAIL')
        address = request.GET.get('ADDRESS')
        date = request.GET.get('DATE')
        time = request.GET.get('TIME')
        delivcomments = request.GET.get('DELIVCOMMENTS')
        print("LEVELS:", levels)
        print("FORM:", form)
        print("TOPPING:", topping)

        return JsonResponse({"status": "success", "message": "Данные успешно получены и обработаны"})
    else:

        return JsonResponse({"status": "error", "message": "Метод не разрешен"})

