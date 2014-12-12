ajax_request = false;

$.ajaxSetup({
    beforeSend: function(jqXHR) {
    ajax_request = jqXHR;
    },
});

function search_user(){
    if(ajax_request){
        ajax_request.abort();
    }

    var cpf_user = $('#search_user').val()

    $.ajax({
        type: "GET",
        url: "/procurar/" + cpf_user ,
        dataType: "json",
        success: function(lista){

                ajax_request = false;
            },
            error: function(){

                ajax_request = false;
            }
        })
    }

$(document).ready(
    $('#search_user').keyup( function(){
        search_user();
    })
)