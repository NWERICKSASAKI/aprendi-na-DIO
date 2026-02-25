const form = document.getElementById("login-form");
const msg  = document.getElementById("msg");

form.addEventListener("submit", async (e) => {
    msg.innerText = "aaabbb";
    e.preventDefault();

    const id = document.getElementById("username").value;
    const senha = document.getElementById("password").value;

    const response = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cliente_id: parseInt(id),
            senha: senha,
            is_adm: true
        })
    });

    const data = await response.json();
    alert(JSON.stringify(data));

    if (response.status === 200) {
        msg.innerText = "Login feito com sucesso";

        // salvar token
        localStorage.setItem("token", data.access_token);

        // redirecionar
        window.location.href = "/home";
    }
    else if (response.status === 401) {
        msg.innerText = "Usuário ou senha errado";
    }
    else if (response.status === 405) {
        msg.innerText = "Vish";
    }
    else {
        msg.innerText = "Erro inesperado";
    }
});
