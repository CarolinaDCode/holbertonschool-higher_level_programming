// get the value of hello from the URL
// 'https://fourtonfish.com/hellosalut/?lang=fr'
// and add it to the id hello
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});