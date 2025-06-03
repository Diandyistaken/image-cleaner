import os
import time
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCHED_DIR = r"C:\Users\mo_ma\Downloads\downthemall"

ALLOWED_EXTENSIONS = [".jpg", ".png"]

def is_unwanted_extension(ext):
    return ext.lower() not in ALLOWED_EXTENSIONS

def convert_jpg_to_png(jpg_path):
    base, _ = os.path.splitext(jpg_path)
    png_path = base + ".png"

    if os.path.exists(png_path):
        os.remove(jpg_path)
        print(f"❌ Silindi (PNG zaten vardı): {os.path.basename(jpg_path)}")
        return

    try:
        with Image.open(jpg_path) as img:
            img.save(png_path, "PNG")
        os.remove(jpg_path)
        print(f"✅ Dönüştürüldü: {os.path.basename(jpg_path)} → {os.path.basename(png_path)}")
    except Exception as e:
        print(f"⚠️ Dönüştürme hatası: {e}")

def initial_cleanup():
    print("🔄 Başlangıç temizliği yapılıyor...")
    for file in os.listdir(WATCHED_DIR):
        path = os.path.join(WATCHED_DIR, file)
        if os.path.isdir(path):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext == ".jpg":
            convert_jpg_to_png(path)
        elif is_unwanted_extension(ext):
            try:
                os.remove(path)
                print(f"❌ Silindi (istenmeyen uzantı): {file}")
            except Exception as e:
                print(f"⚠️ Silme hatası: {e}")

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.handle(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.handle(event.src_path)

    def handle(self, path):
        _, ext = os.path.splitext(path)
        ext = ext.lower()

        if ext == ".jpg":
            convert_jpg_to_png(path)
        elif is_unwanted_extension(ext):
            try:
                os.remove(path)
                print(f"❌ Silindi (istenmeyen dosya): {os.path.basename(path)}")
            except Exception as e:
                print(f"⚠️ Silme hatası: {e}")

def start_watching():
    print(f"📁 İzlenen klasör: {WATCHED_DIR}")
    observer = Observer()
    handler = FileEventHandler()
    observer.schedule(handler, WATCHED_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 İzleme durduruldu.")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    initial_cleanup()
    start_watching()
