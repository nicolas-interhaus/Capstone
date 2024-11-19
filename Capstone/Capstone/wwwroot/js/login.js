async function iniciarSesion(username, password) {
    try {
        const response = await fetch('/api/UsuarioApi', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const usuario = await response.json();
            console.log('Usuario encontrado:', usuario);
            return usuario;
        } else {
            const errorData = await response.json();
            alert(errorData.Message || 'Error al iniciar sesión.');
        }
    } catch (error) {
        console.error('Error al conectarse a la API:', error);
    }
}
