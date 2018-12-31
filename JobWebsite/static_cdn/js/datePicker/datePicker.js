$(document).ready(function () {
    $(function () {
        $(".datepicker").datepicker({ 
            dateFormat: 'dd MM yy',       
            changeMonth: true,
            changeYear: true,
            yearRange: "1900:2048"
        });
    });
});