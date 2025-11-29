# generate_gallery.py
import os
import glob

def create_gallery():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(project_root, "outputs", "images")
    output_html = os.path.join(project_root, "outputs", "gallery.html")
    
    if not os.path.exists(images_dir):
        print("No images directory found. Run main.py first.")
        return

    images = glob.glob(os.path.join(images_dir, "*.png"))
    images.sort()
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VLM Graph Gallery</title>
        <style>
            body { font-family: sans-serif; padding: 20px; background: #f0f0f0; }
            .gallery { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
            .card { background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
            img { max-width: 400px; height: auto; border: 1px solid #ddd; }
            h3 { margin: 10px 0 0 0; color: #333; }
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Generated Graphs Gallery</h1>
        <div class="gallery">
    """
    
    for img_path in images:
        filename = os.path.basename(img_path)
        # Relative path from html file to image
        rel_path = f"images/{filename}"
        html_content += f"""
            <div class="card">
                <img src="{rel_path}" alt="{filename}">
                <h3>{filename}</h3>
            </div>
        """
        
    html_content += """
        </div>
    </body>
    </html>
    """
    
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Gallery created at: {output_html}")

if __name__ == "__main__":
    create_gallery()
