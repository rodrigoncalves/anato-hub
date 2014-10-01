// Disabling Enter button
$(document).ready( function() {
    if ($('#username').val() != '' && $('#password').val() != '') {
        $('#enter-button').removeAttr('disabled');
    } else {
        $('#enter-button').attr('disabled', 'disabled');
    }
})

$('#username').keyup(function () {
    if ($(this).val() != '' && $('#password').val() != '') {
        $('#enter-button').removeAttr('disabled');
    } else {
        $('#enter-button').attr('disabled', 'disabled');
    }
})

$('#password').keyup(function () {
    if ($(this).val() != '' && $('#username').val() != '') {
        $('#enter-button').removeAttr('disabled');
    } else {
        $('#enter-button').attr('disabled', 'disabled');
    }
})