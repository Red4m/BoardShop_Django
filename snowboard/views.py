from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from snowboard.models import Snowboard


def get_home(request):
    snowboard = Snowboard.objects.all()
    user = User.objects.all()
    return render(
        request, "index.html", {"snowboard": snowboard, "user": user},
    )


def get_one_board(request, pk):
    snowboard = get_object_or_404(Snowboard, pk=pk)
    # snowboard = Snowboard.objects.all()
    return render(
        request, "one_snowboard.html", {"snowboard": snowboard},
    )
