// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.


use("cine");
// 1. Contar cuántas películas hay a partir del año 2000.
// db.peliculas.aggregate([
//     { $match: { year: {
//         $gte: 2000
//     }}},
//     { $count: "total" }
// ])

// 2. Mostrar el título, el año y el número de géneros de cada película. (Recuerda: genres es un array.)
// db.peliculas.aggregate([
//     {
//         $project: {
//             _id: 0,
//             title: 1,
//             year: 1,
//             genres: 1
//         }
//     }
// ])

// 3. Mostrar los 10 años con más películas.
// db.peliculas.aggregate([
//     {
//         $group: {
//             _id: "$year",
//             totalPeliculas: { $sum: 1 }
//         }
//     },
//     {
//         $sort: {
//             totalPeliculas: -1
//         }
//     },
//     {
//         $limit: 10
//     }
// ])

// 4. Clasificar las películas según su duración y contar cuántas hay de cada tipo, considerando:
// corta: duración menor que 90 minutos,
// media: duración entre 90 y 119 minutos,
// larga: duración mayor o igual que 120 minutos.
// db.peliculas.aggregate([
//     {
//         $project: {
//             _id: 0,
//             runtime: 1,
//             categoriaRuntime: {
//                 $switch: {
//                     branches: [
//                         {
//                             case: {
//                                 $lt: ["$runtime", 90]
//                             }, then: "corta"
//                         },
//                         {
//                             case: {
//                                 $gte: ["$runtime", 120]
//                             }, then: "larga"
//                         }
//                     ],
//                     default: "media"
//                 }
//             }
//         }
//     },
//     {
//         $group: {
//             _id: "$categoriaRuntime",
//             totalPeliculas: { $sum: 1 }
//         }
//     }
// ])

// 5. Mostrar el título, el año y un campo llamado epoca que indique:
// clasica si el año es anterior a 1980,
// moderna si está entre 1980 y 1999,
// actual si es del año 2000 o posterior.
// db.peliculas.aggregate([
//     {
//         $project: {
//             _id: 0,
//             title: 1,
//             year: 1,
//             epoca: {
//                 $switch: {
//                     branches: [
//                         {
//                             case: {
//                                 $lt: ["$year", 1980]
//                             }, then: "clasica"
//                         },
//                         {
//                             case: {
//                                 $gte: ["$year", 2000]
//                             }, then: "actual"
//                         }
//                     ],
//                     default: "moderna"
//                 }
//             }
//         }
//     }
// ])

// 6. Mostrar los 10 géneros con más películas (como genres es un array, tendrás que usar $unwind antes de agrupar.)
// db.peliculas.aggregate([
//     {
//         $unwind: {
//             path: "$genres"
//         }
//     },
//     {
//         $group: {
//             _id: "$genres",
//             totalPeliculas: { $sum: 1 }
//         }
//     },
//     {
//         $sort: {
//             totalPeliculas: -1
//         }
//     },
//     {
//         $limit: 10
//     }
// ])

// 7. Mostrar los 10 directores con más películas. (directors también es un array, así que vuelve a aparecer $unwind.)
// db.peliculas.aggregate([
//     {
//         $unwind: {
//             path: "$directors"
//         }
//     },
//     {
//         $group: {
//             _id: "$directors",
//             totalPeliculas: { $sum: 1 }
//         }
//     },
//     {
//         $sort: {
//             totalPeliculas: -1
//         }
//     },
//     {
//         $limit: 10
//     }
// ])

// 8. Clasificar las películas según su popularidad por número de votos en IMDb y mostrar el título, los votos y la etiqueta asignada. Utiliza estas reglas:
// poco votada: menos de 1000 votos,
// popular: entre 1000 y 50000 votos,
// muy popular: más de 50000 votos.
db.peliculas.aggregate([
    {
        $project: {
            _id: 0,
            title: 1,
            categoriaRuntime: {
                $switch: {
                    branches: [
                        {
                            case: {
                                $lt: ["$imdb.votes", 1000]
                            }, then: "muy popular"
                        },
                        {
                            case: {
                                $gt: ["$imdb.votes", 50000]
                            }, then: "poco votada"
                        }
                    ],
                    default: "popular"
                }
            }
        }
    }
])

// 9. Contar cuántas películas hay de cada tipo de popularidad (poco votada, popular, muy
// popular). (crea primero la etiqueta y después agrupa por ella.)