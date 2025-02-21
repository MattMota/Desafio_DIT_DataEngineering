SELECT DISTINCT
    codigo,
    placa
FROM {{ ref('brt_data') }}
;
