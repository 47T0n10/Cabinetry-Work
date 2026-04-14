import os
from PIL import Image
import json

original_dir = r"C:\Users\m_cha\OneDrive\Desktop\Cabinetry-Work\portfolio\original"
optimized_dir = r"C:\Users\m_cha\OneDrive\Desktop\Cabinetry-Work\public\images\portfolio"
js_file_path = r"C:\Users\m_cha\OneDrive\Desktop\Cabinetry-Work\scripts.js"

# Create optimized directory if not exists
if not os.path.exists(optimized_dir):
    os.makedirs(optimized_dir)

# List all jpg files
files = [f for f in os.listdir(original_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
# Sort files by filename (since they have dates) in reverse
files.sort(reverse=True)

processed_files = []

print(f"Starting optimization of {len(files)} images...")

for i, filename in enumerate(files):
    try:
        img_path = os.path.join(original_dir, filename)
        with Image.open(img_path) as img:
            # Handle Orientation from EXIF
            try:
                from PIL import ExifTags
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = img._getexif()
                if exif is not None:
                    orientation = exif.get(orientation)
                    if orientation == 3: img = img.rotate(180, expand=True)
                    elif orientation == 6: img = img.rotate(270, expand=True)
                    elif orientation == 8: img = img.rotate(90, expand=True)
            except (AttributeError, KeyError, IndexError):
                pass # No EXIF or Orientation tag

            # Resize (Max 1200px)
            max_size = (1200, 1200)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save as optimized
            new_filename = f"job_{i+1:03d}.jpg"
            save_path = os.path.join(optimized_dir, new_filename)
            img.save(save_path, "JPEG", quality=85, optimize=True)
            processed_files.append(new_filename)
            print(f"Processed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Update scripts.js
if processed_files:
    try:
        with open(js_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the imageList array
        files_json = json.dumps(processed_files)
        # Regex replacement for imageList = [];
        import re
        new_content = re.sub(r'const imageList = \[.*?\];', f'const imageList = {files_json};', content, flags=re.DOTALL)

        with open(js_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated scripts.js with the new image list.")
    except Exception as e:
        print(f"Error updating scripts.js: {e}")

print("Done.")
