from django.shortcuts import render, get_object_or_404

from snowboard.models import Snowboard


def get_home(request):
    snowboard = Snowboard.objects.all()
    return render(
        request, "main.html", {"snowboard": snowboard},
    )


def get_one_board(request, pk):
    snowboard = get_object_or_404(Snowboard, pk=pk)
    # snowboard = Snowboard.objects.all()
    return render(
        request, "one_snowboard.html", {"snowboard": snowboard},
    )
