"""
Sticker Image Renaming Tool
This script helps you categorize and rename sticker images by theme.
"""

import os
from pathlib import Path

def main():
    print("=" * 60)
    print("STICKER IMAGE RENAMING TOOL")
    print("=" * 60)
    print("\nThis tool will help you rename your sticker images by theme.")
    print("\nInstructions:")
    print("1. The script will list each image file")
    print("2. Type a theme name (e.g., 'anime', 'space', 'cute-animals')")
    print("3. Type 'skip' to skip an image")
    print("4. Type 'done' when finished")
    print("5. Files will be renamed like: theme-pack-01.webp\n")
    
    # Get the sticker pics folder
    sticker_folder = Path("Sticker Pics")
    
    if not sticker_folder.exists():
        print(f"\nError: '{sticker_folder}' folder not found!")
        print("Make sure you run this script from the repository root directory.")
        return
    
    # Get all image files (excluding the 'For site' subfolder)
    image_files = [f for f in sticker_folder.iterdir() 
                   if f.is_file() and f.suffix.lower() in ['.webp', '.jpg', '.jpeg', '.png']]
    
    if not image_files:
        print("\nNo image files found in 'Sticker Pics' folder!")
        return
    
    print(f"\nFound {len(image_files)} images to process.\n")
    
    # Dictionary to track theme counts
    theme_counts = {}
    # List to store renaming operations
    rename_list = []
    
    for idx, img_file in enumerate(image_files, 1):
        print(f"\n[{idx}/{len(image_files)}] Current file: {img_file.name}")
        print(f"Full path: {img_file}")
        
        theme = input("Enter theme name (or 'skip'/'done'): ").strip().lower()
        
        if theme == 'done':
            print("\nFinishing up...")
            break
        
        if theme == 'skip' or theme == '':
            print("Skipped.")
            continue
        
        # Normalize theme name (replace spaces with hyphens)
        theme = theme.replace(' ', '-')
        
        # Track count for this theme
        if theme not in theme_counts:
            theme_counts[theme] = 0
        theme_counts[theme] += 1
        
        # Create new filename
        new_name = f"{theme}-pack-{theme_counts[theme]:02d}{img_file.suffix}"
        
        rename_list.append((img_file, new_name))
        print(f"Will rename to: {new_name}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nTotal images to rename: {len(rename_list)}")
    
    if theme_counts:
        print("\nThemes found:")
        for theme, count in sorted(theme_counts.items()):
            print(f"  - {theme}: {count} pack(s)")
    
    # Confirm renaming
    if rename_list:
        print("\n" + "=" * 60)
        confirm = input("\nProceed with renaming? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            print("\nRenaming files...")
            for old_path, new_name in rename_list:
                new_path = old_path.parent / new_name
                old_path.rename(new_path)
                print(f"✓ Renamed: {old_path.name} → {new_name}")
            
            print("\n✓ All files renamed successfully!")
            print("\nNext steps:")
            print("1. Check the renamed files in 'Sticker Pics' folder")
            print("2. Commit and push changes to GitHub:")
            print("   git add 'Sticker Pics'")
            print("   git commit -m 'Renamed sticker images by theme'")
            print("   git push")
        else:
            print("\nRenaming cancelled. No files were changed.")
    else:
        print("\nNo files to rename.")
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
