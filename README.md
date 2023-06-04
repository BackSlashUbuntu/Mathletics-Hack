# Mathletics-Hack
This is a code to hack Mathletics Live Points, you can choose accuracy, level, time, etc.



El código comienza solicitando al usuario que ingrese ciertos valores, como el valor de sesión, el nivel en el que se generarán los puntos, la cantidad de puntos a generar, el porcentaje de precisión deseado y el límite de tiempo.

Luego, se muestra un mensaje indicando que se están generando puntos.

El código entra en un bucle mientras haya puntos para generar. Dentro del bucle:

a. Se construye una URL específica utilizando el valor de sesión y el nivel proporcionados.

b. Se realiza una solicitud GET a la URL construida para obtener los datos relacionados con la pregunta.

c. Los datos de respuesta se analizan como JSON y se extraen el ID de la pregunta, el texto de la pregunta y las posibles respuestas.

d. El código verifica las respuestas para encontrar una que sea correcta y aún no haya sido seleccionada.

e. Si se encuentra una respuesta adecuada, se construye una nueva URL para guardar la respuesta proporcionada.

f. Se realiza una solicitud GET a la URL construida para guardar la respuesta.

g. El contador de puntos se reduce en uno.

h. El código espera el tiempo límite especificado antes de continuar con la siguiente iteración del bucle.

Una vez que se han generado todos los puntos deseados, se muestra un mensaje indicando que se ha completado.

En resumen, el código interactúa con el sitio web de Mathletics a través de solicitudes HTTP para obtener preguntas, seleccionar respuestas correctas y guardar las respuestas proporcionadas. Repite este proceso hasta generar la cantidad deseada de puntos.

Es importante tener en cuenta que, al igual que con el código anterior, el uso de este programa para generar puntos en Mathletics podría violar los términos de servicio del sitio web. Te recomendaría utilizarlo únicamente con fines educativos y bajo tu propia responsabilidad.
