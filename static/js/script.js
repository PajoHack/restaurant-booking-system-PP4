$(document).ready(function() {
    console.log('Script loaded')
    $("#tables, #date, #time-input, #guests").change(function() {
        var tableIds = $("#tables").val();
        var date = $("#date").val();
        var time = $("#time-input").val();
        var guests = $("#guests").val();

        // Only proceed if all four fields have a value
        if (tableIds && date && time && guests) {
            // Loop over each table ID and make a separate AJAX call for each one
            for (var i = 0; i < tableIds.length; i++) {
                $.ajax({
                    url: '/check_table_availability/',  // URL of Django view
                    data: {
                        'table_id': tableIds[i],
                        'date': date,
                        'time': time,
                        'guests': guests,
                    },
                    dataType: 'json',
                    success: function (data) {
                        if (data.is_available) {
                            // If the table is available, enable the booking button
                            $("#booking-button").prop("disabled", false);
                            $("#availability-message").text("");
                            $("#booking-feedback").text("Table is available.");
                        } else {
                            // If the table is not available, disable the booking button and display a message
                            $("#booking-button").prop("disabled", true);
                            $("#availability-message").text("One or more selected tables are not available at the selected time. Please select different times or tables.");
                            $("#booking-feedback").text("Table is not available.");
                        }
                    }
                    
                });
            }
        }
    });
    
    $('.timepicker').timepicker({
        'timeFormat': 'H:i',
        'minTime': '12:00',
        'maxTime': '21:30',
        'step': 30  // increment of 30 minutes
    });    
    
});