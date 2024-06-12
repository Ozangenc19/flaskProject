CREATE VIEW vue_nouveaute AS
SELECT
    id_nouveaute,
    nom_nouveaute,
    image_nouveaute,
    prix_nouveaute,
    description
FROM
    nouveaute;
