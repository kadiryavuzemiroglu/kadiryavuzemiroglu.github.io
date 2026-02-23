import fitz
import os

pdf_path = "/Users/kyemiroglu/Downloads/Kadir Yavuz Emiroglu, Dissertation Defense Deck.pdf"
output_dir = "/Users/kyemiroglu/gemini/antigravity/scratch/uxr-portfolio/web_images/slides"

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    output_path = os.path.join(output_dir, f"slide_{i+1:03d}.png")
    pix.save(output_path)
    print(f"Saved {output_path}")

print("Done")
