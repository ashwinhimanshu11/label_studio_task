import json
import os

main_folder_path = "/run/media/ashwinhimanshu11/New Volume/Work/Work/label_studio_task/separated_json_files"

files = os.listdir(main_folder_path)
    
json_files = [file for file in files if file.endswith('.json')]

for json_file in json_files:
    file_path = os.path.join(main_folder_path, json_file)
    with open(file_path, 'r') as f:
        data = json.load(f)


    client_format_data = []

    for item in data["result"]:
        text = None
        bbox = None

        if "text" in item["value"]:
            text = item["value"]["text"][0]

        if "x" in item["value"] and "y" in item["value"] and "width" in item["value"] and "height" in item["value"] and "rotation" in item["value"]:
            bbox = {
                "x": item["value"]["x"],
                "y": item["value"]["y"],
                "width": item["value"]["width"],
                "height": item["value"]["height"],
                "rotation": item["value"]["rotation"]
            }

        if text and bbox:
            client_format_data.append({"text": text, "bbox": bbox})

        # print(client_format_data)

        for data in client_format_data:

            print(data)

            filename = os.path.join(f"client_format.json")
            with open(filename, "w") as json_file:
                json.dump(client_format_data, json_file, indent=4)