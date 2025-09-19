from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

def home(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, 'resume/home.html', {'form': form})

def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    return render(request, 'resume/resume_detail.html', {'resume': resume})
