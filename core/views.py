from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
import os
from rembg import remove
from PIL import Image
import io

def home(request):
    examples = Example.objects.all()
    features = Feature.objects.all()
    
    context = {
        'examples': examples,
        'features': features,
    }
    return render(request, 'core/index.html', context)

def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']

        # ✅ Ensure user session exists
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key

        # ✅ Define storage for original images
        original_dir = os.path.join(settings.MEDIA_ROOT, 'uploads/original')
        fs = FileSystemStorage(location=original_dir)
        filename = fs.save(uploaded_file.name, uploaded_file)
        original_path = fs.path(filename)

        try:
            # ✅ Open and process the image using rembg
            input_image = Image.open(original_path)
            output_image = remove(input_image)

            # ✅ Prepare processed image path
            processed_filename = f"processed_{os.path.splitext(filename)[0]}.png"
            processed_dir = os.path.join(settings.MEDIA_ROOT, 'uploads/processed')
            processed_path = os.path.join(processed_dir, processed_filename)
            os.makedirs(processed_dir, exist_ok=True)

            # ✅ Save processed image as PNG
            output_image.save(processed_path)

            # ✅ Save paths in database
            processed_image = ProcessedImage.objects.create(
                original_image=f"uploads/original/{filename}",
                processed_image=f"uploads/processed/{processed_filename}",
                session_key=session_key
            )

            # ✅ Optionally delete original file (already saved in DB)
            # fs.delete(filename)

            # ✅ Return result page
            return render(request, 'core/result.html', {
                'original_image': processed_image.original_image.url,
                'processed_image': processed_image.processed_image.url
            })

        except Exception as e:
            # Handle unexpected processing errors gracefully
            print(f"Error processing image: {e}")
            return render(request, 'core/error.html', {'error': 'Image processing failed. Please try again.'})

    return redirect('home')

def result(request, pk):
    processed_image = ProcessedImage.objects.get(pk=pk)
    return render(request, 'core/result.html', {
        'original_image': processed_image.original_image.url,
        'processed_image': processed_image.processed_image.url
    })