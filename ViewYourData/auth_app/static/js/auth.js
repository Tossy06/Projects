// auth.js

document.addEventListener("DOMContentLoaded", () => {
    // Seleccionar los botones y los formularios
    const btnLogin = document.getElementById("login-change");
    const btnRegister = document.getElementById("register-change");
    const registerForm = document.getElementById("register");
    const loginForm = document.getElementById("login");
    const formContent = document.querySelector(".form-content");

    // Mostrar solo el formulario de registro al principio
    registerForm.style.display = "block";
    loginForm.style.display = "none";
    formContent.classList.add("fade-in");

    // Función para manejar el cambio de formulario
    function changeForm(formToShow, formToHide) {
        // Aplicar la animación de desvanecimiento de salida al formulario actual
        formToHide.classList.add("fade-out");
        formToHide.classList.remove("fade-in");

        // Esperar que termine la animación antes de cambiar el formulario
        setTimeout(() => {
            formToShow.style.display = "block";
            formToHide.style.display = "none";

            // Aplicar la animación de desvanecimiento de entrada al nuevo formulario
            formToShow.classList.add("fade-in");
            formToShow.classList.remove("fade-out");
        }, 300); // Espera el tiempo de animación (0.3s) antes de cambiar de formulario
    }

    // Mostrar el formulario de login al hacer clic en "login"
    btnLogin.addEventListener("click", () => {
        changeForm(loginForm, registerForm);
    });

    // Mostrar el formulario de registro al hacer clic en "Register"
    btnRegister.addEventListener("click", () => {
        changeForm(registerForm, loginForm);
    });
});