import os

release_file_path = r"D:\HP\Links\Leaks\Ny mappe\Pstars.Leaks.zip."

# Assuming you want to iterate from 1 to 34
for i in range(1, 30):
    file_number = f"{i:03d}"  # Format the number with leading zeros
    file_path = f'{release_file_path}{file_number}'
    
    command = f'gh release upload PS "{file_path}"'
    
    # Execute the command
    os.system(command)