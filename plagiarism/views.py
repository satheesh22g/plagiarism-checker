from django.shortcuts import render
from .utils import check_plagiarism,calculate_marks


from django.core.files.storage import default_storage

def handle_uploaded_file(uploaded_file):
    file_path = default_storage.save('plagiarism/uploads/' + uploaded_file.name, uploaded_file)
    return file_path
def plagiarism_check(request):
    message=None
    try:
        if request.method == 'POST' and request.FILES['new_file']:
            new_file = request.FILES['new_file']
            file_path = handle_uploaded_file(new_file)
            similarity= check_plagiarism(file_path)
            print(new_file)
            marks = calculate_marks(similarity * 100)
            return render(request, 'results.html', {'similarity_score': round(similarity*100,2),'message': message,'score':marks})
        
    except Exception as e:
        print(e)
        message = "Submission Failed! Check the Document type and Try again!"

    return render(request, 'home.html',{'message':message})

def marks_calculation(request):
    return render(request, 'marks_calculation.html')
