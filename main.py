from src.data_ingestion.read_csv import read_csv
from src.data_transform.standarization import standarize_headers_data
from src.data_load.write_csv import write_csv
from src.data_ingestion.read_dict_to_json import read_dict_to_json

if __name__ == "__main__":
    file_path = r'./data_raw/datos_sucios.csv'

    # Leer y estandarizar los datos del CSV
    data, resumen = read_csv(file_path)
    data_standarized = standarize_headers_data(data)
    write_csv(data_standarized, r'./data_clean/datos_limpio.csv')
    print("Datos Estandarizados:", data_standarized[:5])

    # Convertir los datos estandarizados a JSON
    file_path_json = r'./data_clean/datos_limpio.json'
    read_dict_to_json(file_path, file_path_json, indent=4)
    print(f"Datos escritos en {file_path_json}...")