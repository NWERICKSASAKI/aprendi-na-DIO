async function init(){
    return
}

init();


async function fetchProfileData() {
    const url = 'https://raw.githubusercontent.com/NWERICKSASAKI/aprendi-na-DIO/refs/heads/main/4%20JS/desafio-05/data/profile.json';
    const response = await fetch(url)
    const profileData = await response.json()
    return profileData
}
