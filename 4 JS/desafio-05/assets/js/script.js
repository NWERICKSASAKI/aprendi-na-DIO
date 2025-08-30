const html = {
    photo:document.getElementById("profile-pic"),
}

async function init(){
    const profile = await fetchProfileData()
    html.photo.src = profile.photo;     
}

async function fetchProfileData() {
    const url = 'https://raw.githubusercontent.com/NWERICKSASAKI/aprendi-na-DIO/refs/heads/main/4%20JS/desafio-05/data/perfil.json';
    const response = await fetch(url)
    const profileData = await response.json()
    return profileData
}

init();