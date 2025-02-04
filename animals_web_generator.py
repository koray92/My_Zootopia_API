import json
import requests


input_animal_name = input("Enter name of an animal: ")
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(input_animal_name)
response = requests.get(api_url, headers={'X-Api-Key': 'SKDWNkk5OmzCCjkkIk9qNw==kHPaSVtQHBC8o5RO'})


def get_animal_name():
    output = ""
    if response.json() == []:
        html_file = str(read_html("animals_template.html"))
        new_html = html_file.replace("My Animal Repository",
                                     f"The animal {input_animal_name} doesn't exist")
        with open("animals.html", "w") as f:
            f.write(new_html)
        return new_html
    for i in response.json():
        skip_type = i.get("characteristics", {}).get("type", "Unknown")
        if skip_type == "Unknown":
            output += "<li class='cards__item'>\n"
            output += f"  <div class='card_title'>{i['name']}</div>\n"
            output += "   <p class='card__text'>"
            output += f"      <strong>Diet:</strong> {i['characteristics']['diet']}<br/>\n"
            output += f"      <strong>Location:</strong> {i['locations'][0]}<br/>\n"
            output += "   </p>"
            output += "</li>"

        else:
            output += "<li class='cards__item'>\n"
            output += f"  <div class='card_title'> {i['name']}</div>\n"
            output += "   <p class='card__text'>\n"
            output += f"      <strong>Diet:</strong> {i['characteristics']['diet']}<br/>\n"
            output += f"      <strong>Location:</strong> {i['locations'][0]}<br/>\n"
            output += f"      <strong>Type:</strong> {i['characteristics']['type']}<br/>\n"
            output += "   </p>"
            output += "</li>"

    return output


def read_html(file_path):
    with open(file_path, "r") as f:
        file_str = f.read()
        return file_str


html_file = str(read_html("animals_template.html"))
animals_str = get_animal_name()

new_html = html_file.replace("__REPLACE_ANIMALS_INFO__", animals_str)

with open("animals.html", "w") as f:
    f.write(new_html)

print("Website was successfully generated to the file animals.html.")