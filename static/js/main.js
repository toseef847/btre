const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#message').fadeOut('slow')
}, 4000);

$('#pw2').on('focusout', function(e){
	const pw1 = $('#pw1').val();
	if ($(this).val() != pw1){
		$('#pw_err').text('Passwords do not match');
	}
});