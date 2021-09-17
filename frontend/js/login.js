function login_fn() {
    url = `${base_url}login`
    body = {
        user: document.getElementById("user").value,
        passwd: document.getElementById("passwd").value
    }
    makeRequest("POST", url, (code, response) => {
        if (code == 200) {
            datos = JSON.parse(response)
            alert(datos.mensaje)
        } else {
            console.log("error en la peticion ", code)
        }
    }, JSON.stringify(body))

}