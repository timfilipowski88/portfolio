$(document).ready(function(){
    $('#hours_btn').click(function(e){
        e.preventDefault()
        $('#hours_card').append(
            "<p>New Paragraph!</p>"
        );
    });
});