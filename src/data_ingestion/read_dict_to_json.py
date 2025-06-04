from .read_csv import read_csv


def read_dict_to_json(file_path_csv:str, file_path_json:str, indent:int) -> None:
    """
    Reads a CSV file and converts its contents into a JSON format.
    Args:
        file_path (str): The path of charger the JSON file.
        indent (int): Indentation of tree JSON.
    Returns:
        None: The function writes the JSON data 
    """

    import json
    data_csv = read_csv(file_path_csv)
    try:
        with open(file_path_json, mode='w', encoding='utf-8') as file:
            file_json = json.dump(data_csv, file, indent=indent, ensure_ascii=False) 
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path_json} does not exist.") 
    return file_json

        