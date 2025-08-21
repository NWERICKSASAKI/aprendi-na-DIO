const url = 'https://nwericksasaki.github.io/aprendi-na-DIO/4%20JS/desafio-01/index.js'

fetch(url)
.then(response => response.text())
.then(texto => {
    document.getElementById("desafio-js").textContent = texto
})
.catch(err => console.error(err));