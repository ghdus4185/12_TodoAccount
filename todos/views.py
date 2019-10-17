from django.shortcuts import render
from IPython import embed
# Create your views here.


def index(request):
    # visit_num = request.session.get('visit_num', 0)
    # request.session['visit_num'] = visit_num + 1
    # request.session.modified = True
    # context = {
    #     'visit_num': visit_num
    # }
    return render(request, 'todos/index.html')
