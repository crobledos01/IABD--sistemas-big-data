
// 1. Carga inicial del sistema
// Importa el fichero personas.json en una colección llamada personas.
// mongoimport --db personas --collection personas --file personas.json
use('personas')
// Comprueba cuántos documentos existen.
db.personas.countDocuments()
// Muestra qué índices están creados inicialmente en la colección.
db.personas.getIndexes()
// 2. Búsqueda directa de empleado
// Realiza una consulta por _id.
db.personas.find({ _id: ObjectId("69b1a1bf5d6a19bddf19dba1") })
// Ejecuta también explain(“executionStat”) y analiza si MongoDB utiliza un índice.
db.personas.explain("executionStats").find({ _id: "69b1a1bf5d6a19bddf19dba1" })
// Utiliza índice porque indexName: '_id_' se encuentra dentro de executionStats.

// 3. Filtrado salarial (departamento financiero)
// Ejecuta explain y comprueba si aparece COLLSCAN.
db.personas.find({ ingresos: { $gt: 7000 } })
db.personas.explain("executionStats").find({ ingresos: { $gt: 7000 } })
// Dentro de winningPlan aparece stage: 'COLLSCAN'
// Decide si esta consulta debería optimizarse con un índice.
// Justifica brevemente tu decisión.
// Sï, debería optimizarse con un índice porque es una consulta que se realiza
//      a menudo. Al no tener un índice, esto hace que se deba escanear la
//      colección completa, afectando al rendimiento de la consulta

// 4. Consulta masiva
// En un informe anual, la empresa realiza una consulta que devuelve prácticamente toda la
// colección.
db.personas.find({ ingresos: { $gt: 0 } })
// Explica si un índice tendría sentido en este caso o no.
// En este caso, un índice no sería necesario, ya que es una consulta que se
//      realiza una vez al año y devuelve prácticamente toda la colección

// 5. Búsquedas geográficas (equipo internacional)
db.personas.explain("executionStats").find({ "direccion.pais": "Fiji" })
// Analiza con explain si se recorre toda la colección.
// En winningPlan aparece stage: 'COLLSCAN', por lo que se recorre toda la colección
// Decide si un índice es recomendable para búsquedas frecuentes por país.
// Justifica tu respuesta.
// Sí, un índice es recomendable para búsquedas frecuentes por país, ya que
//      existen personas de muchos países distintos y si no se realizan índices 
//      puede bajar mucho el rendimiento

// 6. Procesos locales (pais + ciudad)
db.personas.find({ "direccion.pais": "Fiji", "direccion.ciudad": "Suva" })
// Comprueba con explain si la consulta es eficiente.
db.personas.explain("executionStats").find(
    { "direccion.pais": "Fiji", "direccion.ciudad": "Suva" }
)
// Decide qué estrategia de índice sería la más adecuada.
// La estrategia de índice más adecuada sería un índice compuesto sobre los campos
//      direccion.pais y direccion.ciudad, ya que esto permitiría optimizar las
//      consultas que filtren por ambos campos al mismo tiempo.
// Implementa tu solución y analiza el resultado.
db.personas.createIndex({ "direccion.pais": 1, "direccion.ciudad": 1 })
db.personas.explain("executionStats").find(
    { "direccion.pais": "Fiji", "direccion.ciudad": "Suva" }
)
// Ahora en winningPlan aparece stage: 'IXSCAN', por lo que la consulta es
//      más eficiente y se ha optimizado con el índice compuesto creado

// 7. Preferencias (arrays multikey)
// Realiza una consulta sobre el array colores.
// Comprueba con explain si se realiza COLLSCAN.
// Decide si un índice multikey tendría sentido.


// 8. Ejercicio abierto: consulta de la empresa
// Elige una consulta diferente sobre la colección personas.
db.personas.find( { colores: "purple" })
// Analízala con explain.
db.personas.explain("executionStats").find( { colores: "purple" } )
// Decide si necesita un índice.
db.personas.find()
// Justifica tu decisión y comprueba como afecta al rendimiento.


// 9. Informe final de rendimiento
// Indica qué índices serían imprescindibles en un sistema real.
// Indica qué índices no crearías para no perjudicar inserciones y actualizaciones.
// Explica brevemente tus decisiones.