// Write the 2 initials of an idiom and click on the button
$(document).ready(() => {
    $('INPUT#btn_translate').click(() => {
        const idiom = $('INPUT#language_code').val();
        $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${idiom}`, (data) => {
            $('DIV#hello').html(data.hello);
        });
    });
});