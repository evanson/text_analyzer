$(document).ready(function() {
    $('#submit').click(function() {
        $(this).attr('disabled', true);
    });

    $("#box").submit(function (e) {
        e.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/",
            data: formData
        }).done(processWords);
    });

    function processWords(data){
        $("#submit").removeAttr("disabled");
        words = $.parseJSON(data);
        var table = $('<table></table>');
        table.append($('<thead><tr><<th>Word</th><th>Frequency</th></tr></thead>')) ;
        var tbody = $('<tbody></tbody>');
        jQuery.each(words, function(index, word) {
            var row = $("<tr><td>"+word[0]+"</td><td>"+word[1]+"</td></tr>");
            tbody.append(row);
        });
        table.append(tbody);
        $("#wordcount").append(table);
    }
});