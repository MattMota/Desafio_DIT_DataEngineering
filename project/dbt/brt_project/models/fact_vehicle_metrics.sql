{{ config(materialized='table') }}

SELECT
    id,
    latitude,
    longitude,
    dataHora,
    velocidade
FROM {{ ref('brt_data') }}
;
