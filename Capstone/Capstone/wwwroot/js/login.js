document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitar el comportamiento por defecto

    // Obtener valores de los campos
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const rememberMe = document.getElementById('rememberMe').checked;

    let errores = [];

    // Validaciones
    if (!username) errores.push('El campo de nombre de usuario es obligatorio.');
    if (!password) errores.push('El campo de contraseña es obligatorio.');

    if (errores.length > 0) {
        alert(errores.join('\n')); // Mostrar errores si los hay
    } else {
        // Aquí puedes hacer el envío de los datos al servidor o cualquier otra acción
        alert('Inicio de sesión exitoso');
        // Envío del formulario si pasa las validaciones
        document.getElementById('loginForm').submit();
    }
});
