// Get Current Date in Footer 
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

//  Auto Hide Alert message after 4 sec
setTimeout(function(e){
    $('#message').fadeOut();
}, 4000);

// Check if the passwords are same (Registration page)
$('#pw2').on('input', function(e){
	const pw1 = $('#pw1').val();
	if ($(this).val() != pw1){
		$('#pw_err').text('Passwords do not match');
		$('#btn_reg').attr('disabled', 'disabled');
	}
	else{
		$('#pw_err').text('');
		$('#btn_reg').attr('disabled', false)
	}
});
$('#pw1').on('input', function(e){
	const pw2 = $('#pw2').val();
	if ($(this).val() != pw2){
		$('#pw_err').text('Passwords do not match');
		$('#btn_reg').attr('disabled', 'disabled')
	}
	else{
		$('#pw_err').text('');
		$('#btn_reg').attr('disabled', false)
	}
});