document.getElementById('registroForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita el comportamiento por defecto del formulario

    // Obtener valores de los campos
    const rut = document.getElementById('rut').value.trim();
    const nombres = document.getElementById('nombres').value.trim();
    const apellidoPaterno = document.getElementById('apellido_paterno').value.trim();
    const apellidoMaterno = document.getElementById('apellido_materno').value.trim();
    const fechaNacimiento = document.getElementById('fecha_nacimiento').value.trim();
    const genero = document.getElementById('inputGender').value;
    const direccion = document.getElementById('inputAddress').value.trim();
    const villa = document.getElementById('inputAddress2').value.trim();
    const ciudad = document.getElementById('inputCity').value.trim();
    const comuna = document.getElementById('inputState').value;
    const codigoPostal = document.getElementById('inputPostal').value.trim();
    const email = document.getElementById('inputEmail4').value.trim();
    const usuario = document.getElementById('inputUsuario').value.trim();
    const cargo = document.getElementById('inputCargo').value;
    const password = document.getElementById('inputPassword4').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const aceptaCondiciones = document.getElementById('gridCheck').checked;

    let errores = [];

    // Validaciones
    if (!rut) errores.push('El campo Rut es obligatorio.');
    if (!nombres) errores.push('El campo Nombres es obligatorio.');
    if (!apellidoPaterno) errores.push('El campo Apellido Paterno es obligatorio.');
    if (!apellidoMaterno) errores.push('El campo Apellido Materno es obligatorio.');
    if (!fechaNacimiento) errores.push('El campo Fecha de Nacimiento es obligatorio.');
    if (!genero) errores.push('Debe seleccionar un género.');
    if (!direccion) errores.push('El campo Dirección es obligatorio.');
    if (!comuna) errores.push('Debe seleccionar una comuna.');
    if (!email) errores.push('El campo Email es obligatorio.');
    if (!usuario) errores.push('El campo Usuario es obligatorio.');
    if (!password || password !== confirmPassword) errores.push('Las contraseñas no coinciden.');
    if (!aceptaCondiciones) errores.push('Debe aceptar las condiciones de uso.');

    if (errores.length > 0) {
        alert(errores.join('\n')); // Muestra los errores al usuario
    } else {
        alert('Formulario enviado con éxito');
        // Aquí puedes hacer el envío de los datos a tu servidor
    }
});
