from src.data_ingestion.read_csv import read_csv
from src.data_transform.standarization import standarize_headers_data
from src.data_load.write_csv import write_csv


if __name__ == "__main__":
    file_path = r'.\data_raw\datos_sucios.csv'
    data, resumen = read_csv(file_path)
    data_standarized = standarize_headers_data(data)
    write_csv(data_standarized, r'.\data_clean\datos_limpio.csv')
    print("Data:", data[:5])
    print("Resumen:", resumen)
    print("Standarized Data:", data_standarized[:5])
