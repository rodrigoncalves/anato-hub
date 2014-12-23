ajax_request = false;

$.ajaxSetup({
    beforeSend: function(jqXHR) {
    ajax_request = jqXHR;
    },
});

function format_date (full_date) {
    date = full_date.split('T')[0];
    date = date.split('-');

    return date[2] + '/' + date[1] + '/' + date[0];
}

function search_user(){
    if(ajax_request){
        ajax_request.abort();
    }
    $('<div class="row"><div id="loading"</div></div>').insertAfter('#search-bar');
    $('#loading').addClass('small-centered columns text-center');
    $('#loading').html('<img src="/static/img/loader.gif">');

    var cpf_user = $('#search_user').val();

    $.ajax({
        type: "GET",
        url: "/procurar/" + cpf_user ,
        dataType: "json",
        success: function(data){
                $('#loading').remove();
                $('#search-results').remove();

                $('<br><div id="search-results"</div>').insertAfter('#search-bar');
                $('#search-results').addClass('row');

                $.each(data.users, function(i, user) {
                    $('#search-results').append('<div id="user' + i + '"></div>');
                    $('#user'+i).addClass('small-14 medium-10 large-10 small-centered columns');
                    $('#user'+i).append('<div id="informations' + i + '"></div>');
                    $('#user'+i).append('<div id="div-button' + i + '"></div>');

                    date = format_date(user.fields["date_joined"]);
                    $('#informations'+i).addClass('small-15 medium-10 large-10 columns');
                    $('#informations'+i).append('<h6><b><i>' + user.fields["username"] + '</i></b></h6>');
                    $('#informations'+i).append('<small>Pedido realizado em ' + date + '.</small>');

                    $('#div-button'+i).addClass('small-15 medium-5 large-5 columns');
                    $('#div-button'+i).append('<a href="/usuario/' + user["pk"] + '" id="button'+i+'">Selecionar</a>');

                    $('#button'+i).addClass('button small expand');
                    $('#user'+i).append('<hr>');

                })

                ajax_request = false;
            },
            error: function(request){
                $('#loading').remove();
                $('#search-results').remove();

                ajax_request = false;
            }
        })
    }

$(document).ready(
    $('#search_user').keyup( function(){
        search_user();
    })
)