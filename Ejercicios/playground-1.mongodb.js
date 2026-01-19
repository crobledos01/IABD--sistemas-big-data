// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("libreria");

// 1. Mostrar los libros cuyo precio sea mayor o igual que 25.
// db.libros.aggregate([
//     {
//         $match: {
//             precio: {
//                 $gte: 25
//             }
//         }
//     }
// ])

// 2. Mostrar únicamente el título y el precio de todos los libros.
// db.libros.aggregate([
//     {
//         $project: {
//             _id: 0,
//             titulo: 1,
//             precio: 1
//         }
//     }
// ])
// 4. Calcular cuántos libros hay por editorial.
// db.libros.aggregate([
//     {
//         $group: {
//             _id: "$editorial",
//             totalPorEditorial: { $sum: 1 }
//         }
//     }
// ])

// 5. Calcular el precio medio de los libros por editorial y ordenar el resultado de menor a mayor.
// db.libros.aggregate([
//     {
//         $group: {
//             _id: "$editorial",
//             mediaPorEditorial: { $avg: "$precio" }
//         }
//     },
//     {
//         $sort: {
//             mediaPorEditorial: 1
//         }
//     }
// ])

// 6. Para cada libro, crear un campo llamado stockAlto que valga true si la cantidad de ese
// libro es mayor o igual que 20, y false en caso contrario. (No hay que agrupar, solo añadir
// el campo).
// db.libros.aggregate([
//     {
//         $project: {
//             _id: 0,
//             titulo: 1,
//             stockAlto: {
//                 $switch: {
//                     branches: [
//                         {
//                             case: {
//                                 $gte: ["$cantidad", 20]
//                             }, then: true
//                         }
//                     ],
//                     default: false
//                 }
//             } 
//         }
//     }
// ])

// 7. Para cada libro, crear un campo llamado estadoLibro que indique:
// agotado si la cantidad es 0,
// pocas unidades si la cantidad es menor que 5,
// disponible en cualquier otro caso.


// 8. Para cada libro, clasificarlo como rentable o no rentable en función de si el valor del stock
// (precio multiplicado por cantidad) es mayor o igual que 500.


// 9. Contar cuántos libros hay de cada tipo de estadoLibro. (crea primero el campo con una
// condición y después agrupa.)