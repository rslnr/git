function login () {
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;
    if (user === "admin" && pass === "admin") {
        alert ("successful login!")
    }
    else {
        alert ("incorrect login or password, please try again!")
    }
}
login()
