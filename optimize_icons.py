import os
from PIL import Image, ImageDraw, ImageOps

def process_icon(input_path, output_path, target_size, radius):
    try:
        # Load image
        img = Image.open(input_path).convert("RGBA")
        
        # Find bounding box of non-white pixels (trim white space)
        # Convert to grayscale to find non-white pixels
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        
        if bbox:
            img = img.crop(bbox)
            
        # Calculate padding (15% padding)
        pad = int(target_size * 0.15)
        inner_size = target_size - (pad * 2)
        
        # Resize cropped image to fit inside inner_size
        img.thumbnail((inner_size, inner_size), Image.Resampling.LANCZOS)
        
        # Create a new white background with rounded corners
        out_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))
        mask = Image.new("L", (target_size, target_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, target_size, target_size), radius=radius, fill=255)
        
        # The background is white inside the rounded corners
        bg_rounded = Image.new("RGBA", (target_size, target_size), (255, 255, 255, 255))
        out_img.paste(bg_rounded, (0, 0), mask=mask)
        
        # Paste the logo in the center
        offset_x = (target_size - img.width) // 2
        offset_y = (target_size - img.height) // 2
        out_img.paste(img, (offset_x, offset_y), mask=img)
        
        out_img.save(output_path)
        print(f"Successfully processed {output_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    from PIL import ImageChops # Import here if needed
    
    # Process 512x512
    process_icon("assets/img/icon-512x512.png", "assets/img/icon-512x512.png", 512, 100)
    # Process 192x192
    process_icon("assets/img/icon-192x192.png", "assets/img/icon-192x192.png", 192, 38)
