// The header will change to red, when you click on DIV#red_header
// but now a css style will be added
$('DIV#red_header').click(function(){
    $('header').addClass('red');
});