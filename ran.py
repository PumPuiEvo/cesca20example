import random

def pick_random_data(dummy_array, num_picks):
    if num_picks > len(dummy_array):
        raise ValueError("Number of picks exceeds the size of the dummy array.")
    
    picked_indices = set()
    picked_data = []
    
    while len(picked_indices) < num_picks:
        index = random.randint(0, len(dummy_array) - 1)
        if index in picked_indices:
            print(f"Duplicate index found: {index}, skipping...")
        else:
            picked_indices.add(index)
            picked_data.append(dummy_array[index])
    
    return picked_data

if __name__ == "__main__":
    dummy_array = [""
    "พั้นรักแมว Game Design", 
    "Database 1 ชื่อกลุ่ม", 
    "Game Design 1", 
    "Kelpie ปี้ ปิ๊ด", 
    "Digital 1 ไม่บอกอย่าหลอกถาม", 
    "DATABASE 2 นะจ๊ะ",]

    random_data = pick_random_data(dummy_array, 6)
    print("Randomly picked data:", random_data)