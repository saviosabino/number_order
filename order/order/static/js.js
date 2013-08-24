google.load("visualization", "1", {packages:["corechart"]});
//google.setOnLoadCallback(drawChart);
function drawChart(arr) {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Index');
    data.addColumn('number', 'Value');
    data.addRows(arr.length);
    
    for(x=0; x< arr.length; x++){
        data.setValue(x, 0, x+'');
        data.setValue(x, 1, arr[x]);
    }

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, {width: 400, height: 240, title: 'Ordered List'});
}

$(document).ready(function(){

    $('#divValues').hide();
    $('#divResult').hide();
    $('#inputQt').focus();

    $('#subQt').click(function(event){
        $('#divQt').hide();
        $('#divValues').show();
        //show fields...
        var qtVal = $('#inputQt').val(); qtVal = parseInt(qtVal);
        if (!isNaN(qtVal)){
            for (x = 1; x <= qtVal; x++){
                $('#divFields').append(
                    '<input size="5" type="text" id="val' + x + '" >')
            }
            $('#val1').focus();
        } else {alert('Digite um número'), window.location ='/order/'}
        event.preventDefault();
    })

    $('#subValues').click(function(event){
        $('#divValues').hide();
        $('#divResult').show();
        //show result
        var $qrVal = $('#divValues :input');
        listVal = '';
        $qrVal.each(function(){
            listVal += $(this).val(); listVal += ',';
        });
        listVal = listVal.replace(',,', '');
        
        $.ajax({
            url: '/order/result/',
            data: {'listVal': listVal, csrfmiddlewaretoken: '{{ csrf_token }}'},
            type: 'POST',
            success: function(retVal){
                $('#divRes').html(retVal);
                drawChart(arr);
                
            },
            error: function(xhr, textStatus, errorThrown){
                alert("Error: " +textStatus)
            }
        });
        event.preventDefault();
    })
});
 