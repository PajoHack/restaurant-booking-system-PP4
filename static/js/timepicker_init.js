$(document).ready(function(){
    $('.timepicker').timepicker({
        'timeFormat': 'H:i',
        'minTime': '12:00',
        'maxTime': '21:30',
        'step': 30  // increment of 30 minutes
    });
});

