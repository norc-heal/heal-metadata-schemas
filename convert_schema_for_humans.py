

file_to_convert = "cedar json"


# https://github.com/coveooss/json-schema-for-humans

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration


input_clean_json = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema.json"
output_clean_html = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-for-humans.html"

input_cedar_json = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-cedar-template.json"
output_cedar_html = r"C:\Users\tentner-andrea\project_repositories\heal-metadata-schemas\study-metadata-schema-cedar-template-for-humans.html"


if file_to_convert == "clean json":
    input_json = input_clean_json
    output_html = output_clean_html
elif file_to_convert == "cedar json":
    input_json = input_cedar_json
    output_html = output_cedar_html
else: 
    raise ValueError("file_to_convert must be one of clean json or cedar json")

config = GenerationConfiguration(copy_css=True,expand_buttons=True)
generate_from_filename(input_json,output_html, config=config) 
