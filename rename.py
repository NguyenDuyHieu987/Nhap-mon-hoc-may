import os

folder = "./Dataset/African_Wildlife/zebra/"
count = 1129
# count increase by 1 in each iteration
# iterate all files from a directory
for file_jpg in os.listdir(folder):
    if file_jpg.lower().endswith('.jpg'):
        count += 1
        # Construct old file name
        source = folder + file_jpg

        # Adding the count to the new file name and extension
        destination_jpg = folder  + str(count) + ".jpg"

        # Renaming the file
        os.rename(source, destination_jpg)
    
count = 1129
for file_txt in os.listdir(folder):
    if file_txt.lower().endswith('.txt'):
        count += 1
        # Construct old file name
        source = folder + file_txt

        # Adding the count to the new file name and extension
        destination_txt = folder  + str(count) + ".txt"
        
        # Renaming the file
        os.rename(source, destination_txt)
        
# 3 0.348438 0.491765 0.693750 0.870588