import json


def modify_property(json_file_path, property_name, value):
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Modificar la propiedad en el objeto JSON
        json_data['py'][property_name] = value

        # Escribir el objeto JSON modificado de vuelta al archivo
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=4)