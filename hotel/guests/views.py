from django.shortcuts import redirect, render

from .models import Guest


# Create your views here.
def guest_list(request):
    guests = Guest.objects.all()

    return render(request, "guest_list.html", {"guests": guests})


def guest_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        entry_day = request.POST.get("entry_day")
        guest = Guest.objects.create(name=name, entry_day=entry_day)
        return redirect("guests")
    return render(request, "guest_add.html")


def guest_delete(request, guest_id):
    guest = Guest.objects.get(id=guest_id)
    guest.delete()
    return redirect("guests")
