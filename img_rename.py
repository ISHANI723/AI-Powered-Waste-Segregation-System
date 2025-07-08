import os

# Define dataset structure
dataset_types = ["train", "test"]
categories = {"Dry": 0, "Wet": 1, "Paper": 2}
valid_extensions = {".jpg", ".jpeg", ".png"}

# Iterate over train and test datasets
for dataset_type in dataset_types:
    dataset_path = os.path.join("DATASET-F", dataset_type)
    
    for category, label in categories.items():
        folder_path = os.path.join(dataset_path, category)
        
        # ✅ Create folder if missing
        if not os.path.exists(folder_path):
            print(f"📂 Creating folder: {folder_path}")
            os.makedirs(folder_path)

        # Process only if folder exists and contains images
        files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[-1].lower() in valid_extensions]
        if not files:
            print(f"⚠️ No images found in {folder_path}, skipping.")
            continue
        
        files.sort()  # Sort for consistency
        for i, filename in enumerate(files):
            ext = os.path.splitext(filename)[-1]
            new_name = f"{category.lower()}_{i+1:03d}{ext}"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

        print(f"✅ Renamed {len(files)} files in {folder_path}.")

print("🎉 Dataset renaming completed successfully!")
    
