from .models import User
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm, ParagraphErrorList, ProfileForm, UserForm
# Create your views here.


def dashboard(request):
    return render(request, "accounts/dashboard.html")


def signin(request):
    return render(request, 'accounts/signin.html', {})


def signup(request):
    return render(request, 'accounts/signup.html', {})


def profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)

        if request.method == 'GET':
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
            return render(request, 'accounts/profile2.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })
        elif request.method == 'POST':
            print('-'*100)
            print(request.user)
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(
                request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                print('*' * 100)

                user = user_form.save()
                profile_form = profile_form.save()

                user.refresh_from_db()
                return render(request, 'accounts/dashboard.html', {'user': user})
            else:
                context = {
                    "errors_us": user_form.errors.items(),
                    "errors_pf": profile_form.errors.items()
                }
                return render(
                    request, "accounts/profile2.html",
                    context
                )
            # return redirect('http://localhost:8000/accounts/dashboard')

    return render(request, 'accounts/signup.html', {})


def register(request):
    context = {"form": CustomUserCreationForm}
    if request.method == "GET":
        return render(
            request, "accounts/signup.html",
            context
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(
            request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            print('yeap')
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect('http://localhost:8000/')
        else:
            context["errors"] = form.errors.items()
            return render(
                request, "accounts/signup.html",
                context
            )


def register_v2(request):
    context = {}

    if request.method == "GET":
        form_user = UserForm()
        form_profile = ProfileForm()

        context = {
            'user_form': form_user,
            'profile_form': form_profile
        }

        return render(
            request, "accounts/signup2.html",
            context
        )

    elif request.method == "POST":

        form_user = UserForm(
            request.POST, error_class=ParagraphErrorList)
        form_profile = ProfileForm(
            request.POST, error_class=ParagraphErrorList)
        if form_user.is_valid() and form_profile.is_valid():
            # with transaction.atomic():

            # user = form_user.save()
            # user.backend = "django.contrib.auth.backends.ModelBackend"

            # user.refresh_from_db()
            # user.profile.location1 = form_profile.cleaned_data.get(
            #     'location1')
            # user.profile.location2 = form_profile.cleaned_data.get(
            #     'location2')
            # user.profile.city = form_profile.cleaned_data.get('city')
            # user.profile.state = form_profile.cleaned_data.get('state')
            # user.profile.zip = form_profile.cleaned_data.get('zip')
            # user.save()
            user = form_user.save()
            # profile = form_profile.save()

            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.refresh_from_db()

            user.profile.location1 = form_profile.cleaned_data.get(
                'location1')
            user.profile.location2 = form_profile.cleaned_data.get(
                'location2')
            user.profile.city = form_profile.cleaned_data.get('city')
            user.profile.state = form_profile.cleaned_data.get('state')
            user.profile.zip = form_profile.cleaned_data.get('zip')
            user.save()
            # user = authenticate(request, username=user.username, password=user.password)

            # user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')

            return render(
                request, "accounts/dashboard.html",
                context
            )
        else:
            context["errors_us"] = form_user.errors.items()
            context["errors_pf"] = form_profile.errors.items()
            return render(
                request, "accounts/signup2.html",
                context
            )
