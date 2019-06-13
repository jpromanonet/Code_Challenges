(function() {
					// Lista de frases
					var quotes = [
						{
							text: "Diagrama de Flijo."
						},
						{
							text: "Tengo un incendio en el trabajo."
                        },
                        {
							text: "uh la de red publica, privada tiene que estar."
                        },
                        {
							text: "A, B, C..."
                        },
                        {
							text: "Y si, el BPN es muy importante"
                        },
                        {
							text: "El tecnico."
                        },
                        {
							text: "Estoy desbordado."
                        },
                        {
							text: "A, B, 73..."
                        },
                        {
							text: "Tengo que volver al laburo."
                        },
                        {
                            text: "Vamo' a ser sinceros, no prepare la clase, pasa que me llamaron a ultimo momento(1ra clase)."
                        },
                        {
							text: "Los puntos de las IP son muy importantes"
                        },
                        {
							text: "La caratula es lo mas importante del trabajo."
                        },
                        {
							text: "El codigo ASCII."
                        },
                        {
							text: "Algo que vamos a usar cada día de nuestra vida, memorizatelo."
                        },
                        {
							text: "Firma: Cosme Bonilla ATR."
                        },
                        {
							text: "Las clases de Scratch."
                        },
                        {
							text: "Su compañero me pidió dar una clase, como me mostró que lo que iba a dar es muy interesante, lo voy a dejar."
                        },
                        {
							text: "Aliens!!!"
                        },
                        {
							text: "Los que dominan el mundo ni se conocen los apellidos."
                        },
                        {
							text: "Los presidentes, los Rotschild y los Rockefeller son todos titeres."
                        },
                        {
							text: "En la luna hay bases militares secretas."
                        },
                        {
							text: "Hubo un loco que descubrio el viaje en el tiempo y desaparecio."
                        },
                        {
							text: "Hay cosas que no sabemos y nos vamos a ir enterando."
                        },
                        {
							text: "Cuando nos llega la informacion es porque es mentira o es informacion vieja."
                        },
                        {
							text: "No me dira nada si lo leo?, no? (El Telettubie)"
                        },
                        {
							text: "El super-poder de leer como Macri(Gato) de Cosme ATR y el Telettubie."
                        },
                        {
							text: "Estoy cansado, sino ibamos a Uggi's y pediamos una pizza y unas birras."
                        },
                        {
							text: "No sabemos si la realidad que vemos es de verdad o no..."
                        },
                        {
							text: "No encuentro mucho..."
                        },
                        {
							text: "Me olvide"
                        },
                        {
							text: "¿Hay que estudiar mucho?"
                        },
                        {
							text: "Me parece que no hay que agregar mucho"
                        },
                        {
							text: "¿Qué es Mb y Gb?"
                        },
                        {
							text: "¿Que es Mhz y Ghz?"
                        },
                        {
							text: "¿La linea del tiempo la hago sin fechas?"
                        },
                        {
							text: "Te di mi mejor material"
                        }                      
					];
					// Quotes randomizer
					var quote = quotes[Math.floor(Math.random() * quotes.length)];
									document.getElementById("quote").innerHTML =
										'<p>' + quote.text + '</p>'
					})();