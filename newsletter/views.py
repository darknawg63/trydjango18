from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = "Welcome"
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # do not use request.POST("full_name") as this bypasses validation and
        # escaping
        full_name = form.cleaned_data.get("full_name")

        if not full_name:
            full_name = "New full name"
            instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)
        #email = form.cleaned_data.get("email")
        #message = form.cleaned_data.get("message")
        #full_name = form.cleaned_data.get("full_name")
        #print(email, message, full_name)

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)
