from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PlaceForm
from .models import Place


def map_page(user_req):
    form = PlaceForm()
    add_place_open = False

    if user_req.method == "POST":
        form = PlaceForm(user_req.POST)
        if form.is_valid():
            form.save()
            messages.success(user_req, "Place added successfully.")
            return redirect("map_page")
        add_place_open = True

    locations = list(Place.objects.values(
        "id", "name", "category", "description", "lat", "lng"
    ))
    return render(
        user_req,
        "places/index.html",
        {
            "locations": locations,
            "form": form,
            "add_place_open": add_place_open,
        },
    )
