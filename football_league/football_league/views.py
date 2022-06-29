from django.shortcuts import render
from django.views import View


class MainView(View):
    """
    # Return home page
    """

    def get(self, request, *args, **kwargs):
        return render(request, "templates/main.html")
