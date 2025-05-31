from typing import List, Dict, Any

def standarize_headers_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    '''
    Standaroze headers of the data to lower case replace spaces and remove the accent mark.

    Args:
        data (List[Dict[str, Any]]): The list of dictionaries representing each row.
    Returns:
       List[Dict[str, Any]]: A list of dictionaries with standarized headers.
    '''
    import unicodedata
    data_standarized = []
    original_headers = list(data[0].keys()) 
    standarize_headers = []
    #Remove and standarized headers
    for header in data[0].keys():
        normalized_header = unicodedata.normalize('NFD', header)
        header_withoput_accent_mark = ''.join(c for c in normalized_header if unicodedata.category(c) != 'Mn')
        standarize_headers.append(header_withoput_accent_mark.lower().replace(" ", "_").strip())
    
    #Standarize headers of the data
    for row in data:
        new_row = {}
        for old_header, value in row.items():
            index = original_headers.index(old_header)
            new_header = standarize_headers[index]
            new_row[new_header] = value
        data_standarized.append(new_row)

    return data_standarized

