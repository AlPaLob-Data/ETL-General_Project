from typing import List, Dict, Any

def write_csv(data: List[Dict[str, Any]], file_path: str) -> None:
    '''
    Write CSV file from a list of dictionaries.
    Args:
        data (List[Dict[str, Any]]): List of dictionaries to write
        file_path (str): Path to the CSV file to be written or exported.
    Returns:
        None: Writes the CSV file to path specified by file_path.
    '''
    import csv
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data) 
    except OSError as e:
        print(f'Error: An error occurred while writing "{file_path}":  {e}')
    except IndexError: 
        print("Error: The data list is empty or the dictionaries do not have consistent keys.")

    return


        
            




