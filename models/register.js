$(function(){
    $("#register").on('click', function(event){
        event.preventDefault();
        var username   = $("#username").val();
        var password   = $("#password").val();
        
        if(!username || !password ||){ 
            $("#msgDiv").show().html("All fields are required.");
        }
        else{ 
            $.ajax({
                url: "/register",
                method: "POST",
                data: { user_name: username, password: password }
            }).done(function( data ) {
                if ( data ) {
                    if(data.status == 'error'){
                        var errors = '<ul>';
                        $.each( data.message, function( key, value ) {
                            errors = errors +'<li>'+value.msg+'</li>';
                        });
                        errors = errors+ '</ul>';
                        $("#msgDiv").html(errors).show();
                    }else{
                        $("#msgDiv").removeClass('invalid').addClass('valid').html(data.message).show(); 
                    }
                }
            });
        }
    });
});


//Code above from: 'http://programmerblog.net/nodejs-user-registration-tutorial/'