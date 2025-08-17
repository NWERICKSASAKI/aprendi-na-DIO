function main(){

    const backbutton = document.getElementById("backButton")
    backbutton.addEventListener("click", () => history.back())

    let params = new URLSearchParams(window.location.search);
    let id = params.get("id");
    getPokemon(id).then(pokemonData => {
        updateHTML(pokemonData);
    });
}

function getPokemon(id=1){
    const url = `https://pokeapi.co/api/v2/pokemon/${id}/`
    return fetch(url)
    .then( (response) => response.json()) 
    .then( convertPokeApiDetailToPokemon )
}

function updateHTML(pokemonData){
    const nome = document.getElementById("pokemonName")
    nome.textContent = pokemonData.name

    const id = document.getElementById("pokemonId")
    id.textContent = "#" + pokemonData.number
    
    const img = document.getElementById("pokemonImage")
    img.src = pokemonData.photo
    
    const h = document.getElementById("pokemonHeight")
    h.textContent = pokemonData.height + " m"

    const w = document.getElementById("pokemonWeight")
    w.textContent = pokemonData.weight + " kg"
    
    const abilities = document.getElementById("pokemonAbilities")
    abilities.textContent = pokemonData.abilities.join(', ')

    const t1 = document.getElementById("pokemonType1")
    t1.textContent = pokemonData.types[0]

    const t2 = document.getElementById("pokemonType2")
    t2.textContent = pokemonData.types[1]
    if (!(pokemonData.types[1])){
        t2.parentElement.removeChild(t2)
    }

    document.body.className = pokemonData.types[0]

    console.log(pokemonData)
}

main()