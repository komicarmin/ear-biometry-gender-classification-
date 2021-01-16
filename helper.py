import os
import json
from shutil import copyfile

male_count = 1
female_count = 1

for root, dirs, files in os.walk('./awe'):
    for dir in dirs:
        with open('./awe/' + dir + '/annotations.json') as f:
            annot = json.load(f)
            cls = "male" if annot["gender"] == "m" else "female"

        for file in os.listdir('./awe/' + dir):
            if file.endswith('.png'):
                if cls == "male":
                    copyfile(os.path.join('./awe/' + dir, file), cls + '/' + str(male_count) + '.png')
                    male_count += 1
                else:
                    copyfile(os.path.join('./awe/' + dir, file), cls + '/' + str(female_count) + '.png')
                    female_count += 1
