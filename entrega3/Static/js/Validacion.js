$(document).ready(function () {

    $("#Contacto").validate({
        rules: {
            Nombre: {
                required: true,
                minlength: 10
            },
            Ciudad: {
                required: true,
                minlength: 5,
                maxlength: 50
            },
            Numrut: {
                required: true,
                minlength: 15
            },
            Email: {
                required: true,
                email: true
            },
            Requerimiento: {
                required: true,
                minlength: 30
            }
        },

        messages: {
            Nombre: {
                required: "Es necesario su Nombre.",
                minlength: "El mínimo es de 10 caracteres."
            },
            Numrut: {
                required: "Ingrese su rut o pasaporte sin puntos y sin guión",
                minlength: "El mínimo es de 15 caracteres."
            },
            Email: {
                required: "Debe escribir su correo.",
                email: "Ingrese un Correo valido."
            },
            Requerimiento: {
                required: "Debe escribir su requerimiento.",
                minlength: "Debe contener al menos 30 caracteres."
            },
            Ciudad: {
                required: "Es necesario ingresar su ciudad",
                minlength: "5 caracteres como minimo"
            }
        }
    })

});