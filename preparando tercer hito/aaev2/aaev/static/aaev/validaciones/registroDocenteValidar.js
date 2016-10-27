$(function() {

	$("form[name='registrarDocente']").validate({

		rules:{
			nombre: {
				required: true,
				maxlength: 30
				},
			apellido: {
				required: true,
				maxlength: 30
				},
			dni: {
				required: true,
				number: true,
				maxlength:30
			},
			mail: {
				required: true,
				email: true,
				maxlength: 30
			},
		},
		messages: {
			nombre: "Por favor, ingresa tu nombre",
			apellido: "Por favor, ingresa tu apellido",
			dni: {
				required: "El DNI es obligatorio",
				number: "El dni tiene que ser un numero",
			},
			mail: {
				required: "El mail es obligatorio",
				mail: "El mail no es valido"
			}
		},
		submitHandler: function(registrarDocente){
			registrarDocente.submit();	
		}
		

	});

}); 