# BackFree - AI Image Background Remover

BackFree is a Django-based web application that allows users to upload images and automatically remove their backgrounds using AI (via the `rembg` library). It offers a clean UI built with Tailwind CSS and provides instant download of processed transparent PNGs.

---

## 🖼️ Live Preview

🧪 **Coming soon:** 

---

## 🌟 Features

* ✨ AI-powered background removal with `rembg`
* 🖼️ Upload, process, and download transparent images
* 🧩 Example gallery and feature showcase
* ⚡ Instant processing and privacy-focused
* 💡 Built with Django, Tailwind CSS, and Pillow

---

## 🛠️ Tech Stack

* **Frontend:** HTML, Tailwind CSS, JavaScript (minimal)
* **Backend:** Django (Python)
* **AI Engine:** rembg
* **Image Processing:** Pillow
* **Storage:** Django FileSystemStorage

---

## 📁 Folder Structure (important parts)

```
BackFree/
├── core/
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── result.html
│   │   └── error.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── static/
│   ├── images/
│   │   ├── bg.png
│   │   ├── before.jpg
│   │   └── after.png
├── media/uploads/
│   ├── original/
│   └── processed/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🚀 How It Works

1. **User visits homepage** (`/`)
2. Uploads an image → Form POSTs to `process_image` view
3. `rembg` removes the background using AI
4. Processed image is saved in `/media/uploads/processed/`
5. User sees result with option to download

---

## 🧠 Core Logic (`views.py`)

### `home(request)`

* Fetches `Example` and `Feature` objects for the homepage
* Renders `index.html`

### `process_image(request)`

* Handles file upload and background removal
* Uses `rembg` to process image
* Saves original + processed image to media folder
* Returns `result.html` template with image preview

### `result(request, pk)`

* Fetches specific processed image by ID
* Displays processed result again

---

## 💻 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/abdullahfahim2/BackFree.git
cd BackFree
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Include these in `requirements.txt`:
> `django`, `rembg`, `Pillow`

### 4. Run the Server

```bash
python manage.py runserver
```

Then go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 Models (Example)

```python
class Example(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    before_image = models.ImageField(upload_to='examples/before/')
    after_image = models.ImageField(upload_to='examples/after/')

class Feature(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

class ProcessedImage(models.Model):
    original_image = models.ImageField(upload_to='uploads/original/')
    processed_image = models.ImageField(upload_to='uploads/processed/')
    session_key = models.CharField(max_length=100)
```

---

## ✉️ Contact

* Email: [abdullahfahim.me@gmail.com](mailto:abdullahfahim.me@gmail.com)
* Facebook: [Md Abdullah Al Fahim](https://facebook.com/abdullah.fahim.507)
* GitHub: [@abdullahfahim2](https://github.com/abdullahfahim2)

---

## 📄 License

You are free to use, modify, and distribute it.

---

## 💬 Credits

* Built by [Md Abdullah Al Fahim](https://github.com/abdullahfahim2)
* Uses open-source libraries: `rembg`, `Pillow`, `Tailwind CSS`, `FontAwesome`

---

