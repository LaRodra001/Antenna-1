async function AnswerFlask() {
            // Flask pregunta qué día es
            const QuestionResponse = await fetch("/get-coords");
            const QuestionData = await QuestionResponse.json();

            console.log("Flask asking:", QuestionData.question);

            // JavaScript obtiene la fecha del navegador
            const Coords = [500, 300];
            const state = true

            // El navegador envía la respuesta a Flask
            const AnswerResponse = await fetch("/answer-coords", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    pos: Coords,
                    state: state
                })
            });

            // Mostrar la respuesta de Flask
            const AnswerData = await AnswerResponse.json();

            document.getElementById("position").textContent =
                AnswerData.message[0];

            document.getElementById("status").textContent =
                AnswerData.message[1]
        }

        AnswerFlask();
