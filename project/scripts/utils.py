import os
import requests
import psycopg2 as pg
import pandas as pd
from config import API_URL, CSV_FILE, DB_CONFIG


def fetch_data() -> pd.DataFrame:
    '''
    Handles data import for the BRT API and returns it in
    a DataFrame for easier data wrangling.

    Due to its JSON format, the API data is wrapped in
    a list named `veiculos`. As such, this single field
    is loaded into the DataFrame, as it actually contains
    all expected data.

    ### Arguments:
        None.
    
    ### Returns:
        data (`pandas.DataFrame`): A DataFrame containing
            BRT vehicle data in tabular format.
    '''

    response = requests.get(API_URL)

    data = pd.DataFrame()

    if response.status_code == 200:
        api_response = response.json()
        data = pd.DataFrame(api_response['veiculos'])

        data["dataHora"] = pd.to_datetime(
            data["dataHora"],
            unit = 's',
            utc = True
        ).dt.strftime("%Y-%m-%d %H:%M:%S%z")


    else:
        print(f"Failed to fetch data: {response.status_code}")

    return data


def write_csv():
    '''
    Collects data from the BRT API and loads it into a CSV file.
    Its path is specified in the `CSV_FILE` constant, in the
    `config.py` file.

    ### Arguments:
        None.
    
    ### Returns:
        None.
    '''

    df = fetch_data()

    if not df.empty:

        if os.path.exists(CSV_FILE):
            df.to_csv(CSV_FILE, mode='a', header=False, index=False)

        else:
            df.to_csv(CSV_FILE, index=False)

        print(f"Data written to path: {CSV_FILE}")

    else:
        print("No data to write.")


def load_to_postgres():

    conn = pg.connect(**DB_CONFIG)
    cursor = conn.cursor()

    df = pd.read_csv(CSV_FILE)

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO brt_data (
                codigo,
                placa,
                linha,
                latitude,
                longitude,
                dataHora,
                velocidade,
                id_migracao_trajeto,
                sentido,
                trajeto,
                hodometro,
                direcao,
                ignicao
            )
            VALUES (
                %s, %s, %s, %s, %s
                %s, %s, %s, %s, %s
                %s, %s, %s
            )
            """,
            [row[col] for col in df.columns]
        )

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into PostgreSQL.")
