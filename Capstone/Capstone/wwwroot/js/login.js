document.getElementById('loginForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Prevenir el envío por defecto del formulario

    // Obtener valores de los campos
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    let errores = [];

    // Validaciones básicas
    if (!username) errores.push('El campo de nombre de usuario es obligatorio.');
    if (!password) errores.push('El campo de contraseña es obligatorio.');

    if (errores.length > 0) {
        alert(errores.join('\n')); // Mostrar errores si los hay
    } else {
        try {
            // Enviar los datos al servidor usando fetch
            const response = await fetch('/Usuario/Login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                // Si el servidor retorna un éxito, redirigir según el rol
                const data = await response.json();
                console.log("encontro la data")
                if (data.isAdmin) {
                    window.location.href = '/Home/Admin_vista'; // Redirige a la vista de administrador
                } else {
                    window.location.href = '/Home/DashboardUsuario'; // Redirige a la vista de usuario
                }
            } else if (response.status === 401) {
                // Manejo de credenciales incorrectas
                alert('Usuario o contraseña incorrectos.');
            } else {
                // Otros errores
                alert('Ocurrió un error al procesar la solicitud.');
            }   
        } catch (error) {
            console.error('Error al conectar con el servidor:', error);
            alert('No se pudo conectar con el servidor.');
        }
    }
});
