from django.shortcuts import render,redirect
from django.views import View
from django.http import FileResponse
from django.conf import settings
from pathlib import Path
from .forms import ReviewForm
from .models import Review


class Home(View):
    def get(self, request):
        return render(request, "home.html")

def download_file(request):
    file_path = Path(settings.MEDIA_ROOT) / 'myapp/resume/Akhilesh.Fresher.2023.pdf'  # Adjust the path based on your file location
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="Akhilesh.Fresher.2023.pdf"'
    return response


class Projects(View):
    def get(self, request):
        return render(request, "home.html")
    
class ReviewView(View):
    template_name = 'home.html'

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()  # Retrieve existing reviews
        return render(request, self.template_name, {'form': form, 'reviews': reviews})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('Home')  # Redirect to the same page after submission
        reviews = Review.objects.all()
        return render(request, self.template_name, {'form': form, 'reviews': reviews})