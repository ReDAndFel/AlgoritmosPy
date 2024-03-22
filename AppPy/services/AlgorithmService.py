from . import JsonService as js

def add_value(json_file_path, value):
        js.modify_property(json_file_path, "NaivOnArray", value)