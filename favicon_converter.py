#!/usr/bin/env python3
"""
Favicon Converter Script
Converts a favicon to multiple PNG sizes for web and mobile use.
"""

import sys
from pathlib import Path
from PIL import Image


def convert_favicon(input_path, output_dir="."):
    """
    Convert a favicon to multiple sizes.
    
    Args:
        input_path: Path to the input favicon file
        output_dir: Directory to save the output files (default: current directory)
    """
    # Define output sizes and filenames
    sizes = {
        "favicon-16x16.png": (16, 16),
        "favicon-32x32.png": (32, 32),
        "apple-touch-icon.png": (180, 180),
        "android-chrome-192x192.png": (192, 192),
        "android-chrome-512x512.png": (512, 512),
    }
    
    # Load the input image
    try:
        img = Image.open(input_path)
        print(f"✓ Loaded {input_path} ({img.size[0]}x{img.size[1]})")
    except FileNotFoundError:
        print(f"✗ Error: File '{input_path}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error loading image: {e}")
        sys.exit(1)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate each size
    print(f"\nGenerating favicon variants in '{output_dir}':")
    for filename, size in sizes.items():
        # Resize using high-quality resampling
        resized_img = img.resize(size, Image.Resampling.LANCZOS)
        
        # Save the resized image
        output_file = output_path / filename
        resized_img.save(output_file, "PNG", optimize=True)
        print(f"  ✓ {filename} ({size[0]}x{size[1]})")
    
    print(f"\n✓ All favicon variants created successfully!")


def main():
    if len(sys.argv) < 2:
        print("Usage: python favicon_converter.py <input_favicon> [output_directory]")
        print("\nExample:")
        print("  python favicon_converter.py favicon.ico")
        print("  python favicon_converter.py favicon.png ./output")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    convert_favicon(input_file, output_dir)


if __name__ == "__main__":
    main()