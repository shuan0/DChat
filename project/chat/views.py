from django.shortcuts import render, redirect
from .models import User, UserAvatar

def home(request):
    return render(request, 'chat/home.html')

def profile(request):
    if request.method == 'GET':
        return render(request, 'chat/profile.html')

    avatar = request.FILES.get('avatar', '')
    if avatar:
        user_avatar = UserAvatar.objects.create(avatar=avatar)
        user_avatar.save()
        avatar = user_avatar.avatar
        user_avatar.delete()

    username = request.POST['username']
    try:
        if request.user.username == username: raise Exception()
        User.objects.get(username=username)
        return redirect('profile')
    except:
        User.objects.filter(username=request.user.username).update(
            username=username,
            avatar=(avatar if avatar else request.user.image)
        )

    return redirect('profile')
