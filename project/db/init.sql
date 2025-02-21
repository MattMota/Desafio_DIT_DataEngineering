CREATE TABLE IF NOT EXISTS brt_data (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(100),
    placa VARCHAR(100),
    linha VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    dataHora TIMESTAMP WITH TIME ZONE,
    velocidade FLOAT,
    id_migracao_trajeto VARCHAR(100),
    sentido VARCHAR(100),
    trajeto VARCHAR(100),
    hodometro FLOAT,
    direcao INT,
    ignicao BIT
);