$(function(){
	
	$("form[name='iniciarSesion']").validate({
	
		rules:{
			usuario: "required",
			clave: "required"
		},
		messages: {
			usuario: "Ingresa un usuario para iniciar sesion",
			clave: "Ingresa tu clave para iniciar sesion"
			
		},
		submitHandler: function(iniciarSesion){
			iniciarSesion.submit();
		}
		
	
	});

});