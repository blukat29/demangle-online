
function onLangSelect() {
    var sample = $('#lang option:selected').data().sample;
    $('#example').text('Try ' + sample);
}

$('#lang').on('changed.bs.select', onLangSelect);
$('#lang').on('loaded.bs.select', onLangSelect);

$('#go').click(function() {
    var names = $('#src').val();
    var lang = $('#lang option:selected').val();
    $.ajax({
        type: 'POST',
        url: '/run',
        data: {names: names, lang: lang},
        dataType: 'text',
        success: function(resp) {
            $('#dst').text(resp);
        },
        error: function(a,b,c) {
            console.log("ERROR");
            console.log(a);
            console.log(b);
            console.log(c);
        }
    });
});

