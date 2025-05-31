from typing import List, Dict, Tuple, Any

def read_csv(file_path: str) -> Tuple[List[Dict[str, Any]]]:
    """Reads a CSV file and returns a list of dictionaries representing each row.
    
    Args:
        file_path (str): The path to the CSV file.
       
    Returns:
        Tuple[List[Dict[str, Any]], List[Dict[str,int]]]: A tuple containing:
            - A list of dictionaries, where each dictionary represents a row.
            - The number of columns in the CSV file.
            - The number of rows in the CSV file.
            - The size of the CSV file in bytes.
    
    Raises:
        FileNotFoundError: If the file does not exist
    """
    import csv
    import os
    try:
        with open(file_path, mode='r', newline='', encoding='utf') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        count_row = len(data)
        count_col = len(reader.fieldnames) if reader.fieldnames else 0
        size_csv = os.path.getsize(file_path)
        resumen = {
            "columns": count_col,
            "rows": count_row,
            "size_bytes": size_csv
        }
        return data, resumen
    except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} does not exist.")   #Futuro punto de a;adir error en archivo .log
    