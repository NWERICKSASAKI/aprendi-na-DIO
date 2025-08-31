const state = {
    sobreMim : document.getElementById("sobre-mim"),
    foto : document.getElementById("profile-pic"),
    idade : document.getElementById("idade"),
    endereco : document.getElementById("endereco"),
    estadoCivil : document.getElementById("estado-civil"),
    disponibilidadeViagem : document.getElementById("disponibilidade-viajar"),
    contato:{
        email : document.getElementById("email"),
        celular : document.getElementById("celular"),
        github : document.getElementById("github-link"),
        linkedin : document.getElementById("linkedin-link"),
        site : document.getElementById("site-link"),
    },
    softSkills : document.getElementById("soft-skills-lista"),
    experiencias : document.getElementById("experiencias-lista"),
    formacoes : document.getElementById("formacoes-lista"),
    certificacoes : document.getElementById("certificacoes-lista")
}


async function fetchProfileData() {
    const url = 'https://raw.githubusercontent.com/NWERICKSASAKI/aprendi-na-DIO/refs/heads/main/4%20JS/desafio-05/data/perfil.json';
    const response = await fetch(url)
    const profileData = await response.json()
    return profileData
}

async function substituirInformacoes(profile) {
   state.foto.src = profile.foto;
   state.sobreMim.textContent = profile["sobre-mim"];
   state.idade.textContent = profile.idade;
   state.estadoCivil.textContent = profile["estado-civil"];
   state.disponibilidadeViagem.textContent = profile["disponibilidade-viagem"];
   state.contato.email.textContent = profile.contato.celular;
}

async function init(){
    const profile = await fetchProfileData()
    substituirInformacoes(profile)
}

init();
