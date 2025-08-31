const state = {
    sobreMim : document.getElementById("sobre-mim"),
    foto : document.getElementById("profile-pic"),
    idade : document.getElementById("idade"),
    endereco : document.getElementById("endereco"),
    estadoCivil : document.getElementById("estado-civil"),
    disponibilidadeViagem : document.getElementById("disponibilidade-viajar"),
    contato : document.getElementById("contato"),
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


async function changeSobreMim(profile) {
    state.foto.src = profile.foto;
    state.sobreMim.textContent = profile["sobre-mim"];
    state.idade.textContent = profile.idade;
    state.estadoCivil.textContent = profile["estado-civil"];
    state.disponibilidadeViagem.textContent = profile["disponibilidade-viagem"];
}


async function addContato(profile) {

    let htmlParaAcrescentar = ''
    
    const emailContent = profile.contato.email;
    if (!!emailContent){
        const icon = '<i class="fa-solid fa-envelope"></i>';
        htmlParaAcrescentar += `<li>${icon}<span>${emailContent}</span></li>`;       
    }
    
    const celularContent = profile.contato.celular;
    if (!!celularContent){
        const icon = '<i class="fa-brands fa-whatsapp"></i>';
        htmlParaAcrescentar += `<li>${icon}<span>${celularContent}</span></li>`;       
    }

    const githubContent = profile.contato.github;
    if (!!githubContent){
        const icon = '<i class="fa-brands fa-github"></i>';
        const textContent = githubContent.replace("https://github.com/","");
        const href = githubContent;
        htmlParaAcrescentar += `<li>${icon}<a target="_blank" href="${href}">${textContent}</a></li>`;       
    }

    const linkedinContent = profile.contato.linkedin;
    if (!!linkedinContent){
        const icon = '<i class="fa-brands fa-linkedin-in"></i>';
        const textContent = linkedinContent.replace("https://www.linkedin.com/in/","");
        const href = linkedinContent;
        htmlParaAcrescentar += `<li>${icon}<a target="_blank" href="${href}">${textContent}</a></li>`;       
    }

    const siteContent = profile.contato.site;
    if (!!siteContent){
        const icon = '<i class="fa-solid fa-globe"></i>';
        const textContent = siteContent.replace("https://www.linkedin.com/in/","");
        const href = siteContent;
        htmlParaAcrescentar += `<li>${icon}<a href="${href}">${textContent}</a></li>`;       
    }
    state.contato.innerHTML = htmlParaAcrescentar;       
}


async function addSoftSkills(profile){
    const lista = profile["soft-skills"];
    let htmlParaAcrescentar = ''
    lista.forEach(skill => {
        const htmlString = `<li>${skill.icone}<span>${skill.nome}</span></li>`;
        htmlParaAcrescentar += htmlString;
    });
    state.softSkills.innerHTML += htmlParaAcrescentar;
}


async function addExperiencias(profile){
    const lista = profile.experiencias;
    const htmlParaAcrescentar = ''
    lista.forEach(info => {

        const htmlString =
        `<li>
            <h3>${info.icone}${info.cargo}</h3>
            <p>
                ${info['data-inicio']} - ${info['data-fim']}
                <br>
                <span class="empresa>${info.empresa}</span>
                <div class="maisInfo">
                    ${info["descricao-atividade"]}
                </div>
            </p>
        </li>`
        htmlParaAcrescentar += htmlString

    });
    state.experiencias.innerHTML = htmlString;
}


async function init(){
    const profile = await fetchProfileData();
    changeSobreMim(profile);
    addContato(profile);
    addSoftSkills(profile);
    addExperiencias(profile);
}


init();
