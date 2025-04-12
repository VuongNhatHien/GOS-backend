CREATE TABLE scores (
    id             VARCHAR(10) PRIMARY KEY,
    toan           FLOAT,
    ngu_van        FLOAT,
    ngoai_ngu      FLOAT,
    vat_li         FLOAT,
    hoa_hoc        FLOAT,
    sinh_hoc       FLOAT,
    lich_su        FLOAT,
    dia_li         FLOAT,
    gdcd           FLOAT,
    ma_ngoai_ngu   VARCHAR(2),
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);