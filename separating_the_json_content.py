import json
import os

file_open = open('label_studio_task.json')
data_file = json.load(file_open)

image_path = "/run/media/ashwinhimanshu11/New Volume/Work/Work/label_studio_task/images"

image_file_names = []
for (dirpath, dirnames, filenames) in os.walk(image_path):
    image_file_names.extend(filenames)
    break

output_folder = "separated_json_files"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for item in data_file:
    image_path = os.path.basename(item["file_upload"])
    image_name = os.path.splitext(image_path)[0]

    annotations = item["annotations"]
    for annotation in annotations:
        annotation_id = annotation["id"]
        filename = os.path.join(output_folder, f"{image_name.split("-")[1]}.json")
        with open(filename, "w") as json_file:
            json.dump(annotation, json_file, indent=4)
        print(f"Annotation {annotation_id} saved to {filename}")

file_open.close()
