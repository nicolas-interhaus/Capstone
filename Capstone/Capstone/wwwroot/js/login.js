document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    // Obtener valores del formulario
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    let errores = [];

    if (!username) errores.push('El campo de nombre de usuario es obligatorio.');
    if (!password) errores.push('El campo de contraseña es obligatorio.');

    if (errores.length > 0) {
        alert(errores.join('\n'));
        return;
    }

    try {
        const response = await fetch('/Usuario/Login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            if (data.isAdmin) {
                window.location.href = '/Home/Admin_vista'; // Redirige a la vista admin
            } else {
                window.location.href = '/Home/DashboardUsuario'; // Redirige a la vista de usuario normal
            }
        } else {
            const errorData = await response.json();
            alert(errorData.Message || 'Usuario o contraseña incorrectos.');
        }
    } catch (error) {
        console.error('Error al intentar iniciar sesión:', error);
        alert('No se pudo conectar con el servidor.');
    }
});
