from django.shortcuts import render, redirect
from .models import Message, Comment
from ..login_register.models import User

def wall(request):
    # check if there is currently a user id in session
    if not 'user_id' in request.session:
        return redirect('/')

    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    messages = Message.objects.all().order_by('-created_at')
    context = {
        'user': user,
        'messages': messages
    }
    return render(request, 'wall/wall.html', context)

def post_message(request):
    if request.method == "POST":
        data = request.POST
        user_id = request.session['user_id']
        Message.objects.post_message(data['message'], user_id)
        return redirect('/wall')

def post_comment(request):
    if request.method == "POST":
        data = request.POST
        user_id = request.session['user_id']
        Comment.objects.post_comment(data['comment'], user_id, data['message_id'])
    return redirect('/wall')
