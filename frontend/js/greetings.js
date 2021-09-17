function greetings_fn() {
    nombre = document.getElementById("name").value
    url = `${base_url}saludo?name=${nombre}`
    makeRequest("GET", url, (code, response) => {
        if (code == 200) {
            datos = JSON.parse(response)
            document.getElementById("greeting-response").innerHTML = datos.mensaje
        } else {
            console.log("error en la peticion ", code)
        }
    })

}